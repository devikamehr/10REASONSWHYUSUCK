
from email.mime import image
from PIL import Image, ImageDraw, ImageFont
from pytesseract import pytesseract
import os
import numpy as np
import random
import loader
from string import ascii_letters
import textwrap

# Grab list of phrases from markov model
list_of_text = loader.createPhrases()
  

for i in range(20):
    # Grab paths
    randomImage_path = r"/Users/devikachipalkatti/Documents/meme/reactions"
    final_path =r"/Users/devikachipalkatti/Documents/meme/draft"

    # Pick a random backgorund file path.
    random_filename = random.choice([
        x for x in os.listdir(randomImage_path)
        if os.path.isfile(os.path.join(randomImage_path, x))
    ])
    randomImage_path = r"/Users/devikachipalkatti/Documents/meme/reactions/" + random_filename

    # Pick a random text and background together
    random_text = random.choice(list_of_text)

    randomImage = Image.open(randomImage_path)

    # Pick a random color and font
    clr = tuple([np.random.choice(range(256)) for i in range(3)])
    font = ImageFont.truetype(font='LEMONMILK-BoldItalic.otf', size=30)

    # Text wrapping crap
    avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
    max_char_count = int(randomImage.size[0] * .618 / avg_char_width)
    text = textwrap.fill(text=random_text, width=max_char_count)

    # Draw the text on half the image.
    draw = ImageDraw.Draw(randomImage)
    draw.text(xy=(randomImage.size[0]/2, randomImage.size[1] / 2), text=text, font=font, fill='#000000', anchor='mm')

    # Save the image
    filenum = str(random.randint(0,10000))
    randomImage = randomImage.save(f"{final_path}/image" + filenum + ".png")
