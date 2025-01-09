import random
from InquirerPy import prompt

class Item():
    def __init__(self, name):
        self.name = name
      
class Food(Item):
  def __init__(self, name, energy):
    super().__init__(name)
    self.energy = energy

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