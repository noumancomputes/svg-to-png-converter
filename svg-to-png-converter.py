# Using cairosvg for high-quality conversion
from cairosvg import svg2png
import os

# Define file paths
input_svg = os.path.join("images", "input_image_name.svg")
output_png = os.path.join("images", "output_image_name.png")

# Ensure output directory exists
os.makedirs("images", exist_ok=True)

# Check if input SVG exists
if not os.path.exists(input_svg):
    print(f"Error: SVG file '{input_svg}' not found. Please check the file path.")
else:
    try:
        # Convert SVG to PNG with high resolution
        svg2png(url=input_svg, 
                write_to=output_png,
                output_width=1000, 
                output_height=1000,
                dpi=300)  # Higher DPI for print quality

        print(f"Conversion successful! PNG saved at '{output_png}'")

    except Exception as e:
        print(f"Error during conversion: {e}")
