
from email.mime import image
from PIL import Image, ImageDraw, ImageFont, ImageSequence, ImageChops
from pytesseract import pytesseract
import os
import numpy as np
import random
import loader
from string import ascii_letters
import textwrap

# Grab list of phrases from markov model
list_of_text = ["The ABCS of this current political movement", "Unpack white feminism", "Let's talk about cancel culture", "What is degrowth", "Apps to keep you conscious",
"Ways to donate", "110 ways to practice being anti-racist if you can't spend money or leave the house", "how to refresh from political overload", "why consumerism culture is racist",
"how to be antiracist", "Let's talk about transphobia", "Why you should stop using Amazon", "so you want to talk about mail-in voting", "being an anti-racist ally", "what is performative activism"]
# for i in range(10):
#     temp = loader.createPhrases()
#     list_of_text += temp


for i in range(15):
    # Grab paths
    randomImage_path = r"/Users/devikachipalkatti/Documents/meme/reactions"
    final_path =r"/Users/devikachipalkatti/Documents/meme/draft"
    animated_path = r"/Users/devikachipalkatti/Documents/meme/sparkles"
    # Pick a random backgorund file path.
    random_filename = random.choice([
        x for x in os.listdir(randomImage_path)
        if os.path.isfile(os.path.join(randomImage_path, x))
    ])
    randomImage_path = r"/Users/devikachipalkatti/Documents/meme/reactions/" + random_filename

    animated_gif = random.choice([
        x for x in os.listdir(animated_path)
        if os.path.isfile(os.path.join(animated_path, x))
    ])
    animated_path = r"/Users/devikachipalkatti/Documents/meme/sparkles/" + animated_gif

    # Pick a random text and background together
    random_text = random.choice(list_of_text)
    randomImage = Image.open(randomImage_path)
    animated_gif = Image.open('sparkles/original.gif')
    animated_gif = Image.open(animated_path)
    print(randomImage_path)
    width = int(randomImage.size[0])
    height = int(randomImage.size[1])
    # ImageChops.offset(animated_gif, width//2, -1 *(height//2))

    # animated_gif = animated_gif.resize((randomImage.size[0], randomImage.size[1]))
    # animated_gif.show()

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

    filenum = str(random.randint(0,10000))
 
    # gif shit
    all_frames = []
    for gif_frame in ImageSequence.Iterator(animated_gif):
        new_frame = randomImage.copy()
        gif_frame = gif_frame.convert('RGBA')
        gif_frame = gif_frame.resize((width, height))
        new_frame.paste(gif_frame, (width//6 - 40, height//6),mask=gif_frame)
        all_frames.append(new_frame)
        # ImageChops.offset(new_frame, width//2,height//2 )

    all_frames[0].save(f"{final_path}/image" + filenum + ".gif", save_all=True, append_images=all_frames[1:], duration=50, loop=0)
    # Save the image

