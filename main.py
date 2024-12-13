from place import *
from player import *
from item import *

from InquirerPy import prompt

entity_mapper = {
    ".": "nothing",
    "#": "wall",
    "X": "chest",
    "?": "interaction",
    "!": "enemy",
    "0": "door"
}

playground = Place(False, [0,0], [5, 10])

hand = Bag("Hand", 1)
basket = Bag("Basket", 5)
backpack = Bag("Backpack", 10)

class Game():
    def __init__(self):
        self.current_place = playground

        self.display_map = []

    def setup(self):
        pass

    def start(self):
        #name = input("Enter player name: ")
        self.player = Player("name", "hand", [0, 0])
        self.current_place = playground

    def print_map(self):
        self.current_place.display_map[self.player.pos[1]][self.player.pos[0]] = "@"
        for i in self.current_place.display_map:
            for j in i:
                print(j, end=" ")
            print("\n")
            
        print(self.current_place.map)


    def game_loop(self):
        while True:
            self.print_map()
            key_press = input("")
            self.player.move(key_press)

game = Game()

game.start()
game.game_loop()