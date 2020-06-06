class Page:
    def __init__(self, ptype):
        self.ptype = ptype
        if ptype == 0:
            self.grid = [[0]*12 for i in range(12)]

        # lists of locations of items
        self.weapons = []
        self.helms = []
        self.bodies = []
        self.belts = []
        self.gloves = []
        self.boots = []
        self.rings = []
        self.amulets = []

        # lists of next available location
        self.weapon_avail = [0, 0]
        self.helm_avail = [0, 0]
        self.body_avail = [0, 0]
        self.belt_avail = [0, 0]
        self.gloves_avail = [0, 0]
        self.boots_avail = [0, 0]
        self.ring_avail = [0, 0]
        self.amulet_avail = [0, 0]

    def update_avail(self, item):
        if item == 'Weapon':
            for j in range(12):
                for i in range(12):
                    bad = False
                    for m in range(4):
                        if i + m > 11:
                            bad = True
                        if bad:
                            break
                        for n in range(2):
                            if j + n > 11:
                                bad = True
                            if bad:
                                break
                            if self.grid[i + m][j + n]:
                                bad = True
                    if not bad:
                        self.weapon_avail = [i, j]
                        return
            self.weapon_avail = [-1, -1]
            return

        if item == 'Helm':
            for j in range(12):
                for i in range(12):
                    bad = False
                    for m in range(2):
                        if i + m > 11:
                            bad = True
                        if bad:
                            break
                        for n in range(2):
                            if j + n > 11:
                                bad = True
                            if bad:
                                break
                            if self.grid[i + m][j + n]:
                                bad = True
                    if not bad:
                        self.helm_avail = [i, j]
                        return
            self.helm_avail = [-1, -1]
            return

        if item == 'Gloves':
            for j in range(12):
                for i in range(12):
                    bad = False
                    for m in range(2):
                        if i + m > 11:
                            bad = True
                        if bad:
                            break
                        for n in range(2):
                            if j + n > 11:
                                bad = True
                            if bad:
                                break
                            if self.grid[i + m][j + n]:
                                bad = True
                    if not bad:
                        self.gloves_avail = [i, j]
                        return
            self.gloves_avail = [-1, -1]
            return

        if item == 'Boots':
            for j in range(12):
                for i in range(12):
                    bad = False
                    for m in range(2):
                        if i + m > 11:
                            bad = True
                        if bad:
                            break
                        for n in range(2):
                            if j + n > 11:
                                bad = True
                            if bad:
                                break
                            if self.grid[i + m][j + n]:
                                bad = True
                    if not bad:
                        self.boots_avail = [i, j]
                        return
            self.boots_avail = [-1, -1]
            return

        if item == 'Ring':
            for j in range(12):
                for i in range(12):
                    bad = False
                    for m in range(1):
                        if i + m > 11:
                            bad = True
                        if bad:
                            break
                        for n in range(1):
                            if j + n > 11:
                                bad = True
                            if bad:
                                break
                            if self.grid[i + m][j + n]:
                                bad = True
                    if not bad:
                        self.ring_avail = [i, j]
                        return
            self.ring_avail = [-1, -1]
            return

        if item == 'Amulet':
            for j in range(12):
                for i in range(12):
                    bad = False
                    for m in range(1):
                        if i + m > 11:
                            bad = True
                        if bad:
                            break
                        for n in range(1):
                            if j + n > 11:
                                bad = True
                            if bad:
                                break
                            if self.grid[i + m][j + n]:
                                bad = True
                    if not bad:
                        self.amulet_avail = [i, j]
                        return
            self.amulet_avail = [-1, -1]
            return

        if item == 'Belt':
            for j in range(12):
                for i in range(12):
                    bad = False
                    for m in range(1):
                        if i + m > 11:
                            bad = True
                        if bad:
                            break
                        for n in range(2):
                            if j + n > 11:
                                bad = True
                            if bad:
                                break
                            if self.grid[i + m][j + n]:
                                bad = True
                    if not bad:
                        self.belt_avail = [i, j]
                        return
            self.belt_avail = [-1, -1]
            return

        if item == 'Body':
            for j in range(12):
                for i in range(12):
                    bad = False
                    for m in range(3):
                        if i + m > 11:
                            bad = True
                        if bad:
                            break
                        for n in range(2):
                            if j + n > 11:
                                bad = True
                            if bad:
                                break
                            if self.grid[i + m][j + n]:
                                bad = True
                    if not bad:
                        self.body_avail = [i, j]
                        return
            self.body_avail = [-1, -1]
            return

    def store_item(self, item):
        if item == 'Weapon':
            for n in range(4):
                for m in range(2):
                    self.grid[self.weapon_avail[0] + n][self.weapon_avail[1] + m] = 1
            self.weapons.append([self.weapon_avail[0], self.weapon_avail[1]])
            return

        if item == 'Helm':
            for n in range(2):
                for m in range(2):
                    self.grid[self.helm_avail[0] + n][self.helm_avail[1] + m] = 1
            self.helms.append([self.helm_avail[0], self.helm_avail[1]])
            return

        if item == 'Gloves':
            for n in range(2):
                for m in range(2):
                    self.grid[self.gloves_avail[0] + n][self.gloves_avail[1] + m] = 1
            self.gloves.append([self.gloves_avail[0], self.gloves_avail[1]])
            return

        if item == 'Boots':
            for n in range(2):
                for m in range(2):
                    self.grid[self.boots_avail[0] + n][self.boots_avail[1] + m] = 1
            self.boots.append([self.boots_avail[0], self.boots_avail[1]])
            return

        if item == 'Ring':
            for n in range(1):
                for m in range(1):
                    self.grid[self.ring_avail[0] + n][self.ring_avail[1] + m] = 1
            self.rings.append([self.ring_avail[0], self.ring_avail[1]])
            return

        if item == 'Amulet':
            for n in range(1):
                for m in range(1):
                    self.grid[self.amulet_avail[0] + n][self.amulet_avail[1] + m] = 1
            self.amulets.append([self.amulet_avail[0], self.amulet_avail[1]])
            return

        if item == 'Belt':
            for n in range(1):
                for m in range(2):
                    self.grid[self.belt_avail[0] + n][self.belt_avail[1] + m] = 1
            self.belts.append([self.belt_avail[0], self.belt_avail[1]])
            return

    def print_grid(self):
        for row in self.grid:
            print(row)

class Stash:
    def __init__(self, pages):
        self.pages = pages

        # count of items in stash
        self.weapons = 0
        self.helms = 0
        self.bodies = 0
        self.belts = 0
        self.gloves = 0
        self.boots = 0
        self.rings = 0
        self.amulets = 0


