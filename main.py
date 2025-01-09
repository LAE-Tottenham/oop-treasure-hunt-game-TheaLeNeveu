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

# human_mouse = Person("Molly")
# human_rabbit = Person("Roger")
# human_magpie1 = Person("Maggie")
# human_magpie2 = Person("Mabel")
# human_magpie3 = Person("Miles")
# human_owl = Person("Owen")
# human_snail = Person("Sasha")

mouse = Trivia_NPC("Molly")
rabbit = TicTacToe_NPC("Roger")
magpie1 = HideAndSeek_NPC("Maggie")
magpie1.hidden_item = marble
magpie2 = HideAndSeek_NPC("Mabel")
magpie2.hidden_item = flower
magpie3 = HideAndSeek_NPC("Miles")
magpie3.hidden_item = sock
owl = Riddle_NPC("Owen")
snail = Hangman_NPC("Sasha")

hand = Bag("hand", 1)
basket = Bag("basket", 5)
backpack = Bag("backpack", 10)

hallway = Place("hallway", [0,0], [], [], [], False)
lab = Place("lab", [0,0], [], [], [], False)
sandbox = Place("sandbox", [0,0], [key], [owl], [], True)
garden = Place("garden", [10, 0], [basket, key, marble], [rabbit, magpie1, magpie2], [chest2, chest3, chest4], True)

class Game():
    def __init__(self):
        self.places = [lab, hallway, sandbox, garden]
        self.current_place = self.places[0]

    def start(self):
        print("You can move using the keys w, a, s, d. You can check your inventory with v. If you want to quit you can press q.")
        print("You can intect with things by moving to the same position as it. (. = nothing, # = door, X = chest, ? = friend)")
        print("Hint: Make sure you search all the rooms carefully you cannot go back to any previous rooms so make sure you have everything you need before you leave.")

        for i in range(3):
            print("...")

        print("Finally! You're awake I've been waiting for you to wake up for ages.")
        print("What you were doing asleep in here Halley?")
        print("Why are you staring at me like that? Is it because I'm a snail?")
        print("Oh! Your name isn't Halley? Sorry, I didn't think you'd have a problem with a nickname. I'm a bit slow, being a snail and all. I'll call you by you're full name from now on.")
        print("So why were you sleeping so long hallucinogen?")
        print("That's not your name either? But it was on the test tube you have in your hand there... Did you steal hallucinogen's test tube?")
        
        name = input("If your name isn't hallucinogen then what is it?")
        self.player = Player(name, hand)
        self.current_place.set_details()

        print(f"{self.player.name}? That was the name on the door of this office. You're head chemist {self.player.name}! I wonder why you go by your last name...")
        print("Anyway, my name's sasha. Nice to meet you!")
        print("I'm going to be off now. See you later!")
        snail.met = True

        # print(f"Hello! You must be {self.player.name}. We're so happy to have you working with us as a chemist.")
        # print("Your lab is the 3rd door to the left in the hallway.")
        # print("You are now in the hallway")
        

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
                self.current_place = self.places[self.places.index(self.current_place)+1]
                self.current_place.set_details()
                print(f"You are now in the {self.current_place.name}")

        elif entity_mapper[current_pos] == "chest":
            for i in self.current_place.chests:
                if i.pos == self.current_place.pos:
                    i.open(self.player)

        elif entity_mapper[current_pos] == "friend":
            for i in self.current_place.npcs:
                if i.pos == self.current_place.pos:
                    i.interact(self.player, self.current_place)
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