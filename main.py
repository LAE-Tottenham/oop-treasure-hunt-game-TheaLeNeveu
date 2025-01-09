from place import *
from player import *
from npc import *
from item import *

from InquirerPy import prompt
import random

entity_mapper = {
    "0": "door",
    "#": "wall",
    "X": "chest",
    "?": "friend",
    ".": "nothing"
}

marble = Item("marble")
flower = Item("flower")
sock = Item("sock")
yoyo = Item("Yoyo")
key = Item("key")
bread = Food("bread", 100)
fish = Food("fish", 30)

chest1 = Chest(key)
chest2 = Chest(bread)
chest3 = Chest(fish)
chest4 = Chest(flower)
chest5 = Chest(marble)
chest6 = Chest(sock)

olivia = Trivia_NPC("Olivia")
fred = TicTacToe_NPC("Fred")
vivian = HideAndSeek_NPC("Vivian")
victor = HideAndSeek_NPC("Victor")
vincent = HideAndSeek_NPC("Vincent")
vivian.hidden_item = marble
victor.hidden_item = flower
vincent.hidden_item = sock
john = Riddle_NPC("John")
sasha = Hangman_NPC("Sasha")

hand = Bag("hand", 1)
basket = Bag("basket", 5)
backpack = Bag("backpack", 10)

hallway = Place("hallway", [2,0], [], [], [])
sandbox = Place("sandbox", [0,0], [key], [john], [])
garden = Place("garden", [10, 0], [basket, key, marble], [fred, vivian, victor], [chest2, chest3, chest4])

class Game():
    def __init__(self):
        self.places = [hallway, sandbox, garden]
        self.current_place = self.places[0]

    def start(self):
        #name = input("Enter player name: ")
        self.player = Player("name", hand)
        self.current_place.set_details()

        print("You can move using the keys w, a, s, d.")
        print("You can intect with things by moving to the same position as it. . = nothing, # = door, X = chest, ? = friend.")
        #print("Hint: Make sure you search all the rooms carefully you cannot go back to any previous rooms so make sure you have everything you need before you leave.")

        print(f"Hello! You must be {self.player.name}. We're so happy to have you working with us as a chemist.")
        print("Your lab is the 3rd door to the left in the hallway.")
        

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
            for i in self.current_place.doors:
                if i.pos == self.current_place.pos:
                    if i.enter(self.player):
                    if self.current_place.door.enter(self.player):
                        self.current_place = self.places[self.places.index(self.current_place)+1]
                        self.current_place.set_details()
                        print(f"You are now in {self.current_place.name}")

        elif entity_mapper[current_pos] == "chest":
            for i in self.current_place.chests:
                if i.pos == self.current_place.pos:
                    i.open(self.player)

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