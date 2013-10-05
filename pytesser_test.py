# Plan: 
# Take image -> rectify orientation -> ocr -> spell correction -> get text -> put into google calendar

from pytesser import *

im = Image.open('images/fb-cover.png')
text = image_to_string(im)
print text