import pyautogui
from cv2 import cv2 as cv
import numpy as np

TEMPLATE_W = 120
TEMPLATE_H = 25
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
GAME_WIDTH = 1280
GAME_HEIGHT = 800
GAME_X = (SCREEN_WIDTH - GAME_WIDTH) / 2
GAME_Y = ((SCREEN_HEIGHT - GAME_HEIGHT) / 2) + 15  # extra 15px for top bar

def create_rects(img):
    # image = cv.imread(img)
    # original = image.copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([22, 93, 0], dtype="uint8")
    upper = np.array([45, 255, 255], dtype="uint8")
    mask = cv.inRange(img, lower, upper)

    cnts = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    rects = []

    for c in cnts:
        x,y,w,h = cv.boundingRect(c)
        if w > TEMPLATE_W and h > TEMPLATE_H:
            rects.append([x, y, w, h])

    # cv.imshow('mask', mask)
    # cv.imshow('original', original)
    # cv.waitKey()
    return(rects)

def calc_center_relative_rect(rect):
    center = []
    center.append(((rect[0] + rect[0] + rect[2]) // 2) + GAME_X)
    center.append(((rect[1] + rect[1] + rect[3]) // 2) + GAME_Y)
    return center

def calc_center_absolute_rect(rect):
    center = []
    center.append((rect[0] + rect[0] + rect[2]) // 2)
    center.append((rect[1] + rect[1] + rect[3]) // 2)
    return center
