# svg-to-png-converter

A lightweight and efficient Python script for converting SVG files to PNG with high resolution using the CairoSVG library. Ideal for graphic designers, developers, and automation tasks.

## 🚀 Features
- Converts **SVG to PNG** with high resolution  
- Supports **custom output dimensions (width & height)**  
- Ensures **300 DPI quality for printing**  
- Automatically **creates output directories** if missing  
- Handles **file existence checks** and errors gracefully  

## 🛠 Installation & Setup

### 1⃣ Install Python (if not already installed)
Ensure you have Python 3.6+ installed. Check with:
```bash
python --version
```

### 2⃣ Install Required Dependencies
Run the following command to install necessary libraries:
```bash
pip install cairosvg
```

If you also need **PNG to SVG** conversion, install:
```bash
pip install png2svg
```

### 3⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/svg-to-png-converter.git
cd svg-to-png-converter
```

### 4⃣ Run the Script
Place your SVG file in the `images/` folder and update the script with the correct file name. Then, run:
```bash
python svg_to_png_converter.py
```

## 🖼️ Usage Example
1. Place an **SVG file** (`input_image.svg`) in the `images/` directory.  
2. Update the script with your input/output file names.  
3. Run the script to get a **high-quality PNG output**.  

## ⚙️ Converting PNG to SVG (Optional)
If you want to convert **PNG back to SVG**, use `png2svg`:
```python
from png2svg import png2svg

png2svg("images/input.png", "images/output.svg")
```

## 📝 License
This project is licensed under the **MIT License**. Feel free to use and modify it.

---