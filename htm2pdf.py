import asyncio
import re
import sys
from pathlib import Path
from playwright.async_api import async_playwright

async def generate_pdf():
    print("Drop the HTML file here and press Enter:")
    user_input_path = input("> ").strip()

    cleaned_file_path = user_input_path.strip('\'"').replace('\\ ', ' ')
    html_file = Path(cleaned_file_path)

    if not html_file.exists() or not html_file.is_file():
        print(f"\nError: Invalid file path '{html_file}'.")
        sys.exit(1)

    if html_file.suffix.lower() not in ['.html', '.htm']:
        print("\nError: Unsupported file type. Please provide an HTML file.")
        sys.exit(1)

    pdf_file = html_file.with_suffix('.pdf')

    print("\nSelect PDF rendering mode:")
    print("1 → Continuous single-page PDF")
    print("2 → Standard A4 paginated PDF")
    print("3 → Custom page-break mode (string based)\n")

    selected_mode = input("Enter option number:\n> ").strip()

    if selected_mode not in ['1', '2', '3']:
        print("\nError: Invalid option selected.")
        sys.exit(1)

    split_marker = ""
    if selected_mode == '3':
        split_marker = input("\nEnter the custom page break marker string:\n> ").strip()

    print("\nEnable Monochrome Print Mode?")
    print("This makes text, lines, and borders pure black while preserving background colors.")
    mono_choice = input("(y/n):\n> ").strip().lower()
    enable_mono = mono_choice == 'y'

    print("\nStarting conversion...")
    async with async_playwright() as playwright_instance:
        browser = await playwright_instance.chromium.launch()
        page = await browser.new_page()

        await page.emulate_media(media="screen")

        css_injection = """
        * {
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
        """

        if enable_mono:
            css_injection += """
            * {
                color: #000000 !important;
                border-color: #000000 !important;
            }
            svg {
                stroke: #000000 !important;
            }
            hr {
                background-color: #000000 !important;
                border-color: #000000 !important;
            }
            """

        layout_flattener_js = """() => {
            const get_bg = (el) => window.getComputedStyle(el).backgroundColor;
            let target_bg = get_bg(document.body);

            if (target_bg === 'rgba(0, 0, 0, 0)' || target_bg === 'transparent') {
                const wrapper = document.querySelector('div') || document.querySelector('article');
                if (wrapper) target_bg = get_bg(wrapper);
            }

            if (target_bg && target_bg !== 'rgba(0, 0, 0, 0)') {
                document.documentElement.style.setProperty('background-color', target_bg, 'important');
                document.body.style.setProperty('background-color', target_bg, 'important');
            }

            document.querySelectorAll('*').forEach(el => {
                const computed = window.getComputedStyle(el);
                if (computed.height.includes('vh') || computed.height === '100%') {
                    el.style.setProperty('height', 'auto', 'important');
                }
                if (computed.overflow === 'hidden' || computed.overflow === 'auto' || computed.overflow === 'scroll') {
                    el.style.setProperty('overflow', 'visible', 'important');
                }
            });
        }"""

        if selected_mode == '1':
            print("Loading HTML...")
            await page.goto(html_file.resolve().as_uri(), wait_until="networkidle")
            await page.add_style_tag(content=css_injection)
            await page.evaluate(layout_flattener_js)

            page_height = await page.evaluate("document.body.scrollHeight")

            pdf_settings = {
                "path": str(pdf_file),
                "width": "1080px",
                "height": f"{page_height + 500}px",
                "margin": {"top": "0", "right": "0", "bottom": "0", "left": "0"},
                "print_background": True,
            }

            print("Generating Continuous PDF...")
            await page.pdf(**pdf_settings)

        elif selected_mode == '2':
            print("Loading HTML...")
            await page.goto(html_file.resolve().as_uri(), wait_until="networkidle")
            await page.add_style_tag(content=css_injection)
            await page.evaluate(layout_flattener_js)

            pdf_settings = {
                "path": str(pdf_file),
                "format": "A4",
                "print_background": True,
            }

            print("Generating Standard A4 PDF...")
            await page.pdf(**pdf_settings)

        elif selected_mode == '3':
            print("Loading HTML...")
            raw_html_text = html_file.read_text(encoding='utf-8')

            body_tag_search = re.search(r'<body([^>]*)>(.*?)</body>', raw_html_text, flags=re.IGNORECASE | re.DOTALL)
            body_attributes = body_tag_search.group(1) if body_tag_search else ""
            extracted_body = body_tag_search.group(2) if body_tag_search else raw_html_text

            extracted_body = extracted_body.strip()
            first_tag_match = re.match(r'^<([a-zA-Z0-9\-]+)([^>]*)>', extracted_body)

            wrapper_tag = "div"
            wrapper_attributes = ""

            if first_tag_match:
                wrapper_tag = first_tag_match.group(1)
                wrapper_attributes = first_tag_match.group(2)
                extracted_body = extracted_body[first_tag_match.end():]
                closing_tag = f"</{wrapper_tag}>"
                if extracted_body.rstrip().endswith(closing_tag):
                    extracted_body = extracted_body.rstrip()[:-len(closing_tag)]

            raw_sections = extracted_body.split(split_marker)
            valid_sections = [section for section in raw_sections if section.strip()]

            if not valid_sections:
                print(f"\nError: Marker string '{split_marker}' not found or produced empty sections.")
                await browser.close()
                sys.exit(1)

            print(f"Found {len(valid_sections)} valid sections")

            head_tag_search = re.search(r'(<head[^>]*>.*?</head>)', raw_html_text, flags=re.IGNORECASE | re.DOTALL)
            extracted_head = head_tag_search.group(1) if head_tag_search else ""

            reconstructed_html = f"<!DOCTYPE html><html>{extracted_head}<body {body_attributes} style='margin: 0; padding: 0;'>"

            for index, section in enumerate(valid_sections):
                page_break_css = "page-break-after: always;" if index < len(valid_sections) - 1 else ""

                reconstructed_html += f"""
                <div class="pdf-page-section" style="{page_break_css} width: 794px; height: 1122px; position: relative; overflow: hidden; box-sizing: border-box;">
                    <div class="section-content" style="transform-origin: top left; display: inline-block; width: 100%;">
                        <{wrapper_tag} {wrapper_attributes}>
                            {section}
                        </{wrapper_tag}>
                    </div>
                </div>
                """
            reconstructed_html += "</body></html>"

            await page.goto(html_file.resolve().as_uri(), wait_until="networkidle")
            await page.set_content(reconstructed_html, wait_until="networkidle")
            await page.add_style_tag(content=css_injection)
            await page.evaluate(layout_flattener_js)

            print("Applying scale-to-fit calculations...")
            await page.evaluate("""() => {
                const page_sections = document.querySelectorAll('.pdf-page-section');
                page_sections.forEach(section => {
                    const inner_content = section.querySelector('.section-content');
                    const a4_width = 794;
                    const a4_height = 1122;

                    const content_rectangle = inner_content.getBoundingClientRect();
                    const content_width = content_rectangle.width > 0 ? content_rectangle.width : 1;
                    const content_height = content_rectangle.height > 0 ? content_rectangle.height : 1;

                    const width_scale = a4_width / content_width;
                    const height_scale = a4_height / content_height;
                    const final_scale = Math.min(width_scale, height_scale);

                    inner_content.style.transform = `scale(${final_scale})`;
                });
            }""")

            print("Rendering pages...")
            await page.pdf(
                path=str(pdf_file),
                format="A4",
                print_background=True,
                margin={"top":"0", "bottom":"0", "left":"0", "right":"0"}
            )

        await browser.close()
        print(f"\nDone!\nOutput: {pdf_file}")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
