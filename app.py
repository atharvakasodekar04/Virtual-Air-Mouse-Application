import sys
import os
from tkinter import *
import tkinter.font as font
top=Tk()
top.geometry("1280x856")
# set minimum window size value
top.minsize(1280, 856)
bg = PhotoImage(file = "bg.png")
label1 = Label(top, image = bg)
label1.place(x = 0,y = 0)
# set maximum window size value
top.maxsize(1280, 856)
logo=PhotoImage(file="logo.png")
top.iconphoto(False, logo)
top.title('Motion Tracker')
myFont = font.Font(size=15,weight="bold",family='Helvetica')
border = LabelFrame(top, bd = 10, bg = "#6ffeff")
border.place(x=583, y=445)
def run():
    os.system('python -i main.py')
btn = Button(border, text="Track", width = 8,command=run,bg = "#4951ce", fg = "black")
btn['font']=myFont
btn.pack()
top.mainloop()

