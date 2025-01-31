from img2table.document import Image
import pytesseract
from PIL import Image as PILImage

# Load the image
image_path = "tableImage.jpg"
img = Image(src=image_path)

# Extract text from the image using OCR
text = pytesseract.image_to_string(PILImage.open(image_path), lang="eng")

# Print the extracted text in English
print("Extracted Text:\n", text)
