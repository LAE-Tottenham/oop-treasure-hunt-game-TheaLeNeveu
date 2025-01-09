class NPC:
  def __init__(self, name):
    self.name = name
    self.met = False
    self.difficulty = 1
    self.friendship = 0
    self.item = ""

  def interact(self, player, current_place):
    if self.met == False:
      print("Hi! Who are you?")
      print(f"Your name is {player.name}? I'm {self.name}. Nice to meet you.")
      self.met = True
    else:
      print(f"Hello {player.name}! It's me {self.name}")

    if current_place.npc_status[self] == "complete":
      print("Sorry I don't have anything else on me right now. We'll play another time.")

    else:
      if self.status == "atte":
        print(f"Guess what. I found this {self.item.name} lying around! I'll give you it if you play a game with me.")
        questions = [
          {
            "type": "confirm",
            "message": "Would you like to play?"
          },
        ]
        answers = prompt(questions)
        confirm = answers[0]

      else:
        questions = [
          {
            "type": "confirm",
            "message": "Are you ready to try again?"
          },
        ]
        answers = prompt(questions)
        confirm = answers[0]   

      if confirm:
        print("Amazing!")
        self.attempted = True
        if self.task():
          print("Congratulations, you won!")
          print(f"As promised, here is the {self.item.name}")
          player.pick_up(self.item)
          print("Thanks for playing with me!")
          self.friendship += 10
          print(f"{self.name} gained 10 friendship points.")
          self.completed = True
          self.difficulty += 1
        else:
          print("Thats a shame. Come back when you want to have another go.")
      else:
        print("Thats fine. Come back if you change your mind.")

class Trivia_NPC(NPC):
  def task(self):
    questions = [
      [
        {
          "type": "list",
          "message": "What does the symbol 0 correspond to?",
          "choices": ["door", "wall", "chest", "nothing"],
        },
        {
          "type": "list",
          "message": "What does the symbol # correspond to?",
          "choices": ["chest", "nothing", "enemy", "wall"],
        },
        {
          "type": "list",
          "message": "What does the symbol X correspond to?",
          "choices": ["nothing", "enemy", "chest", "friend"],
        },
        {
          "type": "list",
          "message": "What does the symbol ? correspond to?",
          "choices": ["nothing", "wall", "friend", "door"],
        },
        {
          "type": "list",
          "message": "What does the symbol . correspond to?",
          "choices": ["chest", "wall", "friend", "nothing"],
        },
      ],
    ]

    answers = [
      ["door", "wall", "chest", "friend", "nothing"],
    ]

    quiz = questions[self.difficulty-1]
    results = prompt(quiz)

    score = 0
    for i in range(len(quiz)):
      if results[i] == answers[self.difficulty-1][i]:
        score += 1

    print(f"You got {score}/{len(quiz)}!")
    if score == len(quiz):
      return True
    else:
      print("Sorry but you need to answer all questions correctly to win.")
      return False

class TicTacToe_NPC(NPC):
  def task(self):
    possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def print_game_board():
      for i in range(3):
        print("\n+---+---+---+")
        print("|", end="")
        for j in range(3):
          print("", game_board[i][j], end=" |")
      print("\n+---+---+---+")

    def place_tile(move, symbol):
      for i in range(3):
        for j in range(3):
          if game_board[i][j] == move:
            game_board[i][j] = symbol
            possible_moves.remove(move)
            break

      if game_board[0][0] == game_board[1][1] == game_board[2][2]:
        return game_board[0][0]
      elif game_board[0][2] == game_board[1][1] == game_board[2][0]:
        return game_board[0][2]
      for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2]:
          return game_board[i][0]
        elif game_board[0][i] == game_board[1][i] == game_board[2][i]:
          return game_board[0][i]
      return False

    print("Each go you input the position you would like to place your tile. The positions are the spaces on the board labled 1-9.")
    print("The first to get three tiles in a row, column or diagonally wins.")
    print("I will use X tiles and you will use O tiles. You go first.")
    run = True
    while run:
      print_game_board()
      inp = input("")
      try:
        inp = int(inp)
      except ValueError:
        print("Please enter an integer.")
      else:
        if inp in possible_moves:
          if place_tile(inp, "O") == "O": return True
          move = random.choice(possible_moves)
          if place_tile(move, "X") == "X": return False
        else:
          print("That is not a valid move. Make sure that your input is a number 1-9 and the place is not already occupied.")

class HideAndSeek_NPC(NPC):
  def interact(self, player):
    if self.met == False:
      print("Hi! Who are you?")
      print(f"Your name is {player.name}? I'm {self.name}. Nice to meet you.")
      self.met = True

    else:
      print(f"Hello {player.name}! It's me {self.name}")

    if self.completed:
      print("Sorry I don't have anything else on me right now. We'll play another time.")

    else:
      if self.attempted == False:
        print(f"Guess what. I found this {self.item.name} lying around! I'll give you it if you play a game with me.")
        self.attempted = True
        print(f"I've hidden a {self.hidden_item.name} somewhere around here. Find it and bring it back to me.")
      
      if self.hidden_item in player.bag.inventory:
        print("Congratulations, you won!")
        print(f"As promised, here is the {self.item.name}")
        player.pick_up(self.item)
        print("Thanks for playing with me!")
        self.friendship += 10
        print(f"{self.name} gained 10 friendship points.")
        self.completed = True
        self.difficulty += 1
      else:
        print(f"It doesn't look like you've found a {self.hidden_item.name} yet. Come back when you've got it'.")

class Riddle_NPC(NPC):
  def task(self):
    print("If you want to give up, type q.")
    riddles = [
      ["What has a head and a tail but no body?", "coin"],
      ["You walk into a room that contains a kerosene lamp, a candle and a fireplace. What would you light first?", "match"],
      ["Where does today come before yesterday?", "dictionary"],
      ["What has one eye, but can’t see?", "needle"] 
    ]
    riddle = riddles[self.difficulty - 1][0]
    ans = riddles[self.difficulty - 1][1]
    correct = False
    while correct == False:
      guess = input(riddle)
      for i in guess.split():
        if guess.lower() == ans:
          return True
        elif guess.lower() == "q":
          return False
        else:
          print("That's not right.")

class Hangman_NPC(NPC):
   def task(self):
      drawings = {
        1: "========== \n",
        2: """
        |
        |
        |
        |
        |
        ==========""",
        3: """
        +----+
        |
        |
        |
        |
        |
        ==========""",
        4: """
        +----+
        |    |
        |
        |
        |
        |
        ==========""",
        5: """
        +----+
        |    |
        |    O
        |
        |
        |
        ==========""",
        6: """
        +----+
        |    |
        |    O
        |    |
        |
        |
        ==========""",
        7: """
        +----+
        |    |
        |    O
        |   /|
        |
        |
        ==========""",
        8: """
        +----+
        |    |
        |    O
        |   /|\
        |
        |
        ==========""",
        9: """
        +----+
        |    |
        |    O
        |   /|\
        |   /
        |
        ==========""",
        10: """
        +----+
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

      if self.difficulty == 1:
        word = random.choice(easy_word_options)
      elif self.difficulty == 2:
        word = random.choice(medium_word_options)
      elif self.difficulty == 3:
        word = random.choice(hard_word_options)
      elif self.difficulty == 4:
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