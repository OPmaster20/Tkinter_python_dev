import importlib

import cv2 as cv
import sys
import numpy as np
import tkinter as t
from tkinter import ttk, Frame,messagebox
from PIL import *
from PIL import Image,ImageTk
import time
import matplotlib as m
import matplotlib.pyplot as plt
import re

window=t.Tk()
window.title("📚Img operator (edition 0.1)")
window.geometry('390x450')
window.configure(background='pink')


img_format = ['png','jpg','bmp']

pos = t.Frame
hist = t.Frame
index = '0'
var_1 = 0
var_2 = t.DoubleVar()
var_3 = t.IntVar()
def mainframe():
    global pos,hist,var_1,var_2,selects
    frame = t.Frame(width=330, height=200, bg='#F8F8FF')
    frame.place(x=32, y=30)
    pos = frame

    entry = t.Entry(window,width=18,cursor='plus')
    entry.place(x=200, y=273)

    button = t.Button(window, text='Exit', command=lambda: window.destroy(), width=4, height=1)
    button.place(x=30, y=300, anchor='sw')


    button = t.Button(window, text='Show', command=lambda: upload(entry), width=6, height=1)
    button.place(x=320, y=273)

    button2 = t.Button(window, text='Sharpen', command=lambda: sharpen(selects), width=6, height=1)
    button2.place(x=80, y=273)

    button2 = t.Button(window, text='Trans', command=lambda: trans(), width=6, height=1)
    button2.place(x=140, y=273)

    button2 = t.Button(window, text='Edge', command=lambda: Edge(selects), width=6, height=1)
    button2.place(x=80, y=240)


def trans():
    import img as p
    global cont, index,var_1,var_2,var_3

    if cont == 0:
        halt()
    else:
        parameter1 = float(var_2.get())
        parameter2 = int(var_3.get())
        img = cv.imread(p.img_name[0] + p.img_name[1])
        rows,cols = img.shape[:2]
        mapx = np.zeros(img.shape[:2],np.float32)
        mapy = np.zeros(img.shape[:2],np.float32)
        for i in range(rows):
            for j in range(cols):
                mapx.itemset((i,j),cols -j - parameter2)
                mapy.itemset((i,j),i)
        img = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
        img_g = cv.GaussianBlur(img, (0, 0), parameter2)
        imges = cv.addWeighted(img, parameter1, img_g, -0.5, 0)
        if var_1 == 1:
            imges = cv.cvtColor(imges, cv.COLOR_BGR2GRAY)
            #imges = cv.equalizeHist(imges)
            strong = cv.createCLAHE(clipLimit=parameter1, tileGridSize=(parameter2, parameter2))
            contrast = strong.apply(imges)
            cv.imshow("img", contrast)
            cv.imwrite("output_p/Output" + index + ".jpg", contrast)
        else:
            cv.imshow("img",imges)
            cv.imwrite("output_p/Output" + index + ".jpg", imges)
    ...
def Edge(self):
    import img as p
    global cont, index, var_1, var_2,var_3
    if cont == 0:
        halt()
    else:
        parameter1 = float(var_2.get())
        parameter2 = int(var_3.get())
        img = cv.imread(p.img_name[0] + p.img_name[1],cv.IMREAD_GRAYSCALE)
        if img is None:
            t.messagebox.showinfo(title='Warn', message='Error!')
        else:
            if str(self.get()) == 'Gauss':
                img_g = cv.GaussianBlur(img,(0,0),parameter2)
            elif str(self.get()) == 'Median':
                if parameter2 % 2 != 1:
                    parameter2 = parameter2 - 1
                img_g = cv.medianBlur(img, (parameter2))
            else:
                img_g = cv.blur(img,(parameter2,parameter2))
            if var_1 == 1:
                imges = cv.addWeighted(img, parameter1, img_g, -0.5, 0)
                #imges = cv.cvtColor(imges,cv.COLOR_BGR2GRAY)
                #imges = cv.equalizeHist(imges)
                strong = cv.createCLAHE(clipLimit=parameter1,tileGridSize=(parameter2,parameter2))
                contrast = strong.apply(imges)
                th1 = cv.adaptiveThreshold(contrast,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,int(parameter1))
            else:
                th1 = cv.adaptiveThreshold(img_g, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11,int(parameter1))
            #th1 = cv.adaptiveThreshold(contrast, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11,int(parameter1))
            cv.imshow("img",th1)
            cv.imwrite("output_p/Output" + index + ".jpg", th1)

        ...
    ...
def sharpen(self):
    import img as p
    global cont,index,var_1,var_2,var_3
    if cont == 0:
        halt()
    else:
        parameter1 = float(var_2.get())
        parameter2 = int(var_3.get())
        #imgs = str(p.img_name[1])
        img = cv.imread(p.img_name[0] + p.img_name[1])
        if img is None:
            t.messagebox.showinfo(title='Warn', message='Error!')
        else:
            if str(self.get()) == 'Gauss':
                img_g = cv.GaussianBlur(img,(0,0),parameter2)
            elif str(self.get()) == 'Median':
                if parameter2 % 2 != 1:
                    parameter2 = parameter2 - 1
                img_g = cv.medianBlur(img, (parameter2))
            else:
                img_g = cv.blur(img,(parameter2,parameter2))
            imges = cv.addWeighted(img,parameter1,img_g,-0.5,0)
            # ////////////////////////////////////////////////////////
            if var_1 == 1:
                imges = cv.cvtColor(imges,cv.COLOR_BGR2GRAY)
                #imges = cv.equalizeHist(imges)
                strong = cv.createCLAHE(clipLimit=parameter1,tileGridSize=(parameter2,parameter2))
                contrast = strong.apply(imges)
            # //////////////////////////////////////////////////////
                cv.imwrite("output_p/Output" + index + ".jpg", contrast)
            #contrast = cv.merge((b,g,r))
                cv.imshow("img",contrast)
            else:
                cv.imwrite("output_p/Output" + index + ".jpg", imges)
                cv.imshow("img",imges)
            index = str(int(index) + 1)

            k = cv.waitKey(0)
            if k == ord('q'):
                cv.destroyAllWindows()
            #button2 = t.Button(window, text='Save', command=lambda: , width=6, height=1)
            #button2.place(x=140, y=273)
    print(var_1)
    ...

def halt(code = 1,filename = ""):
    if code == 1:
        t.messagebox.showinfo(title='Error',message='No input image_name !')
    elif code == 2:
        t.messagebox.showinfo(title='Warn', message='Image_name must be full, include the format of image !')
    elif code == 3:
        t.messagebox.showinfo(title='Error', message='Something went wrong. Please check the image you entered')
    elif code == 4:
        t.messagebox.showinfo(title='Error', message='No such file or directory: "Input_p/"' + filename)
def main():
    mainframe()
    ...


cont = 0
def check(var = 1):
    global var_1
    if var == 0:
        var_1 = 1
    else:
        var_1 = 0
    print(f"{var_1} in check")
    ...

selects = ttk.Combobox
def upload(self):
    global cont,var_1,selects
    import img as p
    if len(str(self.get())) <= 0:
        halt(1)
    print(str(self.get()))
    if re.search('^.+\\.(jpg|png)$', str(self.get())):
        p.img_name[1] = str(self.get())
        #importlib.reload(p)
        if p.img is None:
            halt(3)
        try:
            p.imgs = Image.open(p.img_name[0] + p.img_name[1])
            p.imgs = p.imgs.resize((p.width, p.height))
            p.img = ImageTk.PhotoImage(p.imgs)
            #print(p.img)
            shows = t.Label(pos,image=p.img)
            shows.pack()
            button2 = t.Button(window, text='Del', command=lambda: shows.destroy(), width=6, height=1)
            button2.place(x=320, y=310)
            ranges = t.Scale(window, length=50, background='pink',variable=var_2,label="Parameter1",from_=1.0,to=9.0,resolution=0.5)
            ranges.place(x=30, y=350)
            ranges = t.Scale(window, length=50, background='pink', variable=var_3, label="Parameter2", from_=1,to=9, resolution=1)
            ranges.place(x=160, y=350)
            w = t.Checkbutton(window, text="Sharpen_Plus", variable = var_1,command = lambda: check(var_1) ,onvalue=1, offvalue=0, height=1,width=15, background='pink')
            w.place(x=10, y=310)
            w.deselect()

            select = ttk.Combobox(window, width=6, textvariable=t.IntVar(), state='readonly')
            lis = ["Gauss","Median","Blur"]
            select['values'] = lis
            select.place(x=140, y=310)
            selects = select


            #text = t.Label(window,text="Regulating parameter")
            cont = cont + 1
        except:
            halt(4,p.img_name[1])
    else:
        halt(2)
    ...
if __name__ == '__main__':
    main()

window.mainloop()
'''
img = cv.imread(imgs,0)
img = img.astype("float")
            row,column = img.shape
            grad = np.zeros((row,column))
            for x in range(row - 1):
                for y in range(column - 1):
                    gx = abs(img[x+1,y]-img[x,y])
                    gy = abs(img[x,y+1]-img[x,y])
                    grad[x,y] = gx + gy
            sharp = img + grad
            sharp = np.where(sharp < 0,0,np.where(sharp > 255,255,sharp))
            sharp = sharp.astype("uint8")
            cv.imshow("img", sharp)

# Sharpening algorithm 1 （selectable）
'''