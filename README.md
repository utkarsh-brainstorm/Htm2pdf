**🚨 NOTE: Generative AI is used in this project. Heisenberg only planned it and verified the functions, but the most code is written by AI. 🚨**

# Htm2pdf

Htm2pdf is a simple tool to convert your HTML files into PDF documents.

## Quick Start

To use this tool without setting up Python:
1. Go to the [Releases](../../releases) page.
2. Download the version for your computer.
3. Run the downloaded file.

## Features & Instructions

When you run the tool, simply drag and drop your HTML file into the window and press Enter. Then, choose one of these options:

* **Option 1: Single Continuous Page**
  Makes one very long PDF page. Good for saving web articles without page cuts.
* **Option 2: Standard A4 Pages**
  Splits the PDF into normal printable A4 pages.
* **Option 3: Custom Split**
  Type a specific text marker. The tool will start a new PDF page every time it sees that text.
* **Monochrome Mode**
  It will ask if you want black text and borders while keeping the background color. Type `y` for yes or `n` for no.

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
