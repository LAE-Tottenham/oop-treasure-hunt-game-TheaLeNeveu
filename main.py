from place import *
from player import *
from item import *

from InquirerPy import prompt
import random

entity_mapper = {
    "0": "door",
    "#": "wall",
    "X": "chest",
    "?": "friend",
    "!": "enemy",
    ".": "nothing"
}

marble = Item("marble")
key = Item("key")
bread = Food("bread", 100)

olivia = Trivia_NPC("Olivia")
fred = TicTacToe_NPC("Fred")
vivian = HideAndSeek_NPC("Vivian")
victor = HideAndSeek_NPC("Victor")
john = Riddle_NPC("John")
sasha = Hangman_NPC("Sasha")

hand = Bag("hand", 1)
basket = Bag("basket", 5)
backpack = Bag("backpack", 10)

playground = Place("playground", [0,0], [key], [olivia])
sandbox = Place("sandbox", [0,0], [key], [john])
garden = Place("garden", [10, 0], [basket, key], [fred, vivian])

class Game():
    def __init__(self):
        self.places = [playground, sandbox, garden]
        self.current_place = self.places[0]

    def start(self):
        #name = input("Enter player name: ")
        self.player = Player("name", hand)
        self.current_place = playground
        self.current_place.set_details()

        print("You can move using the keys w, a, s, d. You can intect with things by mving to the same position as it.")

    def print_map(self):
        for i in range(self.current_place.height):
            for j in range(self.current_place.width):
                if i == self.current_place.pos[1] and j == self.current_place.pos[0]:
                    print("@", end=" ")
                else:
                    print(self.current_place.map[i][j], end=" ")
            print("\n")

    def move(self, key_press):
        if key_press == "d":
          self.current_place.pos[0] += 1
          if self.check_pos() == False:
            self.current_place.pos[0] -= 1

        elif key_press == "a":
          self.current_place.pos[0] -= 1
          if self.check_pos() == False:
            self.current_place.pos[0] += 1

        elif key_press == "w":
          self.current_place.pos[1] -= 1
          if self.check_pos() == False:
            self.current_place.pos[1] += 1

        elif key_press == "s":
          self.current_place.pos[1] += 1
          if self.check_pos() == False:
            self.current_place.pos[1] -= 1

    def check_pos(self):
        if (self.current_place.pos[1] < 0 or self.current_place.pos[1] > self.current_place.height-1) or (self.current_place.pos[0] < 0 or self.current_place.pos[0] > self.current_place.width-1):
           return False
        
        current_pos = self.current_place.map[self.current_place.pos[1]][self.current_place.pos[0]]

        if entity_mapper[current_pos] == "wall":
            return False
        
        elif entity_mapper[current_pos] == "door":
            if self.current_place.door.enter(self.player):
                for i in self.current_place.npcs:
                    i.completed = False
                    i.attempted = False
                self.current_place = self.places[self.places.index(self.current_place)+1]
                self.current_place.set_details()
                print(f"You are now in {self.current_place.name}")

        elif entity_mapper[current_pos] == "chest":
            item = random.choice(self.current_place.items)
            self.player.pick_up(item)

        elif entity_mapper[current_pos] == "friend":
            for i in self.current_place.npcs:
                if i.pos == self.current_place.pos:
                    i.interact(self.player)
        else:
           pass

    def run(self):
        while True:
            self.print_map()
            key_press = input("")

            if key_press == "q":
                break
            elif key_press == "v":
               self.player.bag.view_inventory()
            else:
                self.move(key_press)

game = Game()

game.start()
game.run()