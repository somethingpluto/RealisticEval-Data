"""
this code was generated by ChatGPT (April 2023)

"""

from PIL import Image


def png_to_ico(png_filename, ico_filename):
    img = Image.open(png_filename)
    img.save(ico_filename, format='ICO', sizes=[(32, 32)])


png_to_ico('youtube.png', 'qtube.ico')