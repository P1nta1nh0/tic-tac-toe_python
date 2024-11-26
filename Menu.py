import random
import sys

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True
Option = -1

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
  else:
      print("That spot is already taken")
      playerInput(board)

def checkHorizontal(board):
  global winner
  if board[0] == board[1] == board[2] and board[1] != "-":
    winner = board[0]
    return True
  elif board[3] == board[4] == board[5] and board[3] != "-":
    winner = board[4]
    return True
  elif board[6] == board[7] == board[8] and board[6] != "-":
    winner = board[6]
    return True

def checkVertical(board):
  global winner
  if board[0] == board[3] == board[6] and board[0] != "-":
    winner = board[0]
    return True
  elif board[1] == board[4] == board[7] and board[1] != "-":
    winner = board[0]
    return True
  elif board[2] == board[5] == board[8] and board[2] != "-":
    winner = board[2]
    return True

def checkDiag(board):
  global winner
  if board[0] == board[4] == board[8] and board[0] != "-":
    winner = board[0]
    return True
  elif board[2] == board[4] == board[6] and board[2] != "-":
    winner = board[2]
    return True

def checkEnd():
  global gameRunning
  if (checkDiag(board) or checkHorizontal(board) or checkVertical(board)) and gameRunning == True:
    print(f"The winner is: {winner}")
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
  while currentPlayer == "O":
    if option == 1:
      position = random.randint(0,8)
      if board[position] == "-":
        board[position] = "O"
        switchPlayer()
    elif option == 2:
      pass
    elif option == 3:
      pass

def game(option):
  global gameRunning
  gameRunning = True
  while gameRunning:
    printBoard(board)
    playerInput(board)
    checkEnd()
    switchPlayer()
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

def minimax(minimax_board, depth, is_maximizing):
    if checkEnd(computer, minimax_board):
      return float('inf')
    elif checkEnd(currentPlayer, minimax_board):
      return float('-inf')
    elif checkEnd(minimax_board):
      return 0
    
    if is_maximizing:
      best_score = -1000
      
    else:
      pass