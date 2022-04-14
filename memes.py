
from email.mime import image
from PIL import Image, ImageDraw, ImageFont
from pytesseract import pytesseract
import os
  
# Defining paths to tesseract.exe
# and the image we would be using
# path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
path_to_tesseract = r"/usr/local/Cellar/tesseract/5.1.0/bin/tesseract"
image_path = r"/Users/devikachipalkatti/Documents/meme/test.png"
randomImage_path = r"/Users/devikachipalkatti/Documents/meme/gecko.png"


# Opening the image & storing it in an image object
img = Image.open(image_path)
randomImage = Image.open(randomImage_path)
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)


newMeme=  Image.new('RGB', (700, 700), color = (73, 109, 137))
newMeme.paste(randomImage, (100,50))

fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d = ImageDraw.Draw(newMeme)
d.text((10,10), text[:-1], font=fnt, fill=(255, 255, 0))
newMeme.save('pil_text_font.png')
# Displaying the extracted text
# print(text[:-1])
