'''
Created on Feb 25, 2020

@author: luebbejo
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
#import requests
from io import BytesIO
from Tools.scripts.parseentities import outfile


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
        print("load_image(): Unable to load" + filename)
        return None # None is a keyword that represents a null pointer
    
    
    
def save_image( imageObject, outfilename ) :
    """
    Save an image to disk
    :param imageObject: The Image to save
    :param outfilename: The target file
    """
    try:
        imageObject.save( outfilename )
    except:
        print("save_image(): Unable to save" + outfilename)
        
        
def crop_image(imageObject, cropRegion): 
        im_c = imageObject.crop(cropRegion) # (left, top, right, bottom) it's a tuple!
        return im_c

        
        