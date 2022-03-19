# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import numpy as np
import sys
from colorama import Fore
def bright(a,b,c,d):
   x=0
   if (d=="avg"):                       #average brightness
        x=(a+b+c)/3
   elif(d=="lum"):
        x=(0.21*a + 0.72*b + 0.07*c)    #Luminosity
   else:                                #min max rgb brightness
       x=max(a, b, c) + min(a, b, c) / 2
   return x
def print_ascii_matrix(ascii_matrix, text_color):
    for row in ascii_matrix:
        line = [p+p+p for p in row]
        print(text_color + "".join(line))
def resize(a,b,image):
    imageresize=a,b
    image.thumbnail(imageresize, Image.ANTIALIAS)        
def print_txt(array):
    sys.stdout = open("test9.txt", "w")          
    print_ascii_matrix(array,Fore.GREEN)               

    sys.stdout.close()
im = Image.open("C:\\Users\\mvako\\Desktop\\projects\\ascii]\\peng.jpg")
#size=resize(200,200,im)

w, h = im.size
s='$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~i!lI;:,"\^`'
print(im.size)                  #check size values after resize
image_rgb = im.convert("RGB")
pixel_array = np.empty((w, h), dtype=object)
bright_array=np.empty((w,h),dtype=int)
pointer_array=np.empty((w,h),dtype=int)
final_array=np.empty((w,h),dtype=object)
flip_array=np.empty((h,w),dtype=object)

for x in range(w):
    for y in range(h):
        pixel_array[x][y] = image_rgb.getpixel((x,y))           #rgb values at the current pixel
        bright_array[x][y]=bright(pixel_array[x][y][0],pixel_array[x][y][1],pixel_array[x][y][2],"lum")   #convert rgb values to single brightness value
        pointer_array[x][y]=bright_array[x][y]/3.657142857142857        #scale pointer 
        if (pointer_array[x][y]>64):
            final_array[x][y]='$'
        else:            
            final_array[x][y]=s[pointer_array[x][y]]
for x in range(w):              #flipping the pic
    for y in range(h):
        flip_array[y][x]=final_array[x][y]            
print_txt(flip_array)    #printing the matrix in txt file

#print_ascii_matrix(flip_array,Fore.GREEN)               

