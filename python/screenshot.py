from os import name
import time
from tkinter.constants import COMMAND, NW
import pyautogui as py
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image



def screenshot():
    name = int(round(time.time()*10))
    name = 'G:/python/screenshotdata/{}.png'.format(name)
    time.sleep(5)
    img = py.screenshot(name)
    #img.show()
 

screen = tk.Tk() 
screen.title("screen snap")

frame = tk.Frame(
    screen,
    

)
frame.pack()

button = tk.Button(
    frame,
    text = "Take a screenhot",
    command = screenshot)

button.pack(side = tk.LEFT)
close = tk.Button(
    frame,
    text = "Quit",
    command = quit)
close.pack(side = tk.RIGHT)


canvas = tk.Canvas(
    frame,
    width=500,
    height=250)
canvas.pack()

img1 = ImageTk.PhotoImage(Image,open(name))
canvas.create_image(135, 20, anchor = NW,
				image = img1)






screen.mainloop()