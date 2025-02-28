import pytesseract
from PIL import Image
import argparse

# Specify the path to the Tesseract OCR executable file
pytesseract.pytesseract.tesseract_cmd = r'D:\\tools\\install_OCR\\tesseract.exe'

# Create a command-line argument parser
parser = argparse.ArgumentParser(description='Perform OCR on an image.')
parser.add_argument('image_path', type=str, help='Path to the image file.')

# Parse the command-line arguments
args = parser.parse_args()

try:
    # Open the image
    image = Image.open(args.image_path)

    # Perform OCR recognition
    text = pytesseract.image_to_string(image)

    print(text)
except FileNotFoundError:
    print(f"Error: The image file {args.image_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")