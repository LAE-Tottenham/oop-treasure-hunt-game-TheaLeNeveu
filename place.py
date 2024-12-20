import random

def generate_map(height, width):
    entity_index = {
      0: "0",
      1: "#",
      2: "X",
      3: "?",
      4: "!",
      5: ".",
    }
    map = []
    for i in range(height):
        temp = []
        for j in range(width):
          rand_int = random.randint(0, 10)
          if rand_int > 4:
              rand_int = 5
          temp.append(entity_index[rand_int])
        map.append(temp)
    return map

maps = {
    "playground": [
        [".", ".", ".", "#", "#", "#", "#", "0", ".", ".", ".", "."],
        [".", "?", ".", ".", "?", "#", "#", "#", "#", "#", ".", "."],
        ["#", "#", "#", "#", ".", ".", ".", "#", "X", "#", ".", "."],
        [".", ".", ".", ".", ".", "#", "#", ".", ".", "#", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    ],
    "sandbox": [
        [".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "#", "?", "#", "#", "#", "#", "#", "#", "#", "#", "."],
        [".", "#", "#", "#", ".", ".", ".", "#", ".", ".", ".", "."],
        [".", "0", "#", "#", ".", "#", ".", "#", ".", "#", ".", "."],
        [".", ".", ".", ".", ".", "#", ".", ".", ".", "#", ".", "."]
    ],
    "garden": [
        ["#","#","#","#","#","#","#","#","#","#",".",".","#","#","#","#","#","#","#"],
        ["#",".",".",".",".","?","#",".",".",".",".",".",".",".",".","#",".",".","#"],
        ["#",".",".","#","#","#",".",".","#",".",".","#",".",".","#",".",".","#","#"],
        ["#",".",".","#",".",".",".",".",".","#",".",".","#",".",".",".",".",".","#"],
        ["#",".",".","#",".",".","#",".",".","#","#","#","#","#","#","#","#","#","#"],
        ["#",".",".","#",".",".","#",".",".",".",".",".",".",".",".",".",".",".","#"],
        ["#",".",".","#",".",".","#","#","#","#","#","#","#","#","#","#",".",".","#"],
        ["#",".",".","#",".",".",".",".",".",".",".",".","#",".","?","#",".",".","#"],
        ["#",".",".","#","#","#","#","#","#","#",".",".","#",".","#","#",".",".","#"],
        ["#",".",".",".",".",".","#",".",".",".",".",".","#",".","#","#",".",".","#"],
        ["#","#","#","#",".",".","#",".",".","#","#","#","#",".",".","#",".",".","#"],
        ["#",".",".",".",".",".",".",".",".",".","#",".",".",".",".",".",".",".","#"],
        ["#","0","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
    ]
}
    
class Place:
    def __init__(self, name, pos, items, npcs):
        self.name = name
        self.pos = pos
        self.map = maps[name]
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.items = items
        self.npcs = npcs

        for i in range(len(self.map)):
            if "0" in self.map[i]:
                self.door = Door([i, self.map[i].index("0")], True)

        count = 0
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "?":
                    self.npcs[count].pos = [i, j]
                    count += 1
        for i in self.npcs:
            print(i.name, i.pos)


        # self.weapons = ["sword", "bow and arrow", "spear", "shield", "axe"]
        # self.food = ["bread", "cheese", "fruit", "vegetable", "cake"]
        # self.enemies = ["zombie", "skeleton", "witch", "vampire"]
        # self.friends = ["alex", "beth", "eva", "sam"]

        # elif entity_mapper[self.current_pos] == "food":
        #     food = random.choice(self.food)
        # elif entity_mapper[self.current_pos] == "enemy":
        #     enemy = random.choice(self.enemies)
        # elif entity_mapper[self.current_pos] == "friend":
        #     friend = random.choice(self.friends)
        # elif entity_mapper[self.current_pos] == "door":
        #     door = random.choice(self.door)

# class RandomPlace(Place):
#     def __init__(self, pos, size):
#         super().__init__(pos, size)
#         self.map = generate_map(self.height, self.width)

class Door:
    def __init__(self, location, locked):
        self.location = location
        self.locked = locked

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