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
        [".", ".", ".", ".", ".", "#", "#", "#", "#", "#", ".", "."],
        ["#", "#", "#", "#", ".", ".", ".", "#", "X", "#", ".", "."],
        [".", ".", ".", ".", ".", "#", "#", ".", ".", "#", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    ],
    "sandbox": [
        [".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "#", "X", "#", "#", "#", "#", "#", "#", "#", "#", "."],
        [".", "#", "#", "#", ".", ".", ".", "#", ".", ".", ".", "."],
        [".", "0", "#", "#", ".", "#", ".", "#", ".", "#", ".", "."],
        [".", ".", ".", ".", ".", "#", ".", ".", ".", "#", ".", "X"]
    ],
    "maze": [
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa   a
        8   8               8               8           8                   8   8
        8   8   aaaaaaaaa   8   aaaaa   aaaa8aaaa   aaaa8   aaaaa   aaaaa   8   8
        8               8       8   8           8           8   8   8       8   8
        8aaaaaaaa   a   8aaaaaaa8   8aaaaaaaa   8aaaa   a   8   8   8aaaaaaa8   8
        8       8   8               8           8   8   8   8   8           8   8
        8   a   8aaa8aaaaaaaa   a   8   aaaaaaaa8   8aaa8   8   8aaaaaaaa   8   8
        8   8               8   8   8       8           8           8       8   8
        8   8aaaaaaaaaaaa   8aaa8   8aaaa   8   aaaaa   8aaaaaaaa   8   aaaa8   8
        8           8       8   8       8   8       8           8   8           8
        8   aaaaa   8aaaa   8   8aaaa   8   8aaaaaaa8   a   a   8   8aaaaaaaaaaa8
        8       8       8   8   8       8       8       8   8   8       8       8
        8aaaaaaa8aaaa   8   8   8   aaaa8aaaa   8   aaaa8   8   8aaaa   8aaaa   8
        8           8   8           8       8   8       8   8       8           8
        8   aaaaa   8   8aaaaaaaa   8aaaa   8   8aaaa   8aaa8   aaaa8aaaaaaaa   8
        8   8       8           8           8       8   8   8               8   8
        8   8   aaaa8aaaa   a   8aaaa   aaaa8aaaa   8   8   8aaaaaaaaaaaa   8   8
        8   8           8   8   8   8   8           8               8   8       8
        8   8aaaaaaaa   8   8   8   8aaa8   8aaaaaaa8   aaaaaaaaa   8   8aaaaaaa8
        8   8       8   8   8           8           8   8       8               8
        8   8   aaaa8   8aaa8   aaaaa   8aaaaaaaa   8aaa8   a   8aaaaaaaa   a   8
        8   8                   8           8               8               8   8
        8   8aaaaaaaaaaaaaaaaaaa8aaaaaaaaaaa8aaaaaaaaaaaaaaa8aaaaaaaaaaaaaaa8aaa8
    ],
}
    
class Place:
    def __init__(self, name, pos, items):
        self.name = name
        self.pos = pos
        self.map = maps[name]
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.items = items

        for i in range(len(self.map)):
            if "0" in self.map[i]:
                self.door = Door([i, self.map[i].index("0")], True)

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
        if "key" in player.bag.inventory:
            self.locked = False
            print("The door is now unlocked.")
        else:
            print()