import random
import copy
import pygame
smallest = float('-inf')


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
    self.recentMajor = 0

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
    print("Checking square:",self.recentMajor,"for a win.")
    for y in range(len(self.winCombos)):
      if self.main[self.recentMajor][self.winCombos[y][0]] == self.main\
      [self.recentMajor][self.winCombos[y][1]] == self.main[self.recentMajor]\
      [self.winCombos[y][2]] and self.main[self.recentMajor]\
      [self.winCombos[y][0]] !="-":
        self.bigwins[self.recentMajor] = self.main[self.recentMajor]\
        [self.winCombos[y][0]]
        print("Square",self.recentMajor,"won by",self.main[self.recentMajor]\
             [self.winCombos[y][0]])
        #if the most recently played major square has already been won, this if
        #statement allows for them to select whatever major square they want.
        if self.bigwins[play.nextMajor] != "":         
          play.lastplayed = 9
        found = True
        #checking for a draw
        if self.findAvailable(self.recentMajor,board.main) == []:
          self.bigwins[self.recentMajor] = "DRAW"


    #If a major square has been won, here it checks for a whole game win.
    if found is True:
      for i in range(len(self.winCombos)):
        if self.bigwins[self.winCombos[i][0]] == self.bigwins[self.winCombos[i][1]] ==\
        self.bigwins[self.winCombos[i][2]] and self.bigwins[self.winCombos[i][0]] != "":
          self.gameWon = True
          self.display()
          print("Player", self.bigwins[self.winCombos[i][0]], "wins!")

    
  def drawGrid(self):
    backgroundColour = (255,255,200)
    gridColour = (50,50,50)
    screen.fill(backgroundColour)
    for x in range (1,3):
      pygame.draw.line(screen,gridColour,(0,x*300),(screenWidth,x*300),width=5)
      pygame.draw.line(screen,gridColour,(x*300,0),(x*300,screenHeight),width = 5)
    for x in range (1,9):  
      pygame.draw.line(screen,gridColour,(x*100,0),(x*100,screenHeight))
      pygame.draw.line(screen,gridColour,(0,x*100),(screenWidth,x*100))



#the superclass for all the forms of players
class player():
  def __init__(self,letter):
    self.letter = letter
    self.littlechoice = 9
    self.bigchoice = 9
    self.choiceValid = False

#the class for a player where a user selects whatever square they want to play in.
class user(player):
  def __init__(self,letter):
    super().__init__(letter)

  #user selection of a move and drawing the corresponding user's symbol onto their square.
  def move(self):
    self.littlechoice = 9
    self.bigchoice = 9
    calcX = -1
    calcY = -1
    self.choiceValid = False
    
    
    
    pygame.display.update()

    for y in range(3):
      for x in range(3):
        if x*300<clickedX<(x+1)*300 and y*300<clickedY<(y+1)*300:
          self.bigchoice = x+(3*y)
          calcX = clickedX- (300*(clickedX//300))
          calcY = clickedY- (300*(clickedY//300))
          smallCalcY = clickedY - (100*(clickedY//100))
          smallCalcX = clickedX - (100*(clickedX//100))
      
    for y in range(3):
      for x in range(3):
        if x*100<calcX<(x+1)*100 and y*100<calcY<(y+1)*100:
          self.littlechoice = x+(3*y)
      
    

    if board.main[self.bigchoice][self.littlechoice] == "-" and board.bigwins[self.bigchoice] =="" and (self.bigchoice == play.nextMajor or  board.bigwins[play.nextMajor] != ""):
      self.choiceValid = True
      if self.letter == "X":
        board.main[self.bigchoice][self.littlechoice] = self.letter
        pygame.draw.line(screen,xColour, ((clickedX- smallCalcX)+10,(clickedY- smallCalcY)+10),(((clickedX-smallCalcX)+100)-10,((clickedY- smallCalcY)+100)-10),width = 10)
        pygame.draw.line(screen,xColour, ((clickedX- smallCalcX)+90,(clickedY- smallCalcY)+10),(((clickedX-smallCalcX)+10),((clickedY- smallCalcY)+100)-10),width = 10)

      elif self.letter == "O":
        board.main[self.bigchoice][self.littlechoice] = self.letter
        pygame.draw.circle(screen,oColour,((clickedX- smallCalcX)+50,(clickedY- smallCalcY)+50),40,width = 9)
          
      
      play.nextMajor = self.littlechoice
      board.recentMajor = self.bigchoice


    pygame.display.update()
      
    

class stupidAI(player):
  def __init__(self,letter):
    super().__init__(letter)

  #randomly selects a square
  def move(self):
    self.littlechoice = 9
    self.bigchoice = 9
    if board.bigwins[play.nextMajor] != "":
      while board.bigwins[self.bigchoice] != "": 
        self.bigchoice = random.randint(0,8)
    else:
      self.bigchoice = play.nextMajor
    board.findAvailable(self.bigchoice,board.main)
    while self.littlechoice not in board.available:
      self.littlechoice = random.randint(0,8)
    board.recentMajor = self.bigchoice
    board.main[self.bigchoice][self.littlechoice] = self.letter
    print("The AI played major square:",self.bigchoice,"minor square:",self.littlechoice)



class smartAI(player):
  def __init__(self,ailetter,userletter):
    super().__init__(ailetter)
    

    #these will become 3d arrays for all of the possible moves.
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
            
          

    #CHECKING FOR A 2-1 BLOCK / PREVENTING A 3 IN A ROW.
    #A 2-1 Block is worth a +8 score for the player that carries out the block.
    
    #"winblocked" records all the co-ordinates of a square that blocks the enemy player from winning that major square. 
    #The co-ordinates are used again later to check if playing there prevents not only a board loss but a whole game loss.
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

    #Here is where the co-ordinates in "winblocked" are used again to check for the blocking of a whole game.
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
  
  def minimax(self,inputboard,inputbigwins):
    self.positives = [[],[],[],[],[],[],[],[],[]]
    self.negatives = [[],[],[],[],[],[],[],[],[]]
    self.biggesteach = []

      
    #Finding the AI's available moves.
    print(inputbigwins)
    if inputbigwins[play.nextMajor] == "":
      currentrates = self.rate(play.nextMajor,inputboard,inputbigwins,self.letter)
      for y in board.findAvailable(play.nextMajor,inputboard):
        self.positives[play.nextMajor].append(currentrates[y])

    
    else:
      for x in range (9):
        
        currentrates = self.rate(x,inputboard,inputbigwins,self.letter)
        for y in board.findAvailable(x,inputboard):
          self.positives[x].append(currentrates[y])

    print(inputbigwins)
    for j in board.findUnavailableMajor(inputbigwins):
      self.positives[j] = []
      


    #checking each of the AI's available moves and rating the user's then possible moves
    for y in range(len(self.positives)):
      print("the positive values for board",self.positives[y])
      for x in self.positives[y]:
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
          self.negatives[x[1]] = negs

        else:
          for i in range(9):
            stupidlis = (self.rate(i,newboard,newbigwins,self.userletter))
            for j in range(9):
              self.negatives[i].append(stupidlis[j])

    
  
    #finding the lowest rating of all the ratings   
    for y in range(9):
      biggestval = smallest      
      if self.negatives[y] == []:
        biggestval = "invalid"
      else:
        for x in range(len(self.negatives[y])):
          if self.negatives[y][x][2] > biggestval:
            biggestval = self.negatives[y][x][2]
            print("Current threat for user in square",y,"is minor",x,"with rating",biggestval)
      
      self.biggesteach.append(biggestval)

    
    for y in range(9):
      for x in range(len(self.positives[y])):
        self.positives[y][x][2] = self.positives[y][x][2]- self.biggesteach[self.positives[y][x][1]]
    
    #picking the largest remaining value with the negatices taken into account
    picking = ["","",smallest]
    print("NEW POSITIVES AFTER EVALUATION")
    print(self.positives)
    for y in range (9):
      for x in range(len(self.positives[y])):

        if self.positives[y] !=[] and self.positives[y][x][2] > picking[2]:

          picking = self.positives[y][x]
          print("Biggest changed to",picking)

    self.bigchoice = picking[0]
    self.littlechoice = picking[1]
    board.recentMajor = self.bigchoice
    board.main[self.bigchoice][self.littlechoice] = self.letter
    print()
    print("Ai picked large square:", self.bigchoice,"and minor square:", self.littlechoice)
    print()
  

#subprograms that control all of the gamemodes
class Game:
  def __init__(self):
    self.nextMajor = 9

  def pvp(self):
    self.xplayer = user("X")
    self.oplayer = user("O")



  def smart(self):
    self.xplayer = user("X")
    self.oplayer = smartAI("O","X")

  def rules(self):
    print("The Rules:")



play = Game()
board = Board()




#PYGAME WORK BEGINS HERE



pygame.init()

numberTurn = -1
screenWidth = 900
screenHeight = 900
whereClicked = []
xColour = (51,153,255)
oColour = (255,51,51)
clickedX = 0
clickedY = 0

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("ULTIMATE Noughts And Crosses")



mainMenu = pygame.image.load("Main_Menu.jpg").convert()
run = True
modeChosen = False


while run:
  firstClick = False
  for event in pygame.event.get():
     
    if event.type == pygame.QUIT:
      run = False

    if modeChosen is False:
      screen.blit(mainMenu,(0,0))
      pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:
 
      whereClicked = pygame.mouse.get_pos()
      clickedX = whereClicked[0]
      clickedY = whereClicked[1] 
      
      if modeChosen is False and (324<clickedX<575 and 312<clickedY<382):
        modeChosen = "1V1"
        board.drawGrid()
        firstClick = True
        play.pvp()
        pygame.display.update()
      elif modeChosen is False and (324<clickedX<575 and 432<clickedY<503):
        modeChosen = "PVC"
        board.drawGrid()
        play.smart()
        pygame.display.update()
        firstClick = True
      elif modeChosen is False and (324<clickedX<575 and 553<clickedY<623):
        modeChosen = "HTP"
        play.rules()
        firstClick = True


    if event.type == pygame.MOUSEBUTTONDOWN and board.gameWon is False and modeChosen == "1V1" and firstClick is False:
      
      if numberTurn == -1:
        play.xplayer.move()
        board.winCheck()
        if play.xplayer.choiceValid is True:
          numberTurn= numberTurn*-1
      elif numberTurn == 1:
        play.oplayer.move()
        board.winCheck()
        if play.oplayer.choiceValid is True:
          numberTurn= numberTurn*-1

    elif event.type == pygame.MOUSEBUTTONDOWN and board.gameWon is False and modeChosen == "PVC" and firstClick is False:
      while play.xplayer.choiceValid is False:
        play.xplayer.move()
        
      board.winCheck()
      
      play.oplayer.minimax(board.main,board.bigwins)
      board.winCheck()
      





pygame.quit()
