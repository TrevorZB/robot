import screenshot
import rectangle
import ai
import time
from cv2 import cv2 as cv
import numpy as np
import pyautogui
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
GAME_WIDTH = 1280
GAME_HEIGHT = 800
GAME_X = (SCREEN_WIDTH - GAME_WIDTH) / 2
GAME_Y = ((SCREEN_HEIGHT - GAME_HEIGHT) / 2) + 15  # extra 15px for top bar

def main():
    while True:
        time.sleep(2)
        img = screenshot.sc(GAME_X, GAME_Y, GAME_WIDTH, GAME_HEIGHT)
        # rectangle.create_map(img)
        rects = rectangle.create_rects(img)
        if rects:
            ai.pick_up(rects[0])

main()