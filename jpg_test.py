#!/usr/bin/env python
# -*- coding:utf-8 -*-

#import Image
#import ImageFont

from PIL import Image

picPath = 'images/1212.jpg'

im = Image.open(picPath)
print im.getbbox()
