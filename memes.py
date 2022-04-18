
from email.mime import image
from PIL import Image, ImageDraw, ImageFont
from pytesseract import pytesseract
import os
import numpy as np
import random

  
# Defining paths to tesseract.exe
# and the image we would be using
# path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
for i in range(30):
    path_to_tesseract = r"/usr/local/Cellar/tesseract/5.1.0/bin/tesseract"
    image_path = r"/Users/devikachipalkatti/Documents/meme/text"
    randomImage_path = r"/Users/devikachipalkatti/Documents/meme/reactions"
    final_path =r"/Users/devikachipalkatti/Documents/meme/draft"

    random_filename = random.choice([
        x for x in os.listdir(randomImage_path)
        if os.path.isfile(os.path.join(randomImage_path, x))
    ])
    randomImage_path = r"/Users/devikachipalkatti/Documents/meme/reactions/" + random_filename

    random_text = random.choice([
        x for x in os.listdir(image_path)
        if os.path.isfile(os.path.join(image_path, x))
    ])
    image_path = r"/Users/devikachipalkatti/Documents/meme/text/" + random_text


    # Opening the image & storing it in an image object
    img = Image.open(image_path)
    randomImage = Image.open(randomImage_path)
    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract
    
    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)

    clr = tuple([np.random.choice(range(256)) for i in range(3)])
    newMeme=  Image.new('RGB', (700, 700), color = clr)
    (width, height) = (randomImage.width // 4, randomImage.height // 4)
    randomImage = randomImage.resize((height, width))
    newMeme.paste(randomImage, (50,200))

    # fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
    fnt = ImageFont.truetype(font='LuckiestGuy-Regular.ttf', size=35)

    d = ImageDraw.Draw(newMeme)
    d.text((100,100), text[:-1], font=fnt, fill=(255, 255, 0))
    filenum = str(random.randint(0,10000))
    newMeme = newMeme.save(f"{final_path}/image" + filenum + ".png")

    # Displaying the extracted text
    # print(text[:-1])
