'''
Created on Feb 25, 2020

@author: luebbejo
'''
from image_functions import *
im = Image.open("SiriusAndViolet.jpg")
print(im.width, im.height, im.mode, im.format) #Displays info about the image

my_image = load_image("SiriusAndViolpet.jpg")
my_image.show(my_image)

