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

  #function that returns a list of all squares in a smaller board that can be played
  def findAvailableMajor(self):
    self.available = []
    for x in range (9):
      if self.bigwins[x] == "":
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
        #checking for a draw
        if self.findAvailable(self.recentlyplayed) == []:
          self.bigwins[self.recentlyplayed] = "DRAW"
          

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
  def __init__(self,ailetter,userletter):
    super().__init__(ailetter)
    
    #these will become 3d arrays for all of the possible moves.
    self.positives = []
    self.negatives = []
    self.value = 0
    self.userletter = userletter


  #function that rates all possible plays within a board. returns a 2d list
  def rate(self,board,letter):
    boardwin = False
    #initial values preset. 1 for corners and 2 for centre
    ratings = [[board,0,1],[board,1,0],[board,2,2],[board,3,0],[board,4,2],[board,5,0],\
               [board,6,1],[board,7,0],[board,8,1]] 
    
    #creates copies of the board to show scenarios possible for the user

    
    #checking for a two in a row
    
    #top row
    if self.tempboard[board][0] == "-" == self.tempboard[board][1] and self.tempboard[2]\
    == letter:
      ratings[1][2] =+5
      ratings[0][2] =+5
    if self.tempboard[board][0] == "-" == self.tempboard[board][2] and self.tempboard[1]\
    == letter:
      ratings[0][2] =+5
      ratings[2][2] =+5
    if self.tempboard[board][1] == "-" == self.tempboard[board][2] and self.tempboard[0]\
    == letter:
      ratings[1][2] =+5
      ratings[2][2] =+5

    #middle row
    if self.tempboard[board][3] == "-" == self.tempboard[board][4] and self.tempboard[5]\
    == letter:
      ratings[3][2] =+5
      ratings[4][2] =+5
    if self.tempboard[board][4] == "-" == self.tempboard[board][5] and self.tempboard[3]\
    == letter:
      ratings[4][2] =+5
      ratings[5][2] =+5
    if self.tempboard[board][3] == "-" == self.tempboard[board][5] and self.tempboard[4]\
    == letter:
      ratings[3][2] =+5
      ratings[5][2] =+5

    #bottom row
    if self.tempboard[board][6] == "-" == self.tempboard[board][7] and self.tempboard[8]\
    == letter:
      ratings[7][2] =+5
      ratings[6][2] =+5
    if self.tempboard[board][8] == "-" == self.tempboard[board][7] and self.tempboard[6]\
    == letter:
      ratings[8][2] =+5
      ratings[7][2] =+5
    if self.tempboard[board][6] == "-" == self.tempboard[board][8] and self.tempboard[7]\
    == letter:
      ratings[6][2] =+5
      ratings[8][2] =+5

    #left column
    if self.tempboard[board][0] == "-" == self.tempboard[board][3] and self.tempboard[6]\
    == letter:
      ratings[0][2] =+5
      ratings[3][2] =+5
    if self.tempboard[board][0] == "-" == self.tempboard[board][6] and self.tempboard[3]\
    == letter:
      ratings[0][2] =+5
      ratings[6][2] =+5
    if self.tempboard[board][6] == "-" == self.tempboard[board][3] and self.tempboard[0]\
    == letter:
      ratings[6][2] =+5
      ratings[3][2] =+5
    
    #middle column
    if self.tempboard[board][1] == "-" == self.tempboard[board][4] and self.tempboard[7]\
    == letter:
      ratings[1][2] =+5
      ratings[4][2] =+5
    if self.tempboard[board][1] == "-" == self.tempboard[board][7] and self.tempboard[4]\
    == letter:
      ratings[1][2] =+5
      ratings[7][2] =+5
    if self.tempboard[board][7] == "-" == self.tempboard[board][4] and self.tempboard[1]\
    == letter:
      ratings[7][2] =+5
      ratings[4][2] =+5
      
    #right column
    if self.tempboard[board][2] == "-" == self.tempboard[board][5] and self.tempboard[8]\
    == letter:
      ratings[2][2] =+5
      ratings[5][2] =+5
    if self.tempboard[board][2] == "-" == self.tempboard[board][8] and self.tempboard[5]\
    == letter:
      ratings[2][2] =+5
      ratings[8][2] =+5
    if self.tempboard[board][8] == "-" == self.tempboard[board][5] and self.tempboard[2]\
    == letter:
      ratings[5][2] =+5
      ratings[8][2] =+5

    #p diagonal
    if self.tempboard[board][6] == "-" == self.tempboard[board][4] and self.tempboard[2]\
    == letter:
      ratings[6][2] =+5
      ratings[4][2] =+5
    if self.tempboard[board][2] == "-" == self.tempboard[board][4] and self.tempboard[6]\
    == letter:
      ratings[2][2] =+5
      ratings[4][2] =+5
    if self.tempboard[board][6] == "-" == self.tempboard[board][2] and self.tempboard[4]\
    == letter:
      ratings[2][2] =+5
      ratings[6][2] =+5

    #n diagonal
    if self.tempboard[board][0] == "-" == self.tempboard[board][4] and self.tempboard[8]\
    == letter:
      ratings[0][2] =+5
      ratings[4][2] =+5
    if self.tempboard[board][8] == "-" == self.tempboard[board][4] and self.tempboard[0]\
    == letter:
      ratings[8][2] =+5
      ratings[4][2] =+5
    if self.tempboard[board][8] == "-" == self.tempboard[board][0] and self.tempboard[4]\
    == letter:
      ratings[0][2] =+5
      ratings[8][2] =+5

    #checking for three in a row
    if self.tempboard[0] == "-" and \
    self.tempboard[board][1] == self.tempboard[board][2] == letter or\
    self.tempboard[board][6] == self.tempboard[board][3] == letter or\
    self.tempboard[board][4] == self.tempboard[board][8] == letter:
      ratings[0][2] =+12
    boardwin = 0

    if self.tempboard[1] == "-" and \
    self.tempboard[board][0] == self.tempboard[board][2] == letter or\
    self.tempboard[board][4] == self.tempboard[board][7] == letter:
      ratings[1][2] =+12
    boardwin = 1

    if self.tempboard[2] == "-" and \
    self.tempboard[board][1] == self.tempboard[board][0] == letter or\
    self.tempboard[board][8] == self.tempboard[board][5] == letter or\
    self.tempboard[board][4] == self.tempboard[board][6] == letter:
      ratings[2][2] =+12
      boardwin = 2

    if self.tempboard[3] == "-" and \
    self.tempboard[board][0] == self.tempboard[board][6] == letter or\
    self.tempboard[board][4] == self.tempboard[board][5] == letter:
      ratings[3][2] =+12
    boardwin = 3

    if self.tempboard[4] == "-" and \
    self.tempboard[board][8] == self.tempboard[board][0] == letter or\
    self.tempboard[board][3] == self.tempboard[board][5] == letter or\
    self.tempboard[board][2] == self.tempboard[board][6] == letter or\
    self.tempboard[board][1] == self.tempboard[board][7] == letter:
      ratings[4][2] =+12
    boardwin = 4

    if self.tempboard[5] == "-" and \
    self.tempboard[board][2] == self.tempboard[board][8] == letter or\
    self.tempboard[board][4] == self.tempboard[board][3] == letter:
      ratings[5][2] =+12
    boardwin = 5

    if self.tempboard[6] == "-" and \
    self.tempboard[board][4] == self.tempboard[board][2] == letter or\
    self.tempboard[board][0] == self.tempboard[board][3] == letter or\
    self.tempboard[board][7] == self.tempboard[board][8] == letter:
      ratings[6][2] =+12
    boardwin = 6

    if self.tempboard[7] == "-" and \
    self.tempboard[board][1] == self.tempboard[board][4] == letter or\
    self.tempboard[board][8] == self.tempboard[board][6] == letter:
      ratings[7][2] =+12
    boardwin = 7

    if self.tempboard[8] == "-" and \
    self.tempboard[board][5] == self.tempboard[board][2] == letter or\
    self.tempboard[board][0] == self.tempboard[board][4] == letter or\
    self.tempboard[board][7] == self.tempboard[board][6] == letter:
      ratings[8][2] =+12
      boardwin = 8

    #checking for a game win
    if boardwin is not False:
      self.tempbigwins[boardwin] = letter
      for i in range (len(board.wincombos)):
        if tempbigwins[board.wincombos[i][0]] == tempbigwins[board.wincombos[i][1]] ==\
        tempbigwins[board.wincombos[i][2]] == letter:
          ratings[boardwin][2] =+100
    
    #checking for a 2-1 block
    if self.tempboard[board][0] == "-" 
          
    
    return ratings
  
  def minimax(self):
    self.majoravailable = board.findAvailableMajor()
    #Creates copies of the board so that future predictions can be made.
    self.tempboard = board.main
    self.tempbigwins = board.bigwins

    
    if board.bigwins[play.lastplayed] != "":
      for y in self.majoravailable:
        self.positives.append(self.rate(y,self.letter))
        

    else:
      self.positives.append(self.rate(play.lastplayed,self.letter))


        
    
    

  
        
      

    

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
