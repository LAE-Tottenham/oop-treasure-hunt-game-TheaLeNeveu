from InquirerPy import prompt

class Player:
    def __init__(self, name, bag):
        self.name = name
        self.bag = bag
        self.max_hp = 100
        self.hp = self.max_hp

    def pick_up(self, item):
        print(f"You have found a {item}")
        if item.__class__.__name__ != "Bag":
            self.bag.add(item)
        else:
            self.new_bag(item)
          
    def new_bag(self, bag):
       temp = self.bag.inventory
       self.bag = bag
       self.bag.inventory.append(temp)
       print("You upgraded to a {self.bag.name} which can hold {self.max_capacity}!")
       print("Don't worry. All your items from your old bag have been transferred to your new one.")

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
        self.inventory = []
    
    def add(self, item):
      if self.check_full():
        self.inventory.append(item)
        print(f"You put the {item.name} in {self.name}")
      else:
        print(f"{self.name} is full")

    def remove(self, item):
       for i in self.inventory:
          if i.name == item:
             self.inventory.remove(i)

    def check_full(self):
      if len(self.inventory) == self.max_capacity:
        return False
      else:
        return True
      
    def view_inventory(self):
        if len(self.inventory) == 0:
           print(f"There is nothing in {self.name}")
        for i in self.inventory:
           print(i.name)
        