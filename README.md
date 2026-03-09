**🚨 NOTE: Generative AI is used in this project. Heisenberg only planned it and verified the functions, but the most code is written by AI. 🚨**

# Htm2pdf

Htm2pdf is a simple tool to convert your HTML files into PDF documents.

## Quick Start

To use this tool without setting up Python:
1. Go to the [Releases](../../releases) page.
2. Download the `htm2pdf` Linux executable file.
3. Open your terminal, make it executable (`chmod +x htm2pdf`), and run it (`./htm2pdf`).

## Features & Instructions

When you run the tool, simply drag and drop your HTML file into the window and press Enter. Then, follow the simple questions it asks you:

* **Continuous Single-Page PDF (Type `1`)**
  Makes one very long PDF page. Good for saving long web articles without annoying page cuts.
* **Standard A4 Pages (Type `2`)**
  Splits the PDF into normal printable A4 pages, just like a standard printer.
* **Custom Split (Type `3`)**
  You type a specific text marker. The tool will cut the document and start a new PDF page every time it sees that exact text.
* **Monochrome Print Mode**
  It will ask if you want to turn text and borders black while keeping background colors. Type `y` for yes or `n` for no.

## Running from Source (For Developers)

If you want to run the code yourself using Python:

1. Make sure Python 3.8+ is installed.
2. Open your terminal in the project folder.
3. (Optional) Create a virtual environment: `python -m venv venv` and activate it.
4. Install requirements: `pip install playwright`
5. Install the browser engine: `playwright install chromium`
6. Run the tool: `python htm2pdf.py`

## Future Updates

We will soon release ready-to-use executable files for Windows and macOS, so you can just double-click and use it without any terminal.
