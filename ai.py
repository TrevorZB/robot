import time
import pyautogui
import rectangle
import random
import win32clipboard

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class AI:
    INV_HEIGHT = 5
    INV_WIDTH = 12
    INV_CELL_WIDTH = 39
    INV_CELL_HEIGHT = 39
    INV_TOP_LEFT_X = 1120
    INV_TOP_LEFT_Y = 590

    def __init__(self, inventory):
        self.inventory = inventory

    def cell_to_rect(self, cell):
        # cell[0] = row ,, cell[1] = col
        rect = []
        rect.append(self.INV_TOP_LEFT_X + self.INV_CELL_WIDTH * cell[1])
        rect.append(self.INV_TOP_LEFT_Y + self.INV_CELL_HEIGHT * cell[0])
        rect.append(self.INV_CELL_WIDTH)
        rect.append(self.INV_CELL_HEIGHT)
        return rect

    def pick_up(self, rect):
        center = rectangle.calc_center_relative_rect(rect)
        pyautogui.moveTo(center[0], center[1], 0.2)
        time.sleep(0.2)
        pyautogui.doubleClick()

    # 1135px x, 610px y, 40px width and height
    def add_to_inv(self):
        pyautogui.press('i')
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText('test')
        win32clipboard.CloseClipboard()
        for i, row in enumerate(self.inventory):
            for j, cell in enumerate(row):
                if not cell:
                    rect = self.cell_to_rect([i, j])
                    center = rectangle.calc_center_absolute_rect(rect)
                    pyautogui.moveTo(center[0], center[1], 0.2)
                    time.sleep(0.5)

                    # todo : ctrl + c on cell
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('c')
                    pyautogui.keyUp('ctrl')
                    # todo : check if clipboard is empty
                    win32clipboard.OpenClipboard()
                    data = win32clipboard.GetClipboardData()
                    win32clipboard.CloseClipboard()

                    print(data)
                    
                    if data != 'test':
                        # parse clipboard for words to tell what kind of item it is
                        # todo : add 1s to the array
                        print('added to inventory')
                        return

        pyautogui.press('i')