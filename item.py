import random
from InquirerPy import prompt

class Item():
    def __init__(self, name):
        self.name = name
      
class Food(Item):
  def __init__(self, name, energy):
    super().__init__(name)
    self.energy = energy

class Door:
    def __init__(self, locked):
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

class Chest:
  def __init__(self, item):
    self.item = item
    self.opened = False

  def open(self, player):
    if self.opened == True:
      print("You've already opened this chest. It's empty.")
    else:
      if player.pick_up(self.item):
        self.opened = True