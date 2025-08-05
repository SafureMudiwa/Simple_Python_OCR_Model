from PIL import Image
import pytesseract

#setting path for tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = "sampleimg1.png"
img = Image.open(image_path) #opening image using Pillow
extracted_text = pytesseract.image_to_string(img)

output_file = "extracted_text.txt"
with open(output_file, "w") as file:
    file.write(extracted_text)

print("ETRACTED FILE SAVED TO: ", output_file)
print("\n-------ETRACTED TEXT---------\n")
print(extracted_text)