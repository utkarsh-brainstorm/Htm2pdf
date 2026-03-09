# Htm2pdf 📄✨

Welcome to **Htm2pdf**! A powerful, elegant, and interactive CLI tool to convert your HTML files directly into beautiful, high-quality PDFs. 

## 🚀 Quick Start (No Setup Required!)

If you just want to use the tool **without** the hassle of setting up Python, installing libraries, or configuring heavy environments:

👉 **[Go to the Releases page](../../releases)** and download the standalone executable for your operating system. Simply download, run, and you are ready to convert!

---

## ✨ Features & How They Work

Htm2pdf provides an interactive Command Line Interface (CLI) that guides you through the conversion process. Once you run the tool, drop your HTML file into the terminal, and choose from the following amazing features:

### 1. 📜 Continuous Single-Page PDF Mode
Perfect for web pages, receipts, or long articles. It seamlessly flattens the entire HTML document into one very long, continuous PDF page. No awkward page cuts!

### 2. 🖨️ Standard A4 Paginated PDF Mode
Want a traditional, printable document? This mode smartly converts your web page into standard A4-sized pages. 

### 3. ✂️ Custom Page-Break Mode
Advanced user? You can provide a custom string marker. The tool will mathematically slice the HTML document exactly at those markers and render perfectly scaled, individual pages.

### 4. 🖤 Monochrome Print Mode
Save your colored ink! This optional mode precisely targets text, borders, and SVGs, turning them pure black while beautifully preserving the background colors.

### 🎮 How to Interact with the CLI
1. Run the program.
2. The CLI will ask: `Drop the HTML file here and press Enter:`. Simply drag and drop your `.html` or `.htm` file into the terminal.
3. Type the number corresponding to your desired PDF layout mode (`1`, `2`, or `3`) and press Enter.
4. Type `y` or `n` when asked to enable Monochrome mode.
5. Sit back and let Htm2pdf do the heavy lifting! The output PDF will be saved in the same folder as your original HTML.

---

## 🐍 For Developers: Running from Python Source

If you prefer to run the script directly via Python, follow these steps to set up the environment.

### 1. Requirements & OS Dependencies
Make sure you have **Python 3.8+** installed on your system. 
You will also need modern web rendering capabilities, which the `playwright` package handles.

### 2. Setup the Environment
Open your terminal and create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required Python dependency:
```bash
pip install playwright
```

**Crucial Step:** Install the Playwright Chromium browser binary (this is the engine that renders the HTML):
```bash
playwright install chromium
```

### 3. Run the Script
Now you can execute the Python script directly:
```bash
python htm2pdf.py
```

---

## 🔮 Future Roadmap

We are constantly improving! Keep an eye out—**after some time, we will be releasing official PyInstaller One-File executables for Windows and macOS!** 

This will mean true click-and-run support across all major platforms without needing the terminal or any installations. Directly download and use!
