import tkinter as t
from tkinter import ttk, Frame,messagebox
from PIL import *
from PIL import Image,ImageTk

width,height = 330,200
img_name = ["Input_p/","__init__.jpg"]
imgs = Image.open(img_name[0] + img_name[1])
imgs = imgs.resize((width,height))
img = ImageTk.PhotoImage(imgs)
