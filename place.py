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
        [".",".",".",".","."],
        ["#","#","#","#","."],
        [".",".",".","#","."],
        [".","#",".","#","."],
        [".","#",".","#","."],
        [".",".",".","#","."],
        [".","#","0","#","."],
        [".","#","#","#","."],
        [".",".",".",".","."],
    ],
    "lab": [
        [".", ".", ".", "#", "#", "#", "#", "0", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "#", "#", "#", "#", "#", ".", "."],
        ["#", "#", "#", "#", ".", ".", "?", "#", "X", "#", ".", "."],
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
    def __init__(self, name, pos, items, npcs, chests, door_locked):
        self.name = name
        self.pos = pos
        self.map = maps[name]
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.items = items
        self.npcs = npcs
        self.chests = chests
        self.door = Door(door_locked)

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

        for j in range(len(self.items)):
            self.npcs[j].item = self.items[j]

        count = 0
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "X":
                    self.chests[count].pos = [j, i]
                    count += 1