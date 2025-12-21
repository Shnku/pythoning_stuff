"""
   Inches = Pixels / PPI
   Pixels = Inches × PPI
   Inches = Centimeters / 2.54
   1 cm = 0.393701 inches
   1 inch = 25.4 mm
   Centimeters = Inches × 2.54
   Centimeters = (Pixels / PPI) × 2.54
   Pixels = (Centimeters / 2.54) × PPI

A4 paper size is 210 x 297 mm.

Width: 210 mm / 25.4 mm/inch ≈ 8.27 inches
Height: 297 mm / 25.4 mm/inch ≈ 11.69 inches
Width in pixels: 8.27 inches * 96 PPI ≈ 796 pixels
Height in pixels: 11.69 inches * 96 PPI ≈ 1120 pixels

Therefore, the A4 paper size in inches is approximately 8.27 x 11.69 inches, and in pixels (assuming 96 PPI) it
 would be approximately 796 x 1120 pixels.

"""


def mm_to_inches(mm):
    return mm / 25.4


def inches_to_pixels(inches, ppi=96):
    return int(inches * ppi)


def create_a4_canvas(ppi):
    # A4 paper size in mm
    width_mm = 210
    height_mm = 297
    # Convert mm to inches
    width_inches = mm_to_inches(width_mm)
    height_inches = mm_to_inches(height_mm)
    # Convert inches to pixels
    width_pixels = inches_to_pixels(width_inches, ppi)
    height_pixels = inches_to_pixels(height_inches, ppi)

    print("A4 paper size in inches:")
    print(f"Width: {width_inches:.2f} inches")
    print(f"Height: {height_inches:.2f} inches")

    print(f"\nA4 paper size in pixels ({ppi} PPI):")
    print(f"Width: {width_pixels} pixels")
    print(f"Height: {height_pixels} pixels")
    return (width_pixels, height_pixels)
