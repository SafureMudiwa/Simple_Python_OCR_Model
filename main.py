from PIL import Image
import pytesseract

#when pytesseract does not find Tesseract installation automatically
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = "sampleimg1.png" #image file
img = Image.open(image_path)

extracted_text = pytesseract.image_to_string(img) #the text extract
print("Extracted Text: ")
print(extracted_text)

