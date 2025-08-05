from PIL import Image
import pytesseract

image_path = r"C:\Users\Emmanuel Safure M\Documents\My Python\Simple_OCR_Model" #image location
img = Image.open(image_path)

extracted_text = pytesseract.image_to_string(img) #the text extract

print("Extracted Text: ")
print(extracted_text)

