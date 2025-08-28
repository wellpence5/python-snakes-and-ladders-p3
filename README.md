# 🎲 Snakes and Ladders – Turn Manager

This module (`TurnManager`) handles **game state and turn management** for our Snakes and Ladders project.  
It manages dice rolls, player turns, movement across the board, and win condition detection.

---

## 📂 Features
- Roll a dice (1–6).
- Track each player's current position.
- Rotate turns automatically.
- Count total moves taken.
- Detect when a player wins (reaches or passes position 100).
- Easily extendable with database integration for saving moves and winners.

---

## 🛠️ Code Overview
### `TurnManager` Class
- **Attributes**
  - `players`: list of players.
  - `current_turn`: index of whose turn it is.
  - `positions`: dictionary mapping player → board position.
  - `moves_count`: number of moves so far.
  
- **Methods**
  - `roll_dice()`: returns a random dice value between 1–6.
  - `play_turn()`:  
    - Rolls the dice.  
    - Updates the current player’s position.  
    - Prints the result.  
    - Checks for a winner.  
    - Rotates to the next player.  
    - Returns `True` if game is over, otherwise `False`.

### `run_game(players)` Function
Runs the game loop until a winner is found.

---

## ▶️ How to Run
1. Clone the repository and open the project.
2. Run the script:
   ```bash
   python3 main.py
