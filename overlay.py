from tkinter import *
from random import *
import time

def create_canvas(x, y, w, h):
    canvas = Canvas(bg='white', height=h, width=w)
    # canvas.master.overrideredirect(True)
    canvas.master.geometry("+{0}+{1}".format(str(int(x) - 10), str(int(y) - 40)))
    # canvas.master.lift()
    canvas.master.wm_attributes("-topmost", True)
    # canvas.master.wm_attributes("-disabled", True)
    canvas.master.wm_attributes("-transparentcolor", "white")
    canvas.focus_set()
    canvas.update_idletasks()
    canvas.update()
    canvas.pack()
    return canvas

def update_canvas(canvas, rects):
    canvas.delete(ALL)
    for rect in rects:
        canvas.create_rectangle(rect[0], rect[1], rect[0] + rect[2], rect[1] + rect[3], outline='red', width=3)
    canvas.update_idletasks()
    canvas.update()
    canvas.pack()