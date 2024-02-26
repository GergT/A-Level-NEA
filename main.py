import random
import copy
import pygame
import time
smallest = float('-inf')


#all the subprograms for the appearance and processes of the game's board
class Board:
  def __init__(self):
    
    #The list that makes up the board that the game is played on.
    self.main = []
    
    #Colour that makes up the lines/grid of the board
    self.GRIDCOLOUR = (50,50,50)

    #Colour of the background of the board
    self.backgroundColour = (255,255,200)
   
    #Assigning 9 lists, each with a length of 9 empty values to the board. 
    #This allows for a square to be found using the board's index followed by the square's index almost acting as a co-ordinate system.
    for _ in range (9):
      self.main.append(["-","-","-","-","-","-","-","-","-"])
    self.main[0] = ["-","-","-","-","-","-","-","-","-"]


    #A dictionary containing the status of all 9 boards. Changed to the letter of whoever wins the square or "DRAW" in the case of a draw in that square. I have made 9 an option so that the first player can play in any board.
    self.bigWins = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",\
                    8:"",9:"False"}
    
    #A variable to validify if the game is won. Changed to the letter of whoever won if a win occurs or to "DRAW" if the game is a draw.
    self.gameWon = False
    
    #A 2D array containing all of the possible win combinations of noughts and crosses. Used to check on a square level and a board level.
    self.winCombos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    #Finds the major board that was last played by a player so that it can be checked for a win.
    self.recentMajor = 0


  #Displays the board to the console in the format that it should be played.
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

  #Function that returns a list of all squares in an inputted board that are free to be played.
  def findAvailable(self,outer,wholeboard):
    self.available = []
    for x in range (9):
      if wholeboard[outer][x] == "-":
        self.available.append(x)
    return self.available

  #Function that returns a list of all the boards that have been won by a player or drawn.
  #If a player is assigned to play in one of the boards in this list, on their turn, they can play in whatever available board they like.
  def findUnavailableMajor(self,bigWins):
    self.unavailable = []
    for x in range (9):
      if bigWins[x] != '':
        self.unavailable.append(x)
    return self.unavailable

  #Function to find all the boards that are available to be played in.
  #Used to check if the game has been drawn if this subprogram returns the list [] and a win has not been found.
  def findAvailableMajor(self,bigWins):
    self.available = []
    for x in range(9):
      if bigWins[x] == "":
        self.available.append(x)
    return self.available

  #Function that checks for a win in a board. 
  #If a win is found, it will then check the all the boards to find 3 board wins in wins in a row, resulting in a full game win.
  def winCheck(self):
    #found is used to detect if a board has been won by a player.
    found = False    
    for y in range(len(self.winCombos)):
      if self.main[self.recentMajor][self.winCombos[y][0]] == self.main[self.recentMajor][self.winCombos[y][1]] == self.main[self.recentMajor][self.winCombos[y][2]]\
      and self.main[self.recentMajor][self.winCombos[y][0]] !="-":
        
        self.bigWins[self.recentMajor] = self.main[self.recentMajor][self.winCombos[y][0]]
        print("Square",self.recentMajor,"won by",self.main[self.recentMajor][self.winCombos[y][0]])
        
        found = True
      
      #Checking for a draw
      if self.findAvailable(self.recentMajor,self.main) == []:
        self.bigWins[self.recentMajor] = "DRAW"

      #This for loop fills out each board that has been won or drawn, showing the letter of the board's winner if won or leaving blank if drawn.
      for x in self.findUnavailableMajor(self.bigWins):
        xPos = 0
        yPos = 0
        if x ==1 or x ==4 or x ==7:
          xPos = xPos +300
        elif x==2 or x ==5 or x ==8:
          xPos = xPos +600
        if x == 3 or x ==4 or x==5:
          yPos = yPos +300
        elif x == 6 or x ==7 or x==8:
          yPos = yPos +600

        boardFiller = pygame.Rect(xPos+5,yPos+5,294,294)
        pygame.draw.rect(screen,self.backgroundColour,boardFiller)

        if board.bigWins[x] == "X":
          pygame.draw.line(screen,XCOLOUR,(xPos+10,yPos+10),(xPos+290,yPos +290),width = 10)
          pygame.draw.line(screen,XCOLOUR,(xPos+290,yPos+10),(xPos+10,yPos+290),width=10)
        elif board.bigWins[x] =="O":
          pygame.draw.circle(screen,OCOLOUR,(xPos+150,yPos+150),140,width=10)
        

        pygame.display.update()

    
    #If a major square has been won, here it checks for a whole game win.
    if found is True:
      for i in range(len(self.winCombos)):
        if self.bigWins[self.winCombos[i][0]] == self.bigWins[self.winCombos[i][1]] ==\
        self.bigWins[self.winCombos[i][2]] and self.bigWins[self.winCombos[i][0]] != "":
          self.gameWon = self.bigWins[self.winCombos[i][0]]
          self.display()
          print("Player", self.bigWins[self.winCombos[i][0]], "wins!")
   
    elif self.findAvailableMajor(self.bigWins) == []:
      self.gameWon = "DRAW"

      
      

  #Function to draw the grid and background onto the pygame display.
  def drawGrid(self):
    screen.fill(self.backgroundColour)
    for x in range (1,3):
      pygame.draw.line(screen,self.GRIDCOLOUR,(0,x*300),(SCREENWIDTH,x*300),width=5)
      pygame.draw.line(screen,self.GRIDCOLOUR,(x*300,0),(x*300,SCREENHEIGHT),width = 5)
    for x in range (1,9):  
      pygame.draw.line(screen,self.GRIDCOLOUR,(x*100,0),(x*100,SCREENHEIGHT))
      pygame.draw.line(screen,self.GRIDCOLOUR,(0,x*100),(SCREENWIDTH,x*100))

  #Function to reset the game and the board so that the game can be replayed once it is finished.
  def reset(self):
    self.main = []
    for _ in range (9):
      self.main.append(["-","-","-","-","-","-","-","-","-"])
    self.bigWins = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",\
                    8:"",9:"False"}
    self.gameWon = False
    self.recentMajor = 0
    play.nextMajor = 9



#The superclass for the different types of player
class player():
  def __init__(self,letter):
    self.letter = letter
    self.littleChoice = 9
    self.bigChoice = 9
    self.choiceValid = False

#The class that accomodates for a user, selecting whatever square they want to play in.
class user(player):
  def __init__(self,letter):
    super().__init__(letter)

  #This function converts the user's mouse input into a square and validates the user's selection of a move, drawing the user's symbol onto that square if it is a valid square.
  def move(self):
    self.littleChoice = 9
    self.bigChoice = 9
    calcX = -1
    calcY = -1
    #Variable to validate the user's choice. 
    self.choiceValid = False

    #Calculations to convert the co-ordinates of where the user clicked into co-ordinates on the board (board,square)
    for y in range(3):
      for x in range(3):
        if x*300<clickedX<(x+1)*300 and y*300<clickedY<(y+1)*300:
          self.bigChoice = x+(3*y)
          calcX = clickedX- (300*(clickedX//300))
          calcY = clickedY- (300*(clickedY//300))
          smallCalcY = clickedY - (100*(clickedY//100))
          smallCalcX = clickedX - (100*(clickedX//100))

    for y in range(3):
      for x in range(3):
        if x*100<calcX<(x+1)*100 and y*100<calcY<(y+1)*100:
          self.littleChoice = x+(3*y)


    #Validating the user's chosen square and drawing their letter on that square if move is valid.
    if board.main[self.bigChoice][self.littleChoice] == "-" and board.bigWins[self.bigChoice] =="" and (self.bigChoice == play.nextMajor or  board.bigWins[play.nextMajor] != ""):
      self.choiceValid = True
      if self.letter == "X":
        board.main[self.bigChoice][self.littleChoice] = self.letter
        pygame.draw.line(screen,XCOLOUR, ((clickedX- smallCalcX)+10,(clickedY- smallCalcY)+10),(((clickedX-smallCalcX)+100)-10,((clickedY- smallCalcY)+100)-10),width = 10)
        pygame.draw.line(screen,XCOLOUR, ((clickedX- smallCalcX)+90,(clickedY- smallCalcY)+10),(((clickedX-smallCalcX)+10),((clickedY- smallCalcY)+100)-10),width = 10)

      elif self.letter == "O":
        board.main[self.bigChoice][self.littleChoice] = self.letter
        pygame.draw.circle(screen,OCOLOUR,((clickedX- smallCalcX)+50,(clickedY- smallCalcY)+50),40,width = 9)

      #play.nextMajor is the variable that represents the board that the next user must play in (corresponding to the square the current user selected)
      play.nextMajor = self.littleChoice
      
      #board.recentMajor is used to store the board that was just played in so that board.winCheck() knows what board it must check for a win.
      board.recentMajor = self.bigChoice


    pygame.display.update()

#The class for the Smart AI player
class smartAI(player):
  def __init__(self,ailetter,userletter):
    super().__init__(ailetter)


    #these will become 3d arrays for all of the possible moves. With the 3rd dimension of the list containing the co-ordinates of a square and that square's rating.
    self.positives = [[],[],[],[],[],[],[],[],[]]
    self.negatives = [[],[],[],[],[],[],[],[],[]]
    #The user's letter is stored so that the AI can analyze their possible moves, giving the AI a better evaluation. 
    self.userLetter = userletter



  #Function that rates all possible plays within a board. returns a 2d list
  def rate(self,majorboard,situboard,situbigwins,letter):
    #self.rememberWins remembers the co-ordinates of a play that will win a board. Thus when analysing this play from the user's perspective, that board will have been won.
    self.rememberWins = []
    boardwin = []
    
    #variable used to validify if a 2-1 block was made
    winblocked = False
    
    #establishes what player the evaluation is looking out for 
    if letter == self.letter:
      minletter = self.userLetter
    else:
      minletter = self.letter

    #The function will return this variable of the ratings. Some values are preset. 1 for corners and 2 for centre due to their advantages in game.
    ratings = [[majorboard,0,1],[majorboard,1,0],[majorboard,2,1],[majorboard,3,0]\
               ,[majorboard,4,2],[majorboard,5,0], [majorboard,6,1],[majorboard,7,0]\
               ,[majorboard,8,1]]




    #Checking for a two in a row of the same letter on any row, column or diagonal.
    
    #constant for the rating of a two in a row
    TWOINROW =5

    #top row
    if situboard[majorboard][0] == "-" == situboard[majorboard][1] and situboard[majorboard][2]\
    == letter:
      ratings[1][2] =+TWOINROW
      ratings[0][2] =+TWOINROW

    if situboard[majorboard][2] == "-" == situboard[majorboard][0] and situboard[majorboard][1]\
    == letter:
      ratings[0][2] =+TWOINROW
      ratings[2][2] =+TWOINROW
    if situboard[majorboard][1] == "-" == situboard[majorboard][2] and situboard[majorboard][0]\
    == letter:
      ratings[1][2] =+TWOINROW
      ratings[2][2] =+TWOINROW

    #middle row
    if situboard[majorboard][3] == "-" == situboard[majorboard][4] and situboard[majorboard][5]\
    == letter:
      ratings[3][2] =+TWOINROW
      ratings[4][2] =+TWOINROW
    if situboard[majorboard][4] == "-" == situboard[majorboard][5] and situboard[majorboard][3]\
    == letter:
      ratings[4][2] =+TWOINROW
      ratings[5][2] =+TWOINROW
    if situboard[majorboard][5] == "-" == situboard[majorboard][3] and situboard[majorboard][4]\
    == letter:
      ratings[3][2] =+TWOINROW
      ratings[5][2] =+TWOINROW

    #bottom row
    if situboard[majorboard][6] == "-" == situboard[majorboard][7] and situboard[majorboard][8]\
    == letter:
      ratings[7][2] =+TWOINROW
      ratings[6][2] =+TWOINROW
    if situboard[majorboard][8] == "-" == situboard[majorboard][7] and situboard[majorboard][6]\
    == letter:
      ratings[8][2] =+TWOINROW
      ratings[7][2] =+TWOINROW
    if situboard[majorboard][8] == "-" == situboard[majorboard][6] and situboard[majorboard][7]\
    == letter:
      ratings[6][2] =+TWOINROW
      ratings[8][2] =+TWOINROW

    #left column
    if situboard[majorboard][0] == "-" == situboard[majorboard][3] and situboard[majorboard][6]\
    == letter:
      ratings[0][2] =+TWOINROW
      ratings[3][2] =+TWOINROW
    if situboard[majorboard][0] == "-" == situboard[majorboard][6] and situboard[majorboard][3]\
    == letter:
      ratings[0][2] =+TWOINROW
      ratings[6][2] =+TWOINROW
    if situboard[majorboard][6] == "-" == situboard[majorboard][3] and situboard[majorboard][0]\
    == letter:
      ratings[6][2] =+TWOINROW
      ratings[3][2] =+TWOINROW

    #middle column
    if situboard[majorboard][1] == "-" == situboard[majorboard][4] and situboard[majorboard][7]\
    == letter:
      ratings[1][2] =+TWOINROW
      ratings[4][2] =+TWOINROW
    if situboard[majorboard][4] == "-" == situboard[majorboard][7] and situboard[majorboard][1]\
    == letter:
      ratings[4][2] =ratings[4][2]+TWOINROW
      ratings[7][2] =ratings[7][2]+TWOINROW
    if situboard[majorboard][7] == "-" == situboard[majorboard][1] and situboard[majorboard][4]\
    == letter:
      ratings[7][2] =+TWOINROW
      ratings[1][2] =+TWOINROW

    #right column
    if situboard[majorboard][2] == "-" == situboard[majorboard][5] and situboard[majorboard][8]\
    == letter:
      ratings[2][2] =+TWOINROW
      ratings[5][2] =+TWOINROW
    if situboard[majorboard][2] == "-" == situboard[majorboard][8] and situboard[majorboard][5]\
    == letter:
      ratings[2][2] =+TWOINROW
      ratings[8][2] =+TWOINROW
    if situboard[majorboard][8] == "-" == situboard[majorboard][5] and situboard[majorboard][2]\
    == letter:
      ratings[5][2] =+TWOINROW
      ratings[8][2] =+TWOINROW

    #p diagonal
    if situboard[majorboard][6] == "-" == situboard[majorboard][4] and situboard[majorboard][2]\
    == letter:
      ratings[6][2] =+TWOINROW
      ratings[4][2] =+TWOINROW
    if situboard[majorboard][2] == "-" == situboard[majorboard][4] and situboard[majorboard][6]\
    == letter:
      ratings[2][2] =+TWOINROW
      ratings[4][2] =+TWOINROW
    if situboard[majorboard][6] == "-" == situboard[majorboard][2] and situboard[majorboard][4]\
    == letter:
      ratings[2][2] =+TWOINROW
      ratings[6][2] =+TWOINROW

    #n diagonal
    if situboard[majorboard][0] == "-" == situboard[majorboard][4] and situboard[majorboard][8]\
    == letter:
      ratings[0][2] =+TWOINROW
      ratings[4][2] =+TWOINROW
    if situboard[majorboard][8] == "-" == situboard[majorboard][4] and situboard[majorboard][0]\
    == letter:
      ratings[8][2] =+TWOINROW
      ratings[4][2] =+TWOINROW
    if situboard[majorboard][8] == "-" == situboard[majorboard][0] and situboard[majorboard][4]\
    == letter:
      ratings[0][2] =+TWOINROW
      ratings[8][2] =+TWOINROW


    #CHECKING FOR A THREE IN A ROW / A BOARD WIN
    
    THREEINROW = 12

    #boardwin becomes a 2d array recording the co-ordinates of a square that if played, a board would be won.
    boardwin =[]
    
    if situboard[majorboard][0] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][2] == letter or\
    situboard[majorboard][6] == situboard[majorboard][3] == letter or\
    situboard[majorboard][4] == situboard[majorboard][8] == letter:
      ratings[0][2] =+THREEINROW
      boardwin.append([majorboard,0])

    if situboard[majorboard][1] == "-" and \
    situboard[majorboard][0] == situboard[majorboard][2] == letter or\
    situboard[majorboard][4] == situboard[majorboard][7] == letter:
      ratings[1][2] =+THREEINROW
      boardwin.append([majorboard,1])

    if situboard[majorboard][2] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][0] == letter or\
    situboard[majorboard][8] == situboard[majorboard][5] == letter or\
    situboard[majorboard][4] == situboard[majorboard][6] == letter:
      ratings[2][2] = ratings[2][2] +THREEINROW
      boardwin.append([majorboard,2])

    if situboard[majorboard][3] == "-" and \
    situboard[majorboard][0] == situboard[majorboard][6] == letter or\
    situboard[majorboard][4] == situboard[majorboard][5] == letter:
      ratings[3][2] =+THREEINROW
      boardwin.append([majorboard,3])

    if situboard[majorboard][4] == "-" and \
    situboard[majorboard][8] == situboard[majorboard][0] == letter or\
    situboard[majorboard][3] == situboard[majorboard][5] == letter or\
    situboard[majorboard][2] == situboard[majorboard][6] == letter or\
    situboard[majorboard][1] == situboard[majorboard][7] == letter:
      ratings[4][2] =+THREEINROW
      boardwin.append([majorboard,4])

    if situboard[majorboard][5] == "-" and \
    situboard[majorboard][2] == situboard[majorboard][8] == letter or\
    situboard[majorboard][4] == situboard[majorboard][3] == letter:
      ratings[5][2] =+THREEINROW
      boardwin.append([majorboard,5])

    if situboard[majorboard][6] == "-" and \
    situboard[majorboard][4] == situboard[majorboard][2] == letter or\
    situboard[majorboard][0] == situboard[majorboard][3] == letter or\
    situboard[majorboard][7] == situboard[majorboard][8] == letter:
      ratings[6][2] =+THREEINROW
      boardwin.append([majorboard,6])

    if situboard[majorboard][7] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][4] == letter or\
    situboard[majorboard][8] == situboard[majorboard][6] == letter:
      ratings[7][2] =+THREEINROW
      boardwin.append([majorboard,7])

    if situboard[majorboard][8] == "-" and \
    situboard[majorboard][5] == situboard[majorboard][2] == letter or\
    situboard[majorboard][0] == situboard[majorboard][4] == letter or\
    situboard[majorboard][7] == situboard[majorboard][6] == letter:
      ratings[8][2] =+THREEINROW
      boardwin.append([majorboard,8])


    #Checking if a whole game win is possible.
    if boardwin != []:
      print(boardwin)
      for x in range(len(boardwin)):     
        if boardwin[x] not in self.rememberWins:
          self.rememberWins.append(boardwin[x])
        tempbigWins = copy.deepcopy(situbigwins)
        tempbigWins[majorboard] = letter
        
        for i in range (len(board.winCombos)):
          
          if tempbigWins[board.winCombos[i][0]] == tempbigWins[board.winCombos[i][1]] == tempbigWins[board.winCombos[i][2]] == self.letter and board.main[majorboard][boardwin[x][1]] != "-" and board.bigWins[boardwin[x][0]] == "":
            
            #this "abort" variable's assignment essentially overrides the square selection using ratings since picking this square will win the game for the AI instantly.
            self.abort = [majorboard,boardwin[x][1]]



    #CHECKING FOR A 2-1 BLOCK / PREVENTING A 3 IN A ROW.
    ONETWOBLOCK = 8

    #"winblocked" records all the co-ordinates of a square that blocks the enemy player from winning that major square. 
    #The co-ordinates are used again later to check if playing there prevents not only a board loss but a whole game loss.
    winblocked = []
    if situboard[majorboard][0] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][2] == minletter or\
    situboard[majorboard][6] == situboard[majorboard][3] == minletter or\
    situboard[majorboard][4] == situboard[majorboard][8] == minletter:
      ratings[0][2] =+ONETWOBLOCK
      winblocked.append(0)

    if situboard[majorboard][1] == "-" and \
    situboard[majorboard][0] == situboard[majorboard][2] == minletter or\
    situboard[majorboard][4] == situboard[majorboard][7] == minletter:
      ratings[1][2] =+ONETWOBLOCK
      winblocked.append(1)
    if situboard[majorboard][2] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][0] == minletter or\
    situboard[majorboard][8] == situboard[majorboard][5] == minletter or\
    situboard[majorboard][4] == situboard[majorboard][6] == minletter:
      ratings[2][2] = ratings[2][2] +ONETWOBLOCK
      winblocked.append(2)

    if situboard[majorboard][3] == "-" and \
    situboard[majorboard][0] == situboard[majorboard][6] == minletter or\
    situboard[majorboard][4] == situboard[majorboard][5] == minletter:
      ratings[3][2] =+ONETWOBLOCK
      winblocked.append(3)

    if situboard[majorboard][4] == "-" and \
    situboard[majorboard][8] == situboard[majorboard][0] == minletter or\
    situboard[majorboard][3] == situboard[majorboard][5] == minletter or\
    situboard[majorboard][2] == situboard[majorboard][6] == minletter or\
    situboard[majorboard][1] == situboard[majorboard][7] == minletter:
      ratings[4][2] =+ONETWOBLOCK
      winblocked.append(4)

    if situboard[majorboard][5] == "-" and \
    situboard[majorboard][2] == situboard[majorboard][8] == minletter or\
    situboard[majorboard][4] == situboard[majorboard][3] == minletter:
      ratings[5][2] =+ONETWOBLOCK
      winblocked.append(5)

    if situboard[majorboard][6] == "-" and \
    situboard[majorboard][4] == situboard[majorboard][2] == minletter or\
    situboard[majorboard][0] == situboard[majorboard][3] == minletter or\
    situboard[majorboard][7] == situboard[majorboard][8] == minletter:
      ratings[6][2] =+ONETWOBLOCK
      winblocked.append(6)

    if situboard[majorboard][7] == "-" and \
    situboard[majorboard][1] == situboard[majorboard][4] == minletter or\
    situboard[majorboard][8] == situboard[majorboard][6] == minletter:
      ratings[7][2] =+ONETWOBLOCK
      winblocked.append(7)

    if situboard[majorboard][8] == "-" and \
    situboard[majorboard][5] == situboard[majorboard][2] == minletter or\
    situboard[majorboard][0] == situboard[majorboard][4] == minletter or\
    situboard[majorboard][7] == situboard[majorboard][6] == minletter:
      ratings[8][2] =+ONETWOBLOCK
      winblocked.append(8)

    #Here is where the co-ordinates in "winblocked" are used again to check for the blocking of a whole game.
    if winblocked is not False:
      for x in winblocked:
        tempbigWins = copy.deepcopy(situbigwins)
        tempbigWins[majorboard] = minletter
        for y in range(len(board.winCombos)):
          if tempbigWins[board.winCombos[y][0]] == tempbigWins[board.winCombos[y][1]]\
          ==tempbigWins[board.winCombos[y][2]] == minletter:
            ratings[x][2] =+ 70

  
    
    return ratings


  def prioritiser(self,situbigwins,letter):
    
    #Altering the weights in favour of majorboards that will result in two majorboards being won in a row.
    TWOINROWPRIORITY = 8

    #top row
    if situbigwins[0] == "" == situbigwins[1] and situbigwins[2] == letter:
      for x in range(len(self.positives[0])):
        self.positives[0][x][2] =self.positives[0][x][2]+ TWOINROWPRIORITY
      for y in range(len(self.positives[1])):
        self.positives[1][y][2] =self.positives[1][y][2]+TWOINROWPRIORITY

    elif situbigwins[2] == "" == situbigwins[1] and situbigwins[0] == letter:
      for x in range(len(self.positives[2])):
        self.positives[2][x][2] =self.positives[2][x][2]+ TWOINROWPRIORITY

      for y in range(len(self.positives[1])):
        self.positives[1][y][2] =self.positives[1][y][2]+TWOINROWPRIORITY

    elif situbigwins[2] == "" == situbigwins[0] and situbigwins[1] == letter:
      for x in range(len(self.positives[0])):
        self.positives[0][x][2] =self.positives[0][x][2]+ TWOINROWPRIORITY

      for y in range(len(self.positives[2])):
        self.positives[2][y][2] =self.positives[2][y][2]+TWOINROWPRIORITY

    #middle row
    if situbigwins[3] == "" == situbigwins[4] and situbigwins[5] == letter:

      for x in range(len(self.positives[3])):
        self.positives[3][x][2] =self.positives[3][x][2]+ TWOINROWPRIORITY

      for y in range(len(self.positives[4])):
        self.positives[4][y][2] =self.positives[4][y][2]+TWOINROWPRIORITY

    elif situbigwins[3] == "" == situbigwins[5] and situbigwins[4] == letter:
      for x in range(len(self.positives[3])):
        self.positives[3][x][2] =self.positives[3][x][2]+ TWOINROWPRIORITY

      for y in range(len(self.positives[5])):
        self.positives[5][y][2] =self.positives[5][y][2]+TWOINROWPRIORITY

    elif situbigwins[5] == "" == situbigwins[4] and situbigwins[3] == letter:
      for x in range(len(self.positives[5])):
        self.positives[5][x][2] =self.positives[5][x][2]+ TWOINROWPRIORITY

      for y in range(len(self.positives[4])):
        self.positives[4][y][2] =self.positives[4][y][2]+TWOINROWPRIORITY

    #bottom row
    if situbigwins[6] == "" == situbigwins[7] and situbigwins[8] == letter:
      for x in range(len(self.positives[6])):
        self.positives[6][x][2] =self.positives[6][x][2]+ TWOINROWPRIORITY

      for y in range(len(self.positives[7])):
        self.positives[7][y][2] =self.positives[7][y][2]+TWOINROWPRIORITY

    elif situbigwins[6] == "" == situbigwins[8] and situbigwins[7] == letter:
      for x in range(len(self.positives[6])):
        self.positives[6][x][2] =self.positives[6][x][2]+ TWOINROWPRIORITY

      for y in range(len(self.positives[8])):
        self.positives[8][y][2] =self.positives[8][y][2]+TWOINROWPRIORITY

    elif situbigwins[8] == "" == situbigwins[7] and situbigwins[6] == letter:
      for x in range(len(self.positives[8])):
        self.positives[8][x][2] =self.positives[8][x][2]+ TWOINROWPRIORITY

      for y in range(len(self.positives[7])):
        self.positives[7][y][2] =self.positives[7][y][2]+TWOINROWPRIORITY

    #left column
    if situbigwins[0] == "" == situbigwins[3] and situbigwins[6] == letter:
      for x in range(len(self.positives[0])):
        self.positives[0][x][2] =self.positives[0][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[3])):
        self.positives[3][x][2] =self.positives[3][x][2]+TWOINROWPRIORITY
    elif situbigwins[0] == "" == situbigwins[6] and situbigwins[3] == letter:
      for x in range(len(self.positives[0])):
        self.positives[0][x][2] =self.positives[0][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[6])):
        self.positives[6][x][2] =self.positives[6][x][2]+TWOINROWPRIORITY
    elif situbigwins[6] == "" == situbigwins[3] and situbigwins[0] == letter:
      for x in range(len(self.positives[6])):
        self.positives[6][x][2] =self.positives[6][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[3])):
        self.positives[3][x][2] =self.positives[3][x][2]+TWOINROWPRIORITY
    #middle column
    if situbigwins[1] == "" == situbigwins[4] and situbigwins[7] == letter:
      for x in range(len(self.positives[1])):
        self.positives[1][x][2] =self.positives[1][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[4])):
        self.positives[4][x][2] =self.positives[4][x][2]+TWOINROWPRIORITY
    elif situbigwins[1] == "" == situbigwins[7] and situbigwins[4] == letter:
      for x in range(len(self.positives[1])):
        self.positives[1][x][2] =self.positives[1][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[7])):
        self.positives[7][x][2] =self.positives[7][x][2]+TWOINROWPRIORITY
    elif situbigwins[7] == "" == situbigwins[4] and situbigwins[1] == letter:
      for x in range(len(self.positives[7])):
        self.positives[7][x][2] =self.positives[7][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[4])):
        self.positives[4][x][2] =self.positives[4][x][2]+TWOINROWPRIORITY

    #right column
    if situbigwins[2] == "" == situbigwins[5] and situbigwins[8] == letter:
      for x in range(len(self.positives[2])):
        self.positives[2][x][2] =self.positives[2][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[5])):
        self.positives[5][x][2] =self.positives[5][x][2]+TWOINROWPRIORITY
    elif situbigwins[2] == "" == situbigwins[8] and situbigwins[5] ==letter:
      for x in range(len(self.positives[2])):
        self.positives[2][x][2] =self.positives[2][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[8])):
        self.positives[8][x][2] =self.positives[8][x][2]+TWOINROWPRIORITY
    elif situbigwins[8] == "" == situbigwins[5] and situbigwins[2] == letter:
      for x in range(len(self.positives[8])):
        self.positives[8][x][2] =self.positives[8][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[5])):
        self.positives[5][x][2] =self.positives[5][x][2]+TWOINROWPRIORITY

    #left diagonal
    if situbigwins[0] == "" == situbigwins[4] and situbigwins[8] == letter:
      for x in range(len(self.positives[0])):
        self.positives[0][x][2] =self.positives[0][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[4])):
        self.positives[4][x][2] =self.positives[4][x][2]+TWOINROWPRIORITY

    elif situbigwins[0] == "" == situbigwins[8] and situbigwins[4] == letter:
      for x in range(len(self.positives[0])):
        self.positives[0][x][2] =self.positives[0][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[8])):
        self.positives[8][x][2] =self.positives[8][x][2]+TWOINROWPRIORITY

    elif situbigwins[8] == "" == situbigwins[4] and situbigwins[0] == letter:
      for x in range(len(self.positives[8])):
        self.positives[8][x][2] =self.positives[8][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[4])):
        self.positives[4][x][2] =self.positives[4][x][2]+TWOINROWPRIORITY

    #right diagonal
    if situbigwins[2] == "" == situbigwins[4] and situbigwins[6] == letter:
      for x in range(len(self.positives[2])):
        self.positives[2][x][2] =self.positives[2][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[4])):
        self.positives[4][x][2] =self.positives[4][x][2]+TWOINROWPRIORITY

    elif situbigwins[2] == "" == situbigwins[6] and situbigwins[4] == letter:
      for x in range(len(self.positives[2])):
        self.positives[2][x][2] =self.positives[2][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[6])):
        self.positives[6][x][2] =self.positives[6][x][2]+TWOINROWPRIORITY

    elif situbigwins[6] == "" == situbigwins[4] and situbigwins[2] == letter:
      for x in range(len(self.positives[6])):
        self.positives[6][x][2] =self.positives[6][x][2]+TWOINROWPRIORITY
      for x in range(len(self.positives[4])):
        self.positives[4][x][2] =self.positives[4][x][2]+TWOINROWPRIORITY

    THREEINROWPRIORITY = 30
    #Altering majorboard weightings based upon a 3 in a row.
    if situbigwins[0] == "" and situbigwins[4] == situbigwins[8] == letter or situbigwins[1] == situbigwins[2] == letter or situbigwins[6] == situbigwins[3] == letter:
      for x in range(len(self.positives[0])):
        self.positives[0][x][2] = self.positives[0][x][2]+THREEINROWPRIORITY
    if situbigwins[2] == "" and situbigwins[4] == situbigwins[6] == letter or situbigwins[1] == situbigwins[0] == letter or situbigwins[8] == situbigwins[5] == letter:
      for x in range(len(self.positives[2])):
        self.positives[2][x][2] = self.positives[2][x][2]+THREEINROWPRIORITY
    if situbigwins[6] == "" and situbigwins[4] == situbigwins[2] == letter or situbigwins[0] == situbigwins[3] == letter or situbigwins[8] == situbigwins[7] == letter:
      for x in range(len(self.positives[6])):
        self.positives[6][x][2] = self.positives[6][x][2]+THREEINROWPRIORITY
    if situbigwins[8] == "" and situbigwins[4] == situbigwins[0] == letter or situbigwins[2] == situbigwins[5] == letter or situbigwins[6] == situbigwins[7] == letter:
      for x in range(len(self.positives[8])):
        self.positives[8][x][2] = self.positives[8][x][2]+THREEINROWPRIORITY
    if situbigwins[1] == "" and situbigwins[4] == situbigwins[7] == letter or situbigwins[2] == situbigwins[0] == letter:
      for x in range(len(self.positives[1])):
        self.positives[1][x][2] =self.positives[1][x][2] +THREEINROWPRIORITY
    if situbigwins[3] == "" and situbigwins[4] == situbigwins[5] == letter or situbigwins[6] == situbigwins[0] == letter:
      for x in range(len(self.positives[3])):
        self.positives[3][x][2] = self.positives[3][x][2] +THREEINROWPRIORITY
    if situbigwins[5] == "" and situbigwins[4] == situbigwins[3] == letter or situbigwins[2] == situbigwins[8] == letter:
      for x in range(len(self.positives[5])):
        self.positives[5][x][2] = self.positives[5][x][2] +THREEINROWPRIORITY
    if situbigwins[7] == "" and situbigwins[1] == situbigwins[4] == letter or situbigwins[8] == situbigwins[6] == letter:
      for x in range(len(self.positives[7])):
        self.positives[7][x][2] = self.positives[7][x][2]+THREEINROWPRIORITY
    if situbigwins[4] == "" and situbigwins[1] == situbigwins[7] == letter or situbigwins[8] == situbigwins[0] == letter or situbigwins[6] == situbigwins[2] == letter or situbigwins[3] == situbigwins[5] == letter:
      for x in range(len(self.positives[4])):
        self.positives[4][x][2] = self.positives[4][x][2]+THREEINROWPRIORITY

  #The program that works with the ratings provided by the rate function.

  def minimax(self,inputboard,inputbigWins):
    self.abort = False
    self.positives = [[],[],[],[],[],[],[],[],[]]
    self.negatives = [[],[],[],[],[],[],[],[],[]]
    
    #A list containing the biggest value from each of the user's possible boards. 
    self.biggestEach = []
    


    #Rating the AI's available moves if the board it was sent to is available (not won or drawn).
    if inputbigWins[play.nextMajor] == "":
      currentrates = self.rate(play.nextMajor,inputboard,inputbigWins,self.letter)
      for y in board.findAvailable(play.nextMajor,inputboard):
        self.positives[play.nextMajor].append(currentrates[y])

    #Rating the AI's available moves if the board it was sent to was not available.
    else:
      for x in range (9):
        currentrates = self.rate(x,inputboard,inputbigWins,self.letter)
        for y in board.findAvailable(x,inputboard):
          self.positives[x].append(currentrates[y])



      #Removing any ratings in boards that are unavailable.
      for j in board.findUnavailableMajor(inputbigWins):
        self.positives[j] = []


      #updating the ratings to prioritize getting multiple board wins in a row
      self.prioritiser(inputbigWins,self.letter)

    
    
    #This part of the function creates a copy of the board for each of the AI's possible moves, assigning that square to the AI's letter on the copied board.
    #This copied board is then rated from the user's perspective.
    
    #Repeat for each board with a possible move.
    for y in range(len(self.positives)):
      #Repeat for all possible moves within that board
      for x in self.positives[y]:
        
        #copying the board and the bigWins
        newboard = copy.deepcopy(inputboard)
        newbigWins = copy.deepcopy(inputbigWins)
        #assigning the possible move to the AI's letter
        newboard[x[0]][x[1]] = self.letter

        #Adjusting the copies bigWins if the possible move results in the win of a board.
        for i in range(len(self.rememberWins)):
          if self.rememberWins[i] == [x[0],x[1]]:
            newbigWins[x[1]] = self.letter

        #Rating the board that the possible move has sent the user to from the user's perspective.
        if newbigWins[x[1]] == "":
          negs = self.rate(x[1],newboard,newbigWins,self.userLetter)
          self.negatives[x[1]] = negs

        #If the possible move sends the user to an unavailable square, all boards are rated from the user's perspective.
        else:
          for i in range(9):
            stupidlis = (self.rate(i,newboard,newbigWins,self.userLetter))
            for j in range(9):
              self.negatives[i].append(stupidlis[j])



    #Finding the highes rating of all the ratings from the user's perspective
    for y in range(9):
      biggestval = smallest      
      
      if self.negatives[y] == []:
        biggestval = "invalid"
      
      else:
        for x in range(len(self.negatives[y])):
          if self.negatives[y][x][2] > biggestval:
            biggestval = self.negatives[y][x][2]

      #For each board, a biggest value is assigned (or isn't if that board isn't in the evaluation)
      self.biggestEach.append(biggestval)

    print("POSITIVES BEFORE EVAL")
    print(self.positives)


    #The greatest possible score the user can acheive after each of the AI's possible moves is subtracted from the rating of the AI's corresponding move here. 
    for y in range(9):
      for x in range(len(self.positives[y])):
        self.positives[y][x][2] = self.positives[y][x][2]- self.biggestEach[self.positives[y][x][1]]

    
    #Picking the largest score from the AI's perspective after the user's moves are taken into account.

    picking = ["","",smallest]
    
    print("NEW POSITIVES AFTER EVALUATION")
    print(self.positives)
    
    for y in range (9):
      for x in range(len(self.positives[y])):
        if self.positives[y] !=[] and self.positives[y][x][2] > picking[2]:

          picking = self.positives[y][x]


    #If a game win for the AI has been detected, this code overrides the AI's chosen square.
    if self.abort is not False:
      self.bigChoice = self.abort[0]
      self.littleChoice = self.abort[1]

    else:
      self.bigChoice = picking[0]
      self.littleChoice = picking[1]

    
    board.main[self.bigChoice][self.littleChoice] = self.letter

    #purpose of these lines listed on lines 214 and 217
    play.nextMajor = self.littleChoice
    board.recentMajor = self.bigChoice

    print()
    print("Ai picked large square:", self.bigChoice,"and minor square:", self.littleChoice)
    print()

    #Here are the calculations to convert the AI's square choice into an output on the GUI
    xPos = 50
    yPos = 50

    if self.bigChoice == 1 or self.bigChoice == 4 or self.bigChoice ==7:
      xPos =xPos+ 300
    elif self.bigChoice == 2 or self.bigChoice == 5 or self.bigChoice ==8:
      xPos =xPos+ 600
    if self.bigChoice == 3 or self.bigChoice == 4 or self.bigChoice ==5:
      yPos = yPos +300
    elif self.bigChoice == 6 or self.bigChoice == 7 or self.bigChoice ==8:
      yPos =yPos+600

    if self.littleChoice == 1 or self.littleChoice == 4 or self.littleChoice ==7:
      xPos = xPos+ 100
    elif self.littleChoice == 2 or self.littleChoice == 5 or self.littleChoice ==8:
      xPos =xPos+ 200
    if self.littleChoice == 3 or self.littleChoice == 4 or self.littleChoice ==5:
      yPos =yPos+100
    elif self.littleChoice == 6 or self.littleChoice == 7 or self.littleChoice ==8:
      yPos =yPos+200

    #Drawing the AI's letter (O) onto their chosen square.
    pygame.draw.circle(screen,OCOLOUR,(xPos,yPos),40,width = 9)
    time.sleep(2)
    pygame.display.update()


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




#instantiating the game's key classes
play = Game()
board = Board()


#PYGAME WORK BEGINS HERE
pygame.init()

#numberTurn variable is used for the GUI. Decides whether a click on a square corresponds to an X player or an O player.
numberTurn = -1

SCREENWIDTH = 900
SCREENHEIGHT = 900

#stores the co-ordinates of where the mouse was clicked in regards to the pygame board
whereClicked = []

XCOLOUR = (51,153,255)
OCOLOUR = (255,51,51)

#one variable for each value of the whereClicked co-ordinates
clickedX = 0
clickedY = 0

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("ULTIMATE Noughts And Crosses")


#Converting all of the menu images
MAINMENU = pygame.image.load("Main_Menu.jpg").convert()
HOWTOPLAY = pygame.image.load("How_to_Play.jpg").convert()
XWINS = pygame.image.load("Game_Won_X.jpg").convert()
OWINS = pygame.image.load("Game_Won_O.jpg").convert()
DRAW = pygame.image.load("DRAW.jpg").convert()

#run is used to keep the pygame window running unless closed
run = True

#used to determine what a click on the screen means. If false, the click is in regards to the main menu.
modeChosen = False


while run:
  
  #used to differentiate between chosing your option in the menu and the first click of a square on the board.
  firstClick = False
  
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      run = False

    #displaying the main menu if no mode has been chosen.
    if modeChosen is False:
      screen.blit(MAINMENU,(0,0))
      pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:

      #Records the co-ordinates of where the mouse has been clicked so the button/square they clicked on can be determined.
      whereClicked = pygame.mouse.get_pos()
      clickedX = whereClicked[0]
      clickedY = whereClicked[1] 

      #user clicked on the Player vs Player Button
      if modeChosen is False and (324<clickedX<575 and 312<clickedY<382):
        modeChosen = "1V1"
        board.drawGrid()
        firstClick = True
        play.pvp()
        pygame.display.update()
      
      #user clicked on the Player vs Smart AI button.
      elif modeChosen is False and (324<clickedX<575 and 432<clickedY<503):
        modeChosen = "PVC"
        board.drawGrid()
        play.smart()
        pygame.display.update()
        firstClick = True
      
      #user clicked on the how to play button. Displays How to Play menu.
      elif modeChosen is False and (324<clickedX<575 and 553<clickedY<623):
        modeChosen = "HTP"
        screen.blit(HOWTOPLAY,(0,0))
        pygame.display.update()
        firstClick = True
      
      #user clicked on QUIT button. Ends the program.
      elif modeChosen is False and (324<clickedX<575 and 685<clickedY<756):
        run = False


    #If player has selected the player vs player mode, this section of code interprets what a mouse click relates to. 
    if event.type == pygame.MOUSEBUTTONDOWN and board.gameWon is False and modeChosen == "1V1" and firstClick is False:

      #numberTurn used to determine whether it is the X player or O player's turn
      if numberTurn == -1:
        play.xplayer.move()

        #Only if player clicks on a valid square (An empty square in a board that is allocated to them)
        if play.xplayer.choiceValid is True:
          board.winCheck()
          numberTurn= numberTurn*-1
      
      
      elif numberTurn == 1:
        play.oplayer.move()

        if play.oplayer.choiceValid is True:
          board.winCheck()
          numberTurn= numberTurn*-1

    #If player has selected the player vs smart AI mode, this section of code interprets what a mouse click relates to. 
    elif event.type == pygame.MOUSEBUTTONDOWN and board.gameWon is False and modeChosen == "PVC" and firstClick is False:
      
      if numberTurn == -1 :
        play.xplayer.move()
        if play.xplayer.choiceValid is True:
          board.winCheck()
          numberTurn= numberTurn*-1

    #Section of code where the AI chooses a square.
    if numberTurn == 1 and modeChosen == "PVC" and board.gameWon is False:
      play.oplayer.minimax(board.main,board.bigWins)
      board.winCheck()
      numberTurn= numberTurn*-1

    #If the how to play screen is being displayed, this code allows the user to return to the menu if they click the "RETURN" button
    if event.type == pygame.MOUSEBUTTONDOWN and modeChosen == "HTP" and (324 < clickedX < 576 and 811 < clickedY < 882):
      modeChosen = False

    #Displays a winning or drawing screen if one has been detected
    if board.gameWon is not False:
      if board.gameWon == "O":
        screen.blit(OWINS,(0,0))
        pygame.display.update()
      elif board.gameWon == "X":
        screen.blit(XWINS,(0,0))
        pygame.display.update()
      elif board.gameWon == "DRAW":
        screen.blit(DRAW,(0,0))
        pygame.display.update()

    #When user clicks "RETURN TO MENU" button, this section of code resets the board and returns the user to the menu.
    if event.type == pygame.MOUSEBUTTONDOWN and board.gameWon is not False and (305 < clickedX < 595 and 593 < clickedY < 703):
      modeChosen = False
      board.gameWon = False
      board.reset()
      numberTurn = -1
