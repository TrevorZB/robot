import pyautogui
from cv2 import cv2 as cv
import numpy as np

def sc(x, y, w, h):
    img = pyautogui.screenshot(region=(x, y, w, h))
    return cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)