from InquirerPy import prompt

class Player:
    def __init__(self, name, bag):
        self.name = name
        self.bag = bag
        self.max_hp = 100
        self.hp = self.max_hp
          
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
        print(f"You put the {item} in {self.name}")
      else:
        print(f"{self.name} is full")

    def check_full(self):
      if len(self.inventory) == self.max_capacity:
        return False
      else:
        return True
      
    # def view_inventory(self):
    #     if len(self.inventory) == 0:
    #        print(f"There is nothing in {self.name}")
    #     for i in self.inventory:
    #        print(i)
        # questions = [
        #     {
        #         "type": "list",
        #         "choices": self.inventory,
        #     }
        # ]
        # answers = prompt(questions)
        # item = answers[0]
        # return item
        # question = {
        #   "type": "list",
        #   "choices": self.inventory
        # }
        # item = prompt(question)[0]
        