import time
import pyautogui
import rectangle
import random
import win32clipboard

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class Stash:
    pass

class AI:
    INV_HEIGHT = 5
    INV_WIDTH = 12
    INV_CELL_WIDTH = 39
    INV_CELL_HEIGHT = 39
    INV_TOP_LEFT_X = 1120
    INV_TOP_LEFT_Y = 590

    weapon_keywords = ['Sword', 'Staff', 'Warstaff']
    helm_keywords = ['Circlet', 'Helm', 'Helmet', 'Bascinet', 'Burgonet', 'Mask', 'Pelt']
    body_keywords = ['Robe', 'Armour', 'Jacket', 'Plate', 'Leather', 'Doublet', 'Hauberk', 'Garb', 'Brigandine']
    belt_keywords = ['Belt', 'Sash', 'Stygian']
    gloves_keywords = ['Gloves', 'Gauntlets']
    boots_keywords = ['Boots', 'Greaves', 'Slippers']
    ring_keywords = ['Ring']
    amulet_keywords = ['Amulet']

    def __init__(self, inventory):
        self.inventory = inventory
        self.currencies = []
        self.uniques = []
        self.weapons = []
        self.rare_helms = []
        self.rare_bodies = []
        self.rare_belts = []
        self.rare_gloves = []
        self.rare_boots = []
        self.rare_rings = []
        self.rare_amulets = []
        self.unknowns = []

        self.inv_i = 0
        self.inv_j = 0

    def __str__(self):
        print('inventory:')
        for row in self.inventory:
            print(row)
        print('items:')
        for name, items in self.__dict__.items():
            if items and name != 'inventory':
                print(name, items)
        return ''

    def cell_to_rect(self, cell):
        # cell[0] = row ,, cell[1] = col
        rect = []
        rect.append(self.INV_TOP_LEFT_X + self.INV_CELL_WIDTH * cell[1])
        rect.append(self.INV_TOP_LEFT_Y + self.INV_CELL_HEIGHT * cell[0])
        rect.append(self.INV_CELL_WIDTH)
        rect.append(self.INV_CELL_HEIGHT)
        return rect

    def parse(self, data, center):
        rarity = data[1]
        if rarity == 'Currency':
            # todo add to currency list
            self.currencies.append(center)
            print("found currency")
            self.log_item_in_inv('Currency')
        elif rarity == 'Unique':
            # todo add to unique list
            self.uniques.append(center)
            print("found unique")
            self.log_item_in_inv('Unique')
        else:
            # must be rare
            self.parse_rare(data, center)

    def parse_rare(self, data, center):
        for word in data:
            if word in AI.weapon_keywords:
                self.weapons.append(center)
                print("found weapon")
                self.log_item_in_inv('Weapon')
                return
            elif word in AI.helm_keywords:
                self.rare_helms.append(center)
                print("found helm")
                self.log_item_in_inv('Helm')
                return
            elif word in AI.body_keywords:
                self.rare_bodies.append(center)
                print("found body")
                self.log_item_in_inv('Body')
                return
            elif word in AI.belt_keywords:
                self.rare_belts.append(center)
                print("found belt")
                self.log_item_in_inv('Belt')
                return
            elif word in AI.gloves_keywords:
                self.rare_gloves.append(center)
                print("found gloves")
                self.log_item_in_inv('Gloves')
                return
            elif word in AI.boots_keywords:
                self.rare_boots.append(center)
                print("found boots")
                self.log_item_in_inv('Boots')
                return
            elif word in AI.ring_keywords:
                self.rare_rings.append(center)
                print("found ring")
                self.log_item_in_inv('Ring')
                return
            elif word in AI.amulet_keywords:
                self.rare_amulets.append(center)
                print("found amulet")
                self.log_item_in_inv('Amulet')
                return 
        self.unknowns.append(center)
        print('found unknown')
        print('logging unknown data to unknown_data.txt')
        self.record_unknown_data(data)
        self.log_item_in_inv('Unknown')
        return

    def log_item_in_inv(self, item):
        print('adding item to virtual inventory')
        if item == 'Weapon':
            for m in range(4):
                for n in range(2):
                    self.inventory[self.inv_i + m][self.inv_j + n] = 1
        elif item == 'Helm' or item == 'Gloves' or item == 'Boots':
            for m in range(2):
                for n in range(2):
                    self.inventory[self.inv_i + m][self.inv_j + n] = 1
        elif item == 'Body':
            for m in range(3):
                for n in range(2):
                    self.inventory[self.inv_i + m][self.inv_j + n] = 1
        elif item == 'Currency' or item == 'Ring' or item == 'Amulet':
            self.inventory[self.inv_i][self.inv_j]
        elif item == 'Belt':
            for n in range(2):
                self.inventory[self.inv_i][self.inv_j + n] = 1
        else:
            self.log_unknown_in_inv()

    def log_unknown_in_inv(self):
        print('finding cells of unknown/unique')
        for i in range(self.inv_i, self.inv_i + 4):
            for j in range(self.inv_j, self.inv_j + 2):
                if i ==  AI.INV_HEIGHT:
                    break
                if j == AI.INV_WIDTH:
                    continue
                if not self.inventory[i][j]:
                    rect = self.cell_to_rect([i, j])
                    center = rectangle.calc_center_absolute_rect(rect)
                    pyautogui.moveTo(center[0], center[1], 0.2)
                    time.sleep(0.5)

                    win32clipboard.OpenClipboard()
                    win32clipboard.EmptyClipboard()
                    win32clipboard.SetClipboardText('test')
                    win32clipboard.CloseClipboard()

                    # todo : ctrl + c on cell
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('c')
                    pyautogui.keyUp('ctrl')

                    # todo : check if clipboard is test
                    win32clipboard.OpenClipboard()
                    data = win32clipboard.GetClipboardData()
                    win32clipboard.CloseClipboard()

                    if data != 'test':
                        self.inventory[i][j] = 1

    def record_unknown_data(self, data):
        f = open('unknown_data.txt', 'a')
        f.write('\n##########################\n')
        for word in data:
            f.write(word)
        f.write('\n##########################\n')
        f.close()

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
        print('finding item in inventory')
        for i, row in enumerate(self.inventory):
            for j, cell in enumerate(row):
                if not cell:
                    self.inv_i = i
                    self.inv_j = j
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
                    
                    if data != 'test':
                        print('item found in inventory', i, j)
                        # parse clipboard for words to tell what kind of item it is
                        split_data = data.split()
                        print('starting item logging procedures')
                        self.parse(split_data, center)
                        print('added to inventory')
                        pyautogui.press('i')
                        return

        pyautogui.press('i')