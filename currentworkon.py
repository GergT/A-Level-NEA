import random
import copy
smallest = -float('inf')

#all the subprograms for the appearance and processes of the game's board
class Board:
  def __init__(self):
    self.main = []
    #creating one larger board where each list of 9 makes up a local board
    for _ in range (9):
      self.main.append(["-","-","-","-","-","-","-","-","-"])
    self.main[0] = ["-","-","-","-","-","-","-","-","-"]

    
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
  def findAvailable(self,outer,wholeboard):
    self.available = []
    for x in range (9):
      if wholeboard[outer][x] == "-":
        self.available.append(x)
        
    return self.available

  #function that returns a list of all squares in a smaller board that can be played
  def findUnavailableMajor(self,bigwins):
    self.available = []
    for x in range (9):
      if bigwins[x] != '':
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
        if self.findAvailable(self.recentlyplayed,board.main) == []:
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
    board.findAvailable(self.bigchoice,board.main)
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
    board.findAvailable(self.bigchoice,board.main)
    while self.littlechoice not in board.available:
      self.littlechoice = random.randint(0,8)
    board.recentlyplayed = self.bigchoice
    board.main[self.bigchoice][self.littlechoice] = self.letter
    print("The AI played major square:",self.bigchoice,"minor square:",self.littlechoice)

class smartAI(player):
  def __init__(self,ailetter,userletter):
    super().__init__(ailetter)
    

    #these 2d lists will be filled with the ratings of the moves
    self.positives = [[],[],[],[],[],[],[],[],[]]
    self.negatives = [[],[],[],[],[],[],[],[],[]]
    self.userletter = userletter
    


  #function that rates all possible plays within a board. returns a 2d list
  def rate(self,majorboard,situboard,situbigwins,letter):
    self.rememberwins = []
    boardwin = []
    winblocked = False
    if letter == self.letter:
      minletter = self.userletter
    else:
      minletter = self.letter

    #initial values preset. 1 for corners and 2 for centre
    ratings = [[majorboard,0,1],[majorboard,1,0],[majorboard,2,1],[majorboard,3,0]\
               ,[majorboard,4,2],[majorboard,5,0], [majorboard,6,1],[majorboard,7,0]\
               ,[majorboard,8,1]]


    #creates copies of the board to show scenarios possible for the user


    #checking for a two in a row

    #top row
    if situboard[majorboard][0] == "-" == situboard[majorboard][1] and situboard[majorboard][2]\
    == letter:
      ratings[1][2] =+5
      ratings[0][2] =+5

    if situboard[majorboard][2] == "-" == situboard[majorboard][0] and situboard[majorboard][1]\
    == letter:
      ratings[0][2] =+5
      ratings[2][2] =+5
    if situboard[majorboard][1] == "-" == situboard[majorboard][2] and situboard[majorboard][0]\
    == letter:
      ratings[1][2] =ratings[1][2]+5
      ratings[2][2] =+5

    #middle row
    if situboard[majorboard][3] == "-" == situboard[majorboard][4] and situboard[majorboard][5]\
    == letter:
      ratings[3][2] =+5
      ratings[4][2] =+5
    if situboard[majorboard][4] == "-" == situboard[majorboard][5] and situboard[majorboard][3]\
    == letter:
      ratings[4][2] =+5
      ratings[5][2] =+5
    if situboard[majorboard][5] == "-" == situboard[majorboard][3] and situboard[majorboard][4]\
    == letter:
      ratings[3][2] =+5
      ratings[5][2] =+5

    #bottom row
    if situboard[majorboard][6] == "-" == situboard[majorboard][7] and situboard[majorboard][8]\
    == letter:
      ratings[7][2] =+5
      ratings[6][2] =+5
    if situboard[majorboard][8] == "-" == situboard[majorboard][7] and situboard[majorboard][6]\
    == letter:
      ratings[8][2] =+5
      ratings[7][2] =+5
    if situboard[majorboard][8] == "-" == situboard[majorboard][6] and situboard[majorboard][7]\
    == letter:
      ratings[6][2] =+5
      ratings[8][2] =+5

    #left column
    if situboard[majorboard][0] == "-" == situboard[majorboard][3] and situboard[majorboard][6]\
    == letter:
      ratings[0][2] =+5
      ratings[3][2] =+5
    if situboard[majorboard][0] == "-" == situboard[majorboard][6] and situboard[majorboard][3]\
    == letter:
      ratings[0][2] =+5
      ratings[6][2] =+5
    if situboard[majorboard][6] == "-" == situboard[majorboard][3] and situboard[majorboard][0]\
    == letter:
      ratings[6][2] =+5
      ratings[3][2] =+5

    #middle column
    if situboard[majorboard][1] == "-" == situboard[majorboard][4] and situboard[majorboard][7]\
    == letter:
      ratings[1][2] =+5
      ratings[4][2] =+5
    if situboard[majorboard][4] == "-" == situboard[majorboard][7] and situboard[majorboard][1]\
    == letter:
      ratings[4][2] =ratings[4][2]+5
      ratings[7][2] =ratings[7][2]+5
    if situboard[majorboard][7] == "-" == situboard[majorboard][1] and situboard[majorboard][4]\
    == letter:
      ratings[7][2] =+5
      ratings[1][2] =+5

    #right column
    if situboard[majorboard][2] == "-" == situboard[majorboard][5] and situboard[majorboard][8]\
    == letter:
      ratings[2][2] =+5
      ratings[5][2] =+5
    if situboard[majorboard][2] == "-" == situboard[majorboard][8] and situboard[majorboard][5]\
    == letter:
      ratings[2][2] =+5
      ratings[8][2] =+5
    if situboard[majorboard][8] == "-" == situboard[majorboard][5] and situboard[majorboard][2]\
    == letter:
      ratings[5][2] =+5
      ratings[8][2] =+5

    #p diagonal
    if situboard[majorboard][6] == "-" == situboard[majorboard][4] and situboard[majorboard][2]\
    == letter:
      ratings[6][2] =+5
      ratings[4][2] =+5
    if situboard[majorboard][2] == "-" == situboard[majorboard][4] and situboard[majorboard][6]\
    == letter:
      ratings[2][2] =+5
      ratings[4][2] =+5
    if situboard[majorboard][6] == "-" == situboard[majorboard][2] and situboard[majorboard][4]\
    == letter:
      ratings[2][2] =+5
      ratings[6][2] =+5

    #n diagonal
    if situboard[majorboard][0] == "-" == situboard[majorboard][4] and situboard[majorboard][8]\
    == letter:
      ratings[0][2] =+5
      ratings[4][2] =+5
    if situboard[majorboard][8] == "-" == situboard[majorboard][4] and situboard[majorboard][0]\
    == letter:
      ratings[8][2] =+5
      ratings[4][2] =+5
    if situboard[majorboard][8] == "-" == situboard[majorboard][0] and situboard[majorboard][4]\
    == letter:
      ratings[0][2] =+5
      ratings[8][2] =+5

    #checking for three in a row
    boardwin =[]
    if situboard[majorboard][0] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][2] == letter or\
    situboard[majorboard][6] == situboard[majorboard][3] == letter or\
    situboard[majorboard][4] == situboard[majorboard][8] == letter:
      ratings[0][2] =+12
      boardwin.append(0)

    if situboard[majorboard][1] == "-" and \
    situboard[majorboard][0] == situboard[majorboard][2] == letter or\
    situboard[majorboard][4] == situboard[majorboard][7] == letter:
      ratings[1][2] =+12
      boardwin.append(1)

    if situboard[majorboard][2] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][0] == letter or\
    situboard[majorboard][8] == situboard[majorboard][5] == letter or\
    situboard[majorboard][4] == situboard[majorboard][6] == letter:
      ratings[2][2] = ratings[2][2] +12
      boardwin.append(2)

    if situboard[majorboard][3] == "-" and \
    situboard[majorboard][0] == situboard[majorboard][6] == letter or\
    situboard[majorboard][4] == situboard[majorboard][5] == letter:
      ratings[3][2] =+12
      boardwin.append(3)

    if situboard[majorboard][4] == "-" and \
    situboard[majorboard][8] == situboard[majorboard][0] == letter or\
    situboard[majorboard][3] == situboard[majorboard][5] == letter or\
    situboard[majorboard][2] == situboard[majorboard][6] == letter or\
    situboard[majorboard][1] == situboard[majorboard][7] == letter:
      ratings[4][2] =+12
      boardwin.append(4)

    if situboard[majorboard][5] == "-" and \
    situboard[majorboard][2] == situboard[majorboard][8] == letter or\
    situboard[majorboard][4] == situboard[majorboard][3] == letter:
      ratings[5][2] =+12
      boardwin.append(5)

    if situboard[majorboard][6] == "-" and \
    situboard[majorboard][4] == situboard[majorboard][2] == letter or\
    situboard[majorboard][0] == situboard[majorboard][3] == letter or\
    situboard[majorboard][7] == situboard[majorboard][8] == letter:
      ratings[6][2] =+12
      boardwin.append(6)

    if situboard[majorboard][7] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][4] == letter or\
    situboard[majorboard][8] == situboard[majorboard][6] == letter:
      ratings[7][2] =+12
      boardwin.append(7)

    if situboard[majorboard][8] == "-" and \
    situboard[majorboard][5] == situboard[majorboard][2] == letter or\
    situboard[majorboard][0] == situboard[majorboard][4] == letter or\
    situboard[majorboard][7] == situboard[majorboard][6] == letter:
      ratings[8][2] =+12
      boardwin.append(8)

    #checking for a game win
    
    if boardwin != []:
      for x in range(len(boardwin)):
        self.rememberwins.append([majorboard,boardwin[x]])
        tempbigwins = copy.deepcopy(situbigwins)
        tempbigwins[majorboard] = letter
        for i in range (len(board.winCombos)):
          if tempbigwins[board.winCombos[i][0]] == tempbigwins\
          [board.winCombos[i][1]] == tempbigwins[board.winCombos[i][2]] == letter:
            ratings[x][2] =+100
            
          

    #checking for a 2-1 block
    winblocked = []
    if situboard[majorboard][0] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][2] == minletter or\
    situboard[majorboard][6] == situboard[majorboard][3] == minletter or\
    situboard[majorboard][4] == situboard[majorboard][8] == minletter:
      ratings[0][2] =+8
      winblocked.append(0)

    if situboard[majorboard][1] == "-" and \
    situboard[majorboard][0] == situboard[majorboard][2] == minletter or\
    situboard[majorboard][4] == situboard[majorboard][7] == minletter:
      ratings[1][2] =+8
      winblocked.append(1)
    if situboard[majorboard][2] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][0] == minletter or\
    situboard[majorboard][8] == situboard[majorboard][5] == minletter or\
    situboard[majorboard][4] == situboard[majorboard][6] == minletter:
      ratings[2][2] = ratings[2][2] +8
      winblocked.append(2)

    if situboard[majorboard][3] == "-" and \
    situboard[majorboard][0] == situboard[majorboard][6] == minletter or\
    situboard[majorboard][4] == situboard[majorboard][5] == minletter:
      ratings[3][2] =+8
      winblocked.append(3)

    if situboard[majorboard][4] == "-" and \
    situboard[majorboard][8] == situboard[majorboard][0] == minletter or\
    situboard[majorboard][3] == situboard[majorboard][5] == minletter or\
    situboard[majorboard][2] == situboard[majorboard][6] == minletter or\
    situboard[majorboard][1] == situboard[majorboard][7] == minletter:
      ratings[4][2] =+8
      winblocked.append(4)

    if situboard[majorboard][5] == "-" and \
    situboard[majorboard][2] == situboard[majorboard][8] == minletter or\
    situboard[majorboard][4] == situboard[majorboard][3] == minletter:
      ratings[5][2] =+8
      winblocked.append(5)

    if situboard[majorboard][6] == "-" and \
    situboard[majorboard][4] == situboard[majorboard][2] == minletter or\
    situboard[majorboard][0] == situboard[majorboard][3] == minletter or\
    situboard[majorboard][7] == situboard[majorboard][8] == minletter:
      ratings[6][2] =+8
      winblocked.append(6)

    if situboard[majorboard][7] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][4] == minletter or\
    situboard[majorboard][8] == situboard[majorboard][6] == minletter:
      ratings[7][2] =+8
      winblocked.append(7)

    if situboard[majorboard][8] == "-" and \
    situboard[majorboard][5] == situboard[majorboard][2] == minletter or\
    situboard[majorboard][0] == situboard[majorboard][4] == minletter or\
    situboard[majorboard][7] == situboard[majorboard][6] == minletter:
      ratings[8][2] =+8
      winblocked.append(8)

    #checking for the block of a game win
    if winblocked is not False:
      for x in winblocked:
        tempbigwins = copy.deepcopy(situbigwins)
        tempbigwins[majorboard] = minletter
        for y in range(len(board.winCombos)):
          if tempbigwins[board.winCombos[y][0]] == tempbigwins[board.winCombos[y][1]]\
          ==tempbigwins[board.winCombos[y][2]] == minletter:
            ratings[x][2] =+50


    return ratings


  #the program that works with the ratings provided by the rate function
  
  def findlargest(self,majorsquare,inputboard,inputbigwins):
    iterationpositives = [[],[],[],[],[],[],[],[],[]]
    iterationnegatives = [[],[],[],[],[],[],[],[],[]]
    biggesteach = []

      
    #Finding the AI's available moves.
    if inputbigwins[majorsquare] == "":
      currentrates = self.rate(majorsquare,inputboard,inputbigwins,self.letter)
      for y in board.findAvailable(majorsquare,inputboard):
        iterationpositives[majorsquare].append(currentrates[y])

    
    else:
      for x in range (9):
        
        currentrates = self.rate(x,inputboard,inputbigwins,self.letter)
        for y in board.findAvailable(x,inputboard):
          iterationpositives[x].append(currentrates[y])

    for j in board.findUnavailableMajor(inputbigwins):
      iterationpositives[j] = []
      


    #checking each of the AI's available moves and rating the user's then possible moves
    for y in range(len(iterationpositives)):
      print("the positive values for board",iterationpositives[y])
      for x in iterationpositives[y]:
        newboard = copy.deepcopy(inputboard)
        newbigwins = copy.deepcopy(inputbigwins)
        newboard[x[0]][x[1]] = self.letter
        
        for i in range(len(self.rememberwins)):
          print(self.rememberwins)
          if self.rememberwins[i] == [x[0],x[1]]:
            newbigwins[x[1]] = self.letter

        print(newbigwins)
        if newbigwins[x[1]] == "":
          negs = self.rate(x[1],newboard,newbigwins,self.userletter)
          print("Board",x[1],"negatives")
          print(negs)
          iterationnegatives[x[1]] = negs

        else:
          for i in range(9):
            stupidlis = (self.rate(i,newboard,newbigwins,self.userletter))
            for j in range(9):
              iterationnegatives[i].append(stupidlis[j])

    
  
    #finding the lowest of all the ratings   
    for y in range(9):
      biggestval = smallest      
      if iterationnegatives[y] == []:
        biggestval = "invalid"
      else:
        for x in range(len(iterationnegatives[y])):
          if iterationnegatives[y][x][2] > biggestval:
            biggestval = iterationnegatives[y][x][2]
            print("Current threat for user in square",y,"is minor",x,"with rating",biggestval)
      
      biggesteach.append(biggestval)

    
    for y in range(9):
      for x in range(len(iterationpositives[y])):
        iterationpositives[y][x][2] = iterationpositives[y][x][2]- biggesteach[iterationpositives[y][x][1]]

    return iterationpositives




  #the recursive subprogram that takes the minimax algorithm to a depth
  def minimax(self,inputboard,inputbigwins,depth):
    
    currentratings = self.findlargest(play.lastplayed,inputboard,inputbigwins)
    
    while depth!= 0:
      depth = depth -1
      
      currentboard = copy.deepcopy(inputboard)
      currentbigwins = copy.deepcopy(inputbigwins)
      print(currentratings)
      print(currentboard)
      
      for p in range(len(currentratings)):
        for y in currentratings[p]:
          currentboard[y[0]][y[1]] = self.letter
          for i in range(len(board.winCombos)):
            if currentboard[y[0]][board.winCombos[i][0]] == currentboard[y[0]][board.winCombos[i][1]]\
            == currentboard[y[0]][board.winCombos[i][2]] == self.letter:
              currentbigwins[y[0]] = self.letter
        
          if y[1] in board.findUnavailableMajor(currentbigwins):
            for j in range(9):
              for k in board.findAvailable(j,currentboard):
                currentboard[j][k] = self.userletter
              
                for i in range(len(board.winCombos)):
                  if currentboard[y[0]][board.winCombos[i][0]] == currentboard[y[0]][board.winCombos[i][1]]\
                  == currentboard[y[0]][board.winCombos[i][2]] == self.userletter:
                    currentbigwins[y[0]] = self.userletter
              
                self.minimax(currentboard,currentbigwins,depth)

          else:
            for x in board.findAvailable(y[1],currentboard):
              currentboard[y[1]][x] = self.userletter
            
              for i in range(len(board.winCombos)):
                if currentboard[y[0]][board.winCombos[i][0]] == currentboard[y[0]][board.winCombos[i][1]]\
                == currentboard[y[0]][board.winCombos[i][2]] == self.userletter:
                  currentbigwins[y[0]] = self.userletter

              self.minimax(currentboard,currentbigwins,depth)

    self.currentsmallest = -smallest
    for h in currentratings:
      if currentratings[h[2]][2] < self.currentsmallest:
        self.currentsmallest = h

    print(self.currentsmallest)


      
              
          
            
            

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

  def smart(self,player1,player2):
    while board.gameWon is False:
      player1.move()
      self.lastplayed = player1.littlechoice
      
      board.winCheck()

      if board.gameWon is False:       
        player2.minimax(board.main,board.bigwins,2)
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
  print("3. Player Vs smart AI")
  print("4: The rules")

  mainchoice = int(input("Enter your choice: "))
  if mainchoice == 1:
    xplayer = user("X")
    oplayer = user("O")
    play.pvp(xplayer,oplayer)

  elif  mainchoice == 2:
    xplayer = user("X")
    oplayer = stupidAI("O")
    play.stupid(xplayer,oplayer)

  elif mainchoice == 3:
    xplayer = user("X")
    oplayer = smartAI("O","X")
    play.smart(xplayer,oplayer)

  elif mainchoice == 4:
    play.rules()   

menu()
