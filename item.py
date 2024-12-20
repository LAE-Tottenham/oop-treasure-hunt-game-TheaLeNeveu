import random
from InquirerPy import prompt

class Item():
    def __init__(self, name):
        self.name = name
      
class Food(Item):
  def __init__(self, name, energy):
    super().__init__(name)
    self.energy = energy

class NPC:
  def __init__(self, name):
    self.name = name
    self.attempted = False
    self.completed = False
    self.friendship = 0
    self.met = False
    self.pos = [0,0]

  def ineract(self, player, item, difficulty):
    if self.completed:
      print("Sorry I don't have anything else on me right now. We'll play another time.")

    elif self.attempted:
      questions = [
        {
          "type": "confirm",
          "message": "Are you ready to try again?"
        },
      ]
      answers = prompt(questions)
      confirm = answers[0]
      

    else:
      if self.met == False:
        print("Hi! Who are you?")
        print(f"Your name is {player.name}. I'm {self.name}. Nice to meet you.")
        self.met = True

      else:
        print(f"Hello {player.name}! It's me {self.name}")

      print(f"Guess what. I found this {item.name} lying around! I'll give you it if you play a game with me.")
      questions = [
        {
          "type": "confirm",
          "message": "Would you like to play?"
        },
      ]
      answers = prompt(questions)
      confirm = answers[0]

      if confirm:
        print("Amazing!")
        self.attempted = True
        if self.task(difficulty):
          print("Congratulations, you won!")
          print("As promised, here is the {item.name}")
          print("Thanks for playing with me!")
          self.friendship += 10
          print(f"{self.name} gained 10 friendship points.")
          self.completed = True
      else:
        print("Thats fine. Come back if you change your mind.")

class TicTacToe_NPC(NPC):
  def task(self):
    pass

class HideAndSeek_NPC(NPC):
  def task(self, hidden_item):
    print(f"I've hidden a {hidden_item.name} somewhere around here. Find it and bring it back to me.")

class Riddle_NPC(NPC):
  def task(self, difficulty):
    riddles = [
      ["What has a head and a tail but no body?", "coin"],
      ["You walk into a room that contains a kerosene lamp, a candle and a fireplace. What would you light first?", "match"],
      ["Where does today come before yesterday?", "dictionary"],
      ["What has one eye, but can’t see?", "needle"] 
    ]
    riddle = riddles[difficulty - 1][0]
    ans = riddles[difficulty - 1][1]
    correct = False
    while correct == False:
      guess = input(riddle)
      for i in guess.split():
        if guess.lower() == ans:
          return True
      else:
        print("That's not right. (It might be useful to rember that the answer is only one word)")
        questions = [
          {
            "type": "confirm",
            "message": "Would you like to give up?"
          },
        ]
        answers = prompt(questions)
        confirm = answers[0]
        if confirm:
          return False

class Hangman_NPC(NPC):
   def task(self, difficulty):
      drawings = {
        1: "========== \n",
        2: """ |
               |
               |
               |
               |
              ==========""",
        3: """+----+
              |
              |
              |
              |
              |
              ==========""",
        4: """+----+
              |    |
              |
              |
              |
              |
              ==========""",
        5: """+----+
              |    |
              |    O
              |
              |
              |
              ==========""",
        6: """+----+
              |    |
              |    O
              |    |
              |
              |
              ==========""",
        7: """+----+
              |    |
              |    O
              |   /|
              |
              |
              ==========""",
        8: """+----+
              |    |
              |    O
              |   /|\
              |
              |
              ==========""",
        9: """+----+
              |    |
              |    O
              |   /|\
              |   /
              |
              ==========""",
        10: """+----+
              |    |
              |    O
              |   /|\
              |   / \
              |
              ==========""",
      }

      attempts = 0
      correct = False
      guesses = []
      easy_word_options = ["norway", "computer", "london", "orange", "strawberry", "watermelon"]
      medium_word_options = ["python", "javascript", "java", "crystal", "ruby", "swift"]
      hard_word_options = ["syndrome", "whiskey", "cobweb", "jinx", "jaywalk", "haphazard", "awkward", "rhythm"]
      superhard_word_options = ["vaporize", "foxglove", "hieroglyphics", "topaz", "squwark", "onyx", "wizardry", "zodiac"]

      questions = [
        {
          "type": "confirm",
          "message": "Do you already know how to play?"
        },
      ]
      answers = prompt(questions)
      confirm = answers[0]
      if confirm:
        print("Brilliant!")
      else:
        print("The aim of the game is pretty simple, you just have to guess the word I'm thinking of.")
        print("There aren't really any rules, but you should to guess the letters one by one.")
        print("If you think you know what the word is, you can guess the whole word at once.")

      if difficulty == 1:
        word = random.choice(easy_word_options)
      elif difficulty == 2:
        word = random.choice(medium_word_options)
      elif difficulty == 3:
        word = random.choice(hard_word_options)
      elif difficulty == 4:
        word = random.choice(superhard_word_options)

      while attempts < 10 and correct == False:
        for char in word:
          if char in guesses:
            print(char + " ", end="")
          else:
            print("_ ", end="")

        guess = input("\nEnter guess: ")

        if guess == word:
          print("You guessed the word!")
          correct = True
          
        elif guess.isalpha is False or len(guess) > 1 or len(guess) == 0 or guess in guesses:
          print("Sorry, that is not a valid guess.")
          if guess.isalpha is False:
            print("Make sure the input is alphanumeric.")
          elif len(guess) > 1:
            print("Please only guess one letter at a time unless guessing the entire word.")
          elif len(guess) == 0:
            print("Please enter a guess.")
          elif guess in guesses:
            print("You have already guessed that.")

        else:
          if guess in word:
            print("Good job!")
            guesses.append(guess)
            
          elif guess not in word:
            print("That's not right.")
            attempts += 1
            print(drawings[attempts])
            print("You have " + str(10 - attempts) + " lives left.")

      if correct == True:
        return True
      else:
        print("Sorry, but you failed to guess my word in the set amount of guesses.")
        reveal = input(print("Would you like to know what the word was?"))
        if reveal == "yes":
          print("The word was", word)
        else:
          print("Ok, maybe next time.")
        return False
      