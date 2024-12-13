import random

def generate_map(height, width):
    entity_index = {
      0: ".",
      1: "#",
      2: "X",
      3: "?",
      4: "!",
      5: "F",
      6: "0"
    }
    map = []
    for i in range(1, height):
        temp = []
        for j in range(1, width):
          temp.append(entity_index[random.randint(0, 5)])
        map.append(temp)
    return map

class Place:
    def __init__(self, locked, current_pos, size):
        self.locked = locked
        self.current_pos = current_pos
        self.height = size[0]
        self.width = size[1]
        self.make_maps()
        # self.weapons = ["sword", "bow and arrow", "spear", "shield", "axe"]
        # self.food = ["bread", "cheese", "fruit", "vegetable", "cake"]
        # self.enemies = ["zombie", "skeleton", "witch", "vampire"]
        # self.friends = ["alex", "beth", "eva", "sam"]

    def make_maps(self):
        map = generate_map(self.height, self.width)
        self.map = map
        self.display_map = map
        

    def move(self):
        if entity_mapper[self.current_pos] == "nothing":
            pass
        elif entity_mapper[self.current_pos] == "weapon":
            weapon = random.choice(self.weapons)
        elif entity_mapper[self.current_pos] == "food":
            food = random.choice(self.food)
        elif entity_mapper[self.current_pos] == "enemy":
            enemy = random.choice(self.enemies)
        elif entity_mapper[self.current_pos] == "friend":
            friend = random.choice(self.friends)
        elif entity_mapper[self.current_pos] == "door":
            door = random.choice(self.door)