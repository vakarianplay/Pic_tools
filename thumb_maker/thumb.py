from PIL import Image
from os import listdir
from PIL import Image
import random
import os

#listing img dir
DIR = 'img'

img_list = listdir("img")

#select center and crop
def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:

    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

#create image
def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


for filename in img_list:
        outname = "out/" + filename
        filename = "img/" + filename
        print(filename)
        #open image
        im = Image.open(filename)
        #crop square
        im_new = crop_max_square(im)
        #resize to rhumbnale
        im_th = im_new.resize((128,128))
        #save with compress
        im_th.save(outname, quality=95)
