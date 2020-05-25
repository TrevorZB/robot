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

def find_absolute_center(rect):
    center = []
    center.append(((rect[0] + rect[0] + rect[2]) // 2) + GAME_X)
    center.append(((rect[1] + rect[1] + rect[3]) // 2) + GAME_Y)
    return center

def create_map(img):
    # image = cv.imread(img)
    # original = img.copy()

    # bg = np.uint8([[[255, 216, 204]]]) #here insert the bgr values which you want to convert to hsv
    # hsvBg = cv.cvtColor(bg, cv.COLOR_BGR2HSV)
    # print(hsvBg)

    # lowerLimit = hsvBg[0][0][0] - 10, 100, 100
    # upperLimit = hsvBg[0][0][0] + 10, 255, 255

    # print(upperLimit)
    # print(lowerLimit)



    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([123, 50, 50], dtype = "uint8")
    upper = np.array([103, 255, 255], dtype = "uint8")
    mask = cv.inRange(img, lower, upper)

    cnts = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    rects = []

    for c in cnts:
        x,y,w,h = cv.boundingRect(c)
        # cv.rectangle(original, (x, y), (x+w, y+h), (255, 0, 0))

    cv.imshow('mask', mask)
    # cv.imshow('original', original)
    cv.waitKey()
    return(rects)
