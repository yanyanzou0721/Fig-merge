# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:34:40 2019

@author:Administrator
"""

from PIL import Image
import os

def rea(pdf_name):
    file_list = os.listdir('.')
    pic_name = []
    im_list = []
    for i in file_list:
    #    if "jpg" in i or "png" in i or "jpeg" in i :
        if "jpg" in i or "png" in i :
            pic_name.append(i)
    pic_name.sort()
    new_pic = []
    for x in pic_name:
        if "jpg" in x:
            new_pic.append(x)
    for x in pic_name:
        if "png" in x:
            new_pic.append(x)
    print("hec",new_pic)
    im1 = Image.open(new_pic[0])
    new_pic.pop(0)
    for i in new_pic:
        img = Image.open(i)
        if img.mode=="RGBA":
            img = img.convert("RGB")
            im_list.append(img)
        else:
            im_list.append(img)
    im1.save(pdf_name,"PDF",resolution=100.0,save_all=True,append_images=im_list)        
    print("output：",pdf_name)

if __name__=='__main__':
    print("start merge files")
    pdf_name=input("please cin the output file name:  ")
    if ".pdf" in pdf_name:
        rea(pdf_name=pdf_name)
    else:
        rea(pdf_name="{}.pdf".format(pdf_name))
