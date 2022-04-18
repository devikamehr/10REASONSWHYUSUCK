
from email.mime import image
from PIL import Image, ImageDraw, ImageFont
from pytesseract import pytesseract
import os
import numpy as np
import random
import loader
from string import ascii_letters
import textwrap

list_of_text = loader.createPhrases()
  
# Defining paths to tesseract.exe
# and the image we would be using
# path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
for i in range(6):
    # path_to_tesseract = r"/usr/local/Cellar/tesseract/5.1.0/bin/tesseract"
    # image_path = r"/Users/devikachipalkatti/Documents/meme/text"
    randomImage_path = r"/Users/devikachipalkatti/Documents/meme/reactions"
    final_path =r"/Users/devikachipalkatti/Documents/meme/draft"

    random_filename = random.choice([
        x for x in os.listdir(randomImage_path)
        if os.path.isfile(os.path.join(randomImage_path, x))
    ])
    randomImage_path = r"/Users/devikachipalkatti/Documents/meme/reactions/" + random_filename

    random_text = random.choice(list_of_text)
    # random_text = random.choice([
    #     x for x in os.listdir(image_path)
    #     if os.path.isfile(os.path.join(image_path, x))
    # ])
    # image_path = r"/Users/devikachipalkatti/Documents/meme/text/" + random_text


    # Opening the image & storing it in an image object
    # img = Image.open(image_path)
    randomImage = Image.open(randomImage_path)
    # Providing the tesseract executable
    # location to pytesseract library
    # pytesseract.tesseract_cmd = path_to_tesseract
    
    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    # text = pytesseract.image_to_string(img)

    clr = tuple([np.random.choice(range(256)) for i in range(3)])
    # newMeme=  Image.new('RGB', (700, 700), color = clr)
    # (width, height) = (randomImage.width // 4, randomImage.height // 4)
    # randomImage = randomImage.resize((height, width))
    # newMeme.paste(randomImage, (50,200))

    # fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
    font = ImageFont.truetype(font='LuckiestGuy-Regular.ttf', size=30)
    avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
    max_char_count = int(randomImage.size[0] * .618 / avg_char_width)
    text = textwrap.fill(text=random_text, width=max_char_count)


    draw = ImageDraw.Draw(randomImage)
    # draw.text((randomImage.width//2,randomImage.height//2), text, font=font, fill=(0, 0, 0))
    draw.text(xy=(randomImage.size[0]/2, randomImage.size[1] / 2), text=text, font=font, fill='#000000', anchor='mm')


    filenum = str(random.randint(0,10000))
    randomImage.show()
    randomImage = randomImage.save(f"{final_path}/image" + filenum + ".png")

    # Displaying the extracted text
    # print(text[:-1])
