import random

#all the subprograms for the appearance and processes of the game's board
class Board:
  def __init__(self):
    self.main = []
    #creating one larger board where each list of 9 makes up a local board
    for _ in range (9):
      self.main.append(["-","-","-","-","-","-","-","-","-"])
    
    #I have kept 9 available here so that moves can be validated as legal
    self.bigwins = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",\
                    8:"",9:"False"}
    self.gameWon = False
    self.winCombos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    #finds the major board that was last played by a player so that it can be checked for a win.
    self.recentlyplayed = 0

  #displays the board in the format that it should be played
  def display(self):
    print(self.main[0][0:3],self.main[1][0:3],self.main[2][0:3])
    print(self.main[0][3:6],self.main[1][3:6],self.main[2][3:6])
    print(self.main[0][6:9],self.main[1][6:9],self.main[2][6:9])
    print("")
    print(self.main[3][0:3],self.main[4][0:3],self.main[5][0:3])
    print(self.main[3][3:6],self.main[4][3:6],self.main[5][3:6])
    print(self.main[3][6:9],self.main[4][6:9],self.main[5][6:9])
    print("")
    print(self.main[6][0:3],self.main[7][0:3],self.main[8][0:3])
    print(self.main[6][3:6],self.main[7][3:6],self.main[8][3:6])
    print(self.main[6][6:9],self.main[7][6:9],self.main[8][6:9])

  #function that returns a list of all squares in a smaller board that can be played
  def findAvailable(self,outer):
    self.available = []
    for x in range (9):
      if self.main[outer][x] == "-":
        self.available.append(x)
    return self.available

  #function that checks for a win in an major square. If a win is found, it will then
  #check the whole board to find 3 major wins in a row, or a full game win.
  def winCheck(self):
    found = False    
    print("Checking square:",self.recentlyplayed,"for a win.")
    for y in range(len(self.winCombos)):
      if self.main[self.recentlyplayed][self.winCombos[y][0]] == self.main\
      [self.recentlyplayed][self.winCombos[y][1]] == self.main[self.recentlyplayed]\
      [self.winCombos[y][2]] and self.main[self.recentlyplayed]\
      [self.winCombos[y][0]] !="-":
        self.bigwins[self.recentlyplayed] = self.main[self.recentlyplayed]\
        [self.winCombos[y][0]]
        print("Square",self.recentlyplayed,"won by",self.main[self.recentlyplayed]\
             [self.winCombos[y][0]])
        #if the most recently played major square has already been won, this if
        #statement allows for them to select whatever major square they want.
        if self.bigwins[play.lastplayed] != "":         
          play.lastplayed = 9
        found = True

    #If a major square has been won, here it checks for a whole game win.
    if found is True:
      for i in range(len(self.winCombos)):
        if self.bigwins[self.winCombos[i][0]] == self.bigwins[self.winCombos[i][1]] ==\
        self.bigwins[self.winCombos[i][2]] and self.bigwins[self.winCombos[i][0]] != "":
          self.gameWon = True
          self.display()
          print("Player", self.bigwins[self.winCombos[i][0]], "wins!")
        

#the superclass for all the forms of players
class player():
  def __init__(self,letter):
    self.letter = letter
    self.littlechoice = 9
    self.bigchoice = 9
  
  #def move(self):
    #self.littlechoice = 9
    #self.bigchoice = 9
    #if board.bigwins[play.lastplayed] != "":
      #while board.bigwins[self.bigchoice] != "":
        #enter()
        

#the class for a player where a user selects whatever square they want to play in.
class user(player):
  def __init__(self,letter):
    super().__init__(letter)
  
  #user selection of a move.
  def move(self):
    board.display() 
    self.littlechoice = 9
    self.bigchoice = 9
    if board.bigwins[play.lastplayed] != "":
      while board.bigwins[self.bigchoice] != "": 
        print("Player", str(self.letter) ,"Enter larger square:")
        self.bigchoice = int(input())
    else:
      self.bigchoice = play.lastplayed
    board.findAvailable(self.bigchoice)
    while self.littlechoice not in board.available:
      print("Player", str(self.letter) ,"Enter inner square:")
      self.littlechoice = int(input())
    board.recentlyplayed = self.bigchoice
    board.main[self.bigchoice][self.littlechoice] = self.letter

class stupidAI(player):
  def __init__(self,letter):
    super().__init__(letter)

  #randomly selects a square
  def move(self):
    self.littlechoice = 9
    self.bigchoice = 9
    if board.bigwins[play.lastplayed] != "":
      while board.bigwins[self.bigchoice] != "": 
        self.bigchoice = random.randint(0,8)
    else:
      self.bigchoice = play.lastplayed
    board.findAvailable(self.bigchoice)
    while self.littlechoice not in board.available:
      self.littlechoice = random.randint(0,8)
    board.recentlyplayed = self.bigchoice
    board.main[self.bigchoice][self.littlechoice] = self.letter
    print("The AI played major square:",self.bigchoice,"minor square:",self.littlechoice)

class smartAI(player):
  def __init__(self,letter):
    super().__init__(letter)

  def values(self):
    
  def minimax(self,depth):
    for x in range(depth):
      
    

#subprograms that control all of the gamemodes
class Game:
  def __init__(self):
    self.lastplayed = 9
  
  def pvp(self,player1,player2):
    while board.gameWon is False:
      player1.move()
      self.lastplayed = player1.littlechoice
      board.winCheck()

      if board.gameWon is False:
        player2.move()
        self.lastplayed = player2.littlechoice
        board.winCheck()

  def stupid(self,player1,player2):
    while board.gameWon is False:
      player1.move()
      self.lastplayed = player1.littlechoice
      board.winCheck()

      if board.gameWon is False:
        player2.move()
        self.lastplayed = player2.littlechoice
        board.winCheck()

  def rules(self):
    print("The Rules:")
    
    
play = Game()
board = Board()

#main menu and gamemode selection
def menu():
  print("1. Player Vs Player")
  print("2. Player Vs stupid AI")
  print("3: The rules")
  mainchoice = int(input("Enter your choice: "))
  if mainchoice == 1:
    xplayer = user("X")
    oplayer = user("O")
    play.pvp(xplayer,oplayer)

  elif mainchoice == 2:
    xplayer = user("X")
    oplayer = stupidAI("O")
    play.stupid(xplayer,oplayer)

  elif mainchoice == 3:
    play.rules()   

menu()
