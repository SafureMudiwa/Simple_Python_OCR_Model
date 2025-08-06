import os
from PIL import Image
import pytesseract

#setting path for tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

file_name = input("ENTER IMAGE NAME HERE: ").strip()

def open_img_auto(file_name, folder=""):

    extensions = [".png", ".jpg", ".jpeg", ".gif", ".tiff"]
    for ext in extensions:
        path = os.path.join(folder, file_name + ext)
        if os.path.exists(path):
            return Image.open(path) #this line is Pillow opening the file.
        
    raise FileNotFoundError(f"{file_name} NOT FOUND IN {folder}")

img = open_img_auto(file_name, folder="images")
extracted_text = pytesseract.image_to_string(img)

output_file = "extracted_text.txt"
with open(output_file, "w") as file:
    file.write(extracted_text)

print("ETRACTED FILE SAVED TO: ", output_file)
print("\n-------ETRACTED TEXT---------\n")
print(extracted_text)