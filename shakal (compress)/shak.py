from os import listdir
from PIL import Image

#list src pic
DIR = 'pic'

#print listing of images
img_list = listdir("pic")

#enter and calculate ratio
sh_ent = int(input("Shakal ratio (compress ratio):"))
sh = 100 - sh_ent

#work with image
for filename in img_list:
        outname = "out/" + filename
        filename = "pic/" + filename
        print(filename)
        img = Image.open(filename)
        #save with compress
        img.save(outname, "JPEG", quality=sh)
