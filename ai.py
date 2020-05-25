import time
import pyautogui
import rectangle
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

def pick_up(rect):
    center = rectangle.find_absolute_center(rect)
    pyautogui.moveTo(center[0], center[1], 0.2)
    time.sleep(0.2)
    pyautogui.doubleClick()