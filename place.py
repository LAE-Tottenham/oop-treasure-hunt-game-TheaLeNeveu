from item import *

import random

# def generate_map(height, width):
#     entity_index = {
#       0: "0",
#       1: "#",
#       2: "X",
#       3: "?",
#       4: ".",
#     }
#     map = []
#     for i in range(height):
#         temp = []
#         for j in range(width):
#           rand_int = random.randint(0, 10)
#           if rand_int > 4:
#               rand_int = 5
#           temp.append(entity_index[rand_int])
#         map.append(temp)
#     return map

maps = {
    "hallway": [
        ["#",".",".",".","#"],
        ["#",".",".",".","#"],
        ["#",".",".",".","#"],
        ["0",".",".",".","0"],
        ["#",".",".",".","#"],
        ["0",".",".",".","0"],
        ["#",".",".",".","#"],
        ["0",".",".",".","0"],
        ["#","#","#","#","#"],
    ],
    "empty lab": [
        [".", ".", ".", "#", "#", "#", "#", "0", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "#", "#", "#", "#", "#", ".", "."],
        ["#", "#", "#", "#", ".", ".", ".", "#", ".", "#", ".", "."],
        [".", ".", ".", ".", ".", "#", "#", ".", ".", "#", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ],
    "sandbox": [
        [".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "#", "?", "#", "#", "#", "#", "#", "#", "#", "#", "."],
        [".", "#", "#", "#", ".", ".", ".", "#", ".", ".", ".", "."],
        [".", "0", "#", "#", ".", "#", ".", "#", ".", "#", ".", "."],
        [".", ".", ".", ".", ".", "#", ".", ".", ".", "#", ".", "."],
    ],
    "garden": [
        ["#","#","#","#","#","#","#","#","#","#",".",".","#","#","#","#","#","#","#"],
        ["#",".",".",".",".","?","#",".",".",".",".",".",".",".",".","#",".","X","#"],
        ["#",".",".","#","#","#",".",".","#",".",".","#",".",".","#",".",".","#","#"],
        ["#",".",".","#",".",".",".",".",".","#",".",".","#",".",".",".",".","?","#"],
        ["#",".",".","#",".",".","#",".",".","#","#","#","#","#","#","#","#","#","#"],
        ["#","X",".","#",".",".","#",".",".",".",".",".",".",".",".",".",".",".","#"],
        ["#",".",".","#",".",".","#","#","#","#","#","#","#","#","#","#",".",".","#"],
        ["#",".",".","#",".",".",".",".",".",".",".",".","#",".","?","#",".",".","#"],
        ["#",".",".","#","#","#","#","#","#","#",".",".","#",".","#","#",".",".","#"],
        ["#",".",".",".",".",".","#",".",".",".",".",".","#",".","#","#",".",".","#"],
        ["#","#","#","#",".",".","#",".",".","#","#","#","#",".",".","#",".",".","#"],
        ["#",".",".",".",".",".",".",".",".",".","#","X",".",".",".",".",".",".","#"],
        ["#","0","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
    ],
    "art_class": [
        ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
        ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".",".","#"],
        ["#",".","#","#","#","#","#","#","#","#","#","#","#","#","#",".","#",".","#",".","#"],
        ["#",".","#",".",".",".",".",".",".",".",".",".",".",".","#",".","#",".","#",".","#"],
        ["#",".","#",".","#","#","#","#","#","#","#","#","#",".","#",".","#",".","#",".","#"],
        ["#",".","#",".","#",".",".",".",".",".",".",".","#",".","#",".","#",".","#",".","#"],
        ["#",".","#",".","#","#","#",".","#","#","#",".","#",".","#",".","#",".","#",".","#"],
        ["#",".","#",".",".",".",".",".","#","0",".",".","#",".","#",".","#","?","#",".","#"],
        ["#",".","#",".","#","#","#","#","#","#","#","#","#",".","#",".","#","#","#",".","#"],
        ["#",".","#",".","#",".",".",".",".",".",".",".","#",".","#",".",".",".",".",".","#"],
        ["#",".","#","#","#",".","#","#","#","#","#",".","#",".","#","#","#","#","#",".","#"],
        ["#",".",".",".","#",".","#",".",".",".","#",".","#",".",".",".",".","X","#",".","#"],
        ["#",".","#",".","#",".","#",".","#",".","#",".","#",".","#","#","#","#","#",".","#"],
        ["#","X","#",".","#",".","#",".","#",".","#",".","#",".",".",".",".",".",".",".","#"],
        ["#","#","#",".","#",".","#",".","#",".","#",".","#",".","#","#","#","#","#","#","#"],
        ["#",".",".",".","#",".","#",".","#",".","#",".","#",".","#",".",".",".",".",".","#"],
        ["#",".","#",".","#",".","#",".","#",".","#",".","#",".","#",".","#","#","#",".","#"],
        ["#",".","#","?","#",".",".",".","#",".","#",".","#",".","#",".",".","?","#",".","#"],
        ["#",".","#","#","#","#","#","#","#",".","#",".","#",".","#","#","#","#","#",".","#"],
        ["#",".",".",".",".",".",".",".",".",".","#",".","#",".",".",".",".",".",".",".","#"],
        ["#","#","#","#","#","#","#","#","#","#","#",".","#","#","#","#","#","#","#","#","#"],
    ],
}
    
class Place:
    def __init__(self, name, pos, items, doors, npcs, chests):
        self.name = name
        self.pos = pos
        self.map = maps[name]
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.items = items
        self.doors = doors
        self.npcs = npcs
        self.chests = chests

    def set_details(self):
        self.npc_status = {}
        for i in self.npcs:
            self.npc_status[i] = ""

        count = 0
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "?":
                    self.npcs[count].pos = [j, i]
                    count += 1

        for j in range(len(self.npcs)):
            self.npcs[j].item = self.items[j]

        count = 0
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "X":
                    self.chests[count].pos = [j, i]
                    count += 1

class Door:
    def __init__(self, locked, places):
        self.locked = locked
        self.places = places

    def enter(self, player):
        self.unlock(player)
        if self.locked:
            print("The door is locked. You need a key to unlock it.")
            return False
        else:
            return True
        
    def unlock(self, player):
        for i in player.bag.inventory:
            if i.name == "key":
                self.locked = False
                player.bag.remove("key")
                print("The door is now unlocked.")
                break