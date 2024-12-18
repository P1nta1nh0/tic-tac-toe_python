# Tic Tac Toe Game with Difficulty Levels

This is a Python-based Tic Tac Toe game that allows a player to compete against an AI-controlled opponent with adjustable difficulty levels. The game also maintains a record of previous results in an XML database.

---

## Features

1. **Interactive Tic Tac Toe**: Play against an AI in a traditional 3x3 Tic Tac Toe grid.
2. **Difficulty Levels**: Choose between Easy (random AI moves) and Medium (AI uses basic strategy).
3. **Result Storage**: Tracks game results in an XML database for review later.
4. **Custom Rules Page**: Learn the rules of Tic Tac Toe in-game.
5. **Replay Functionality**: Play multiple rounds without restarting the program.

---

## How It Works

### Game Modes
1. **Easy (Option 1)**: The AI makes random moves.
2. **Medium (Option 2)**: The AI prioritizes blocking the player’s winning move and creating opportunities to win.

### User Interface
- The grid is displayed as a 3x3 board using text.
- The user inputs a number (1-9) to place their marker on the corresponding cell.
- AI moves are displayed automatically.

---

## XML-Based Database
The game maintains results (win, loss, or tie) and difficulty levels in an XML file (`Database.xml`). Each game's result is saved with:
- **Result**: Victory, Defeat, or Tie.
- **Difficulty**: Corresponding difficulty level of the match.

---

## How to Play

1. **Choose Difficulty**:
   - The game begins with an options menu:
     - `1`: Easy Mode
     - `2`: Medium Mode
     - `4`: View Previous Results
     - `5`: Display Game Rules
     - `0`: Exit the Game

2. **Player's Turn**:
   - Enter a number between `1-9` to place your marker (`X`) on the grid.

3. **AI's Turn**:
   - The AI makes a move based on the selected difficulty.

4. **Winning Conditions**:
   - Align three of your symbols (`X`) vertically, horizontally, or diagonally.

5. **Endgame**:
   - The game ends when either the player or AI wins, or the board is full (resulting in a tie).
   - Results are stored in `Database.xml`.

