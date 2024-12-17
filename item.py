class Item():
    def __init__(self, name):
        self.name = name
        

      

      
class Food(Item):
  def __init__(self, name, energy):
    super().__init__(name)
    self.energy = energy

