Snakes and Ladders CLI (with Supabase Database)
A command-line Snakes and Ladders game built with Python, backed by Supabase for persistent storage of players, moves, and game history.
This project supports saving and resuming games, tracking leaderboards, and managing players.


--Features
play Snakes & Ladders in the terminal
Save game progress automatically (resume unfinished games)
Track player stats:
    Wins
    Total moves
    Current position
    View leaderboard (Top 10 players by wins)
    Delete unfinished games or reset the entire database

--Tech Stac
Python 3.9+
Supabase (PostgreSQL backend)
supabase-py client for database interactions


--Project Structure
.
├── main.py          # CLI entry point
├── game_logic.py    # Dice rolling, movement, snakes/ladders logic
├── database.py      # Supabase database interactions
├── README.md        # Documentation

Setup Instructions
1.Clone Repository
git clone https://github.com/your-username/snakes-ladders-supabase.git
cd snakes-ladders-supabase

2. Install Dependencies
pip install supabase

3. Configure Supabase
Update your Supabase credentials inside database.py:

SUPABASE_URL = "your-project-url"
SUPABASE_KEY = "your-service-role-key"


--Running the Game
Start the CLI with:
    python main.py

