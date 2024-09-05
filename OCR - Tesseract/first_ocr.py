import pytesseract
import cv2

# Set the path to the Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Specify the path to your image
image_path = "education.png"

# Load the image
image = cv2.imread(image_path)
if image is None:
    print("Could not open or find the image.")
    exit()

# Convert the image to RGB (pytesseract expects an RGB image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)