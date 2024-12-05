import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
gameRunning = True
Option = -1
AllLines = None

def printBoard(board):
  print(board[0] + "|" + board[1] + "|" + board[2])
  print("__________")
  print(board[3] + "|" + board[4] + "|" + board[5])
  print("__________")
  print(board[6] + "|" + board[7] + "|" + board[8])

def playerInput(board):
  inp = int(input("Enter a number 1-9: "))
  if inp >= 1 and inp <= 9 and board[inp-1] == "-":
      board[inp-1] == "-"
      board[inp-1] = currentPlayer
      updateAllLines()
      switchPlayer()
  else:
      print("That spot is already taken")
      playerInput(board)

def updateAllLines():
  global AllLines
  line1 = [board[0], board[1], board[2]]
  line2 = [board[3], board[4], board[5]]
  line3 = [board[6], board[7], board[8]]
  line4 = [board[0], board[3], board[6]]
  line5 = [board[1], board[4], board[7]]
  line6 = [board[2], board[5], board[8]]
  line7 = [board[0], board[4], board[8]]
  line8 = [board[2], board[4], board[6]]

  AllLines = [line1, line2, line3, line4, line5, line6, line7, line8]

def checkEndAUX(player):
  global AllLines
  for line in AllLines:
    numberOfChecks = 0
    for space in line:
      if space == player:
        numberOfChecks += 1      
    if numberOfChecks == 3:
      return True
  return False

def checkRow_Play(player):
  global AllLines
  rowNumber = 0
  openSpace = [0,0]
  storeEmptySpaces = []
  for row in AllLines:
    numberOfChecks = 0
    spaceNumber = 0
    for space in row:
      if space == player:
        numberOfChecks += 1
      elif space == "-":
        openSpace = [rowNumber, spaceNumber]
        storeEmptySpaces.append(arrayToNumber(openSpace))
      spaceNumber += 1
    if numberOfChecks == 2:
      return [arrayToNumber(openSpace),True]
    rowNumber += 1
  return [random.choice(storeEmptySpaces),False]

def arrayToNumber(array):
  if array[0] == 0:
    return array[1]
  
  if array[0] == 1:
    return array[1] + 3
  
  if array[0] == 2:
    return array[1] + 6
  
  if array[0] == 3:
    return array[1] * 3
  
  if array[0] == 4:
    return array[1] * 3 + 1
  
  if array[0] == 5:
    return array[1] * 3 + 2
  
  if array[0] == 6:
    return array[1] * 4
  
  if array[0] == 7:
    return array[1] * 2 + 2

def checkEnd():
  global gameRunning
  if gameRunning == True:
    if checkEndAUX("X"):
      printBoard(board)
      print("The winner is: X")
      gameRunning = False
    elif checkEndAUX("O"):
      printBoard(board)
      print("The Winner is: O")
      gameRunning = False
  elif "-" not in board:
    printBoard(board)
    print("It's a tie")
    gameRunning = False

def switchPlayer():
  global currentPlayer
  if currentPlayer == "X":
    currentPlayer = "O"
  else:
    currentPlayer = "X"

def computer(board, option):
  global currentPlayer
  while currentPlayer == "O":
    oppositePlayer = "X"
    if option == 1:
      position = random.randint(0,8)
      if board[position] == "-":
        board[position] = "O"
        switchPlayer()
    elif option == 2:
      result = checkRow_Play(currentPlayer)
      if result[1] == False:
        result = checkRow_Play(oppositePlayer)
      if board[result[0]] == "-":
        board[result[0]] = "O"
        switchPlayer()
    elif option == 3:
      pass
    updateAllLines()

def game(option):
  global gameRunning
  gameRunning = True
  while gameRunning:
    printBoard(board)
    playerInput(board)
    checkEnd()
    computer(board, option)
    checkEnd()
  playAgain()

def playAgain():
  global board, gameRunning
  board = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]
  print("Would you like to play again?")
  pAgain = input("(Y) or (N): ")
  if pAgain == "Y":
    global Option
    game(Option)
  elif pAgain != "N":
    print("Invalid Option")
    playAgain()

def opening():
  global Option
  print("TIC TAC TOE GAME\nChoose an option: \n")

  print("1 -- Easy")
  print("2 -- Medium")
  print("3 -- Hard")
  print("4 -- Check previous results")
  print("5 -- Rules")
  print("0 -- Exit game")  
  Option = int(input("Enter an option: "))

while Option != 0:
  opening()
  if 1 <= Option <= 3:
    game(Option)
  elif Option == 4:
      pass
  elif Option == 5:
      print("\nThe game is played on a 3x3 grid\n"
            "First the Player chooses X or O to be their symbol\n"
            "Then it's chosen randomly who starts the game\n"
            "When the game starts the objective is to be the first to align three of your symbols, vertically, horizontally or diagonally\n"
            "If all squares are filled and neither player has aligned three symbols, the game is a draw.\n")
print("Thanks for playing, see you next time!")