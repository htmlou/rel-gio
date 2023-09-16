from tkinter import *
from tkinter.ttk import *

from time import  strftime

root = Tk()
root.title("Relogio")

def time():
    string = strftime('%H:%M:%S ')
    label.config(text=string)
    label.after(1000, time)

