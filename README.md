-------- SIMPLE OCR (Image To Text) MODEL IN PYTHON --------
  
This is simple & straight-forward CLI Python based project that uses Tesseract OCR to extract text from images and written them to a .TXT file. 
Practical for converting images and extracting text from screenshots, images or handwritten notes into editabel text.

---- FEATURES ----
  1. Extract text from (PNG, JPEG, JPG, etc) images.
  2. Writes the extracted text to a .TXT file.
  3. Outputs the extracted text in the terminal.

---- HOW IT WORKS ----
  - Image is opened using Pillow(PIL)
  - Proceeds to send opened image to Tesseract OCR to detect text.
  - Detected text is then written to a .TXT file.
  - The same etext is displayed in the terminal.

---- PROJECT STRUCTURE ----
  Simple_OCR_Model\  
  |----main.py  #Main Script
  |----images\  #Exaple images file.
    |____sampleimg1.png
    |____UAE.png
    |____zimbabwe.png
  |----extracted_text.txt  Output file for extracted text.
    |____README.md  #Project Documentation
