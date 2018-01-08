#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:00:20 2018

@author: scrojasn
"""

from PIL import Image
from pylab import *
import os

mediaFolder = 'media'
qtyFiles = len(os.listdir(mediaFolder))

# Calculate the average width and height to make all the flags the same size
avgWidth = 0
avgHeight = 0
for filename in os.listdir(mediaFolder):
    img = Image.open(mediaFolder + '/' + filename)
    print(filename)
    print(img.size)
    
    if avgWidth == 0:
        avgWidth = img.size[0] / qtyFiles
    else:
        avgWidth += img.size[0] / qtyFiles
        
    if avgHeight == 0:
        avgHeight = img.size[1] / qtyFiles
    else:
        avgHeight += img.size[1] / qtyFiles

avgWidth = int(avgWidth)
avgHeight = int(avgHeight)
print(avgWidth)
print(avgHeight)

# Substractive Mixing of Images
for filename in os.listdir(mediaFolder):
    img = Image.open(mediaFolder + '/' + filename)
    print(filename)
    img = img.resize((avgWidth,avgHeight), Image.ANTIALIAS)
    if 'sumImgs' in vars():
        sumImgs += float64(array(img)) / qtyFiles
    else:
        sumImgs = float64(array(img)) / qtyFiles
        
finalImg = uint8(sumImgs)
#print(finalImg)
imshow(finalImg)
