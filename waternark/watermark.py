from os import listdir
from PIL import Image
import random
import os

#list of watermarks dir
DIR = 'on'

#list of img (src) dir
img_list = listdir("src")
wat_list = listdir("on")

#print name of watermarks
for watname in wat_list:
    watname = "on/" + watname
    print (watname)

#work with image
for filename in img_list:
        filename = "src/" + filename
        print(filename)
        img = Image.open(filename)
        #resizing
        img = img.resize((1000,700))
        #choose random watermark from dir
        watermark = Image.open(os.path.join(DIR, random.choice(os.listdir(DIR))))
        #paste watermark on pic
        img.paste(watermark, (200, 200),  watermark)
        img.save(filename)
