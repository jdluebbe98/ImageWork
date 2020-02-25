'''
Created on Feb 25, 2020

@author: luebbejo
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
#import requests
from io import BytesIO


"""
    Load an image file from disk
    :param filename: The file to load
    :return the image object
"""


def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        print("Unable to find image")
        return None # None is a keyword that represents a null pointer