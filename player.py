class Player:
    def __init__(self, name, bag, pos):
        self.name = name
        self.bag = bag
        self.pos = pos
        self.max_hp = 100
        self.hp = self.max_hp

    def move(self, key_press):
        if key_press == "d":
          self.pos[0] += 1
        elif key_press == "a":
          self.pos[0] -= 1
        elif key_press == "w":
          self.pos[1] -= 1
        elif key_press == "s":
          self.pos[1] += 1
          
    def interact(self):
      pass
    
    def eat(self, food):
      self.hp += food.energy
      if self.hp > self.max_hp:
        self.hp = self.max_hp

class Bag:
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = int(max_capacity)
        self.items = []
    
    def add(self, item):
      if self.check_full():
        self.items.append(item)
      else:
        print(f"{self.name} is full")

    def check_full(self):
      if len(self.items) == self.max_capacity:
        return False
      else:
        return True
      