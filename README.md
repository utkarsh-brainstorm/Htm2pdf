**🚨 NOTE: Generative AI is used in this project. Heisenberg only planned it and verified the functions, but the most code is written by AI. 🚨**

# Htm2pdf 📄✨

**Htm2pdf** is an incredibly powerful, interactive Command Line (CLI) tool designed to perfectly render HTML files into PDF documents. It completely bypasses the limitations of standard browser printing by utilizing the Chromium engine under the hood via Playwright, offering advanced features like continuous page rendering and custom string-based page splitting.

---

## 🚀 Quick Start (No Setup Required!)

If you do not want to install Python or set up developer environments, you can use the standalone executable:

1. Go to the **[Releases](../../releases)** page of this repository.
2. Download the `htm2pdf` executable file for your operating system (currently available for Linux).
3. If on Linux/macOS, open your terminal, navigate to your download folder, and make it executable: `chmod +x htm2pdf`
4. Run the file: `./htm2pdf`
5. Drag and drop your `.html` or `.htm` file into the terminal window when prompted and press Enter!

---

## ✨ Comprehensive Feature Guide

Htm2pdf offers three distinct rendering modes and a powerful monochromatic filter. When you run the script, it will interactively ask you which modes you want to use.

### 1. 📜 Continuous Single-Page PDF Mode (Option `1`)
*   **What it does:** Standard PDF converters break your web pages into multiple arbitrary pages, cutting through images and text. This mode prevents that entirely by evaluating the exact total height of the web page and generating a single, continuous, highly elongated PDF page.
*   **How it works:** It uses custom layout-flattening JavaScript to remove scrollbars, force `overflow: visible`, and adapt elements to their natural maximum height. The final PDF is strictly sized to `1080px` wide, dynamically extending downwards to fit the entire `scrollHeight` of the document.
*   **Best for:** Saving web articles, long receipts, dashboards, or any webpage where a page-break ruins the flow.

### 2. 🖨️ Standard A4 Paginated PDF Mode (Option `2`)
*   **What it does:** Triggers a high-fidelity standard print of the HTML document.
*   **How it works:** Reformats the viewport and natively utilizes Chromium's background-printing capabilities to slice the document logically into standard A4-sized pages.
*   **Best for:** Documents you actually intend to print on physical paper.

### 3. ✂️ Custom Page-Break Mode (Option `3`)
*   **What it does:** This is an advanced feature that allows you to define exactly where a page should split based on a specific text string present in your HTML.
*   **How it works:** 
    1. It asks you for a "custom page break marker string". 
    2. The tool reads your raw HTML and splits the document exactly at those string markers.
    3. It reconstructs a brand-new internal HTML layout where every split section is forcefully placed into an A4 dimension wrapper (`794px` x `1122px`) with a CSS `page-break-after: always;` property.
    4. **Smart Scaling:** If the content inside any of these newly cut sections is larger than an A4 page, the internal engine mathematically calculates the ratio and applies a CSS `transform: scale()` perfectly fitting your content into the boundaries of the A4 page before rendering the PDF.
*   **Best for:** HTML reports generated from data where you want specific sections to guarantee a fresh page, regardless of their height.

### 🖤 Monochrome Print Mode (Post-Processing Filter)
*   **What it does:** After selecting your layout mode, the tool asks if you want to enable Monochrome Print Mode. This forces your text and borders to be pure black but keeps the background colors completely intact.
*   **How it works:** It dynamically injects aggressive CSS overrides (`color: #000000 !important`, `border-color: #000000 !important`, `stroke: #000000 !important`) targeting typography, horizontal rules (`<hr>`), and SVGs. Simultaneously, a JavaScript flattener hunts for the primary background color of the HTML body or its main wrapper and enforces standard background rendering. 
*   **Best for:** Saving colored ink when printing colored articles, ensuring high contrast for text reading.

---

## 🐍 For Developers: Running from Python Source

If you prefer to run the code manually or modify it, follow these steps:

### 1. Requirements
*   **Python 3.8+** installed on your system.

### 2. Setup the Environment
Open your terminal in the project folder and run:
```bash
# Optional but recommended: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install the required Python wrapper for the browser engine
pip install playwright

# Download the actual Chromium browser binaries required for rendering
playwright install chromium
```

### 3. Run the Script
```bash
python htm2pdf.py
```

---

## 🔮 Future Updates
We are actively working on pushing PyInstaller one-file executable releases for **Windows** and **macOS** as well! This ensures full click-and-run support universally without touching a terminal.
