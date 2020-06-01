import screenshot
import rectangle
from ai import AI
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
    inventory = [[0]*AI.INV_WIDTH for i in range(AI.INV_HEIGHT)]
    inventory[3][11] = 1
    inventory[4][11] = 1
    inventory[0][0] = 1
    inventory[0][1] = 1
    player = AI(inventory)

    while True:
        time.sleep(2)
        img = screenshot.sc(GAME_X, GAME_Y, GAME_WIDTH, GAME_HEIGHT)
        rects = rectangle.create_rects(img)
        if rects:
            player.pick_up(rects[0])
            time.sleep(1)
            player.add_to_inv()

main()