import random
import sys

print("TIC TAC TOE GAME\nChoose an option:\n1-- Easy\n2-- Medium\n3-- Hard\n4-- Check previous results\n5-- Rules\n6-- Exit Game")

letter = int(input())

if letter == 1:
 
 def whoGoesFirst():

      # Randomly choose the player who goes first.

      if random.randint(0, 1) == 0:

         print("The Computer goes first")
         return 'computer'
      
      else:

          print("The Player goes first")
          return 'player'

 def inputPlayerLetter():

     # Lets the player type which letter they want to be.
     letter = ''

     while not (letter == 'X' or letter == 'O'):
         print('Do you want to be X or O?')
         letter = input().upper()

     # the first element in the list is the player’s letter, the second is the computer's letter.
     if letter == 'X':
         return ['X', 'O']
     else:
         return ['O', 'X']
     

 def drawBoard(board):

     print('   |   |')
     print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
     print('   |   |')
if letter == 2:
  def whoGoesFirst():

      # Randomly choose the player who goes first.

      if random.randint(0, 1) == 0:

         print("The Computer goes first")
         return 'computer'
      
      else:

          print("The Player goes first")
          return 'player'

  def inputPlayerLetter():

     # Lets the player type which letter they want to be.
     letter = ''

     while not (letter == 'X' or letter == 'O'):
         print('Do you want to be X or O?')
         letter = input().upper()

     # the first element in the list is the player’s letter, the second is the computer's letter.
     if letter == 'X':
         return ['X', 'O']
     else:
         return ['O', 'X']
     

  def drawBoard(board):

     print('   |   |')
     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
     print('   |   |')
if letter == 3:
  def whoGoesFirst():

      # Randomly choose the player who goes first.

      if random.randint(0, 1) == 0:

         print("The Computer goes first")
         return 'computer'
      
      else:

          print("The Player goes first")
          return 'player'

  def inputPlayerLetter():

     # Lets the player type which letter they want to be.
     letter = ''

     while not (letter == 'X' or letter == 'O'):
         print('Do you want to be X or O?')
         letter = input().upper()

     # the first element in the list is the player’s letter, the second is the computer's letter.
     if letter == 'X':
         return ['X', 'O']
     else:
         return ['O', 'X']
     

  def drawBoard(board):

     print('   |   |')
     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
     print('   |   |')
if letter == 4:
    print
if letter == 5:
    print
if letter == 6:
  sys.exit()