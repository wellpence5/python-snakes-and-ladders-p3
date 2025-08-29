from supabase.client import create_client, Client
from datetime import datetime
SUPABASE_URL="https://tdwohwhqhphcqwasrwez.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRkd29od2hxaHBoY3F3YXNyd2V6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NjEwNzczNSwiZXhwIjoyMDcxNjgzNzM1fQ.5z6zaDJ0cIPcyofkY6BroLbvHv8vELq4nHtlg8yOVSI"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#database Setup
def init_db():
    print("Database ready. Powered by Supabase (Loading...).")

#players
def add_player(name):
    #add player if not already in database,otherwise return existing player
    #try to fetch the player first
    result = supabase.table("players").select("*").eq("name", name).execute()
    if result.data:
        return result.data[0]#player already exists,return it
    result = supabase.table("players").insert({"name": name}).execute()#otherwise insert new player
    return result.data[0]

def update_player_position(player_id: int, new_position: int):
    #Update a player position and increase their total moves.
    # First get current total_moves
    player = supabase.table("players").select("total_moves").eq("id", player_id).execute()
    total_moves = player.data[0]["total_moves"] if player.data else 0
    #update both position and total_moves
    supabase.table("players").update({
        "current_position": new_position,
        "total_moves": total_moves + 1
    }).eq("id", player_id).execute()

#moves
def log_move(game_id: int, player_id: int, roll: int, old_pos: int, new_pos: int):
    #Record one move in the moves table.
    #Each move is tied to a game and a player.
    supabase.table("moves").insert({
        "game_id": game_id,
        "player_id": player_id,
        "roll_value": roll,
        "old_position": old_pos,
        "new_position": new_pos,
        "timestamp": datetime.now().isoformat()
    }).execute()

#games
def create_game():
    #Start a new game in the database.
    result = supabase.table("games").insert({
        "start_time": datetime.now().isoformat()
    }).execute()
    return result.data[0] if result.data else None

def record_game_result(game_id: int, winner_id: int):
    #Mark the game as finished, set the winner, and
    #increase the winner’s total wins.
    # Mark the game as ended
    supabase.table("games").update({
        "end_time": datetime.now().isoformat(),
        "winner_id": winner_id
    }).eq("id", game_id).execute()
    #increase the winner wins
    player = supabase.table("players").select("wins").eq("id", winner_id).execute()
    if player.data:
        current_wins = player.data[0]["wins"] or 0
        supabase.table("players").update({"wins": current_wins + 1}).eq("id", winner_id).execute()

def get_active_game():
    #Return the most recent unfinished game(where end_time is still NULL cause how else would we know its unfinished).
    result = supabase.table("games").select("*")\
        .is_("end_time", "null")\
        .order("start_time", desc=True)\
        .limit(1)\
        .execute()
    return result.data[0] if result.data else None

def delete_game(game_id: int):
    #Delete a game and all of its moves.
    #(Players stay in the database.)
    supabase.table("moves").delete().eq("game_id", game_id).execute()
    supabase.table("games").delete().eq("id", game_id).execute()

def reset_all():
    #Reset the entire database:
    supabase.table("moves").delete().neq("id", 0).execute()
    supabase.table("games").delete().neq("id", 0).execute()
    supabase.table("players").update({
        "current_position": 0,
        "total_moves": 0,
        "wins": 0
    }).neq("id", 0).execute()

#stats
def get_leaderboard():
    result = supabase.table("players").select("*")\
        .order("wins", desc=True)\
        .limit(10)\
        .execute()
    return result.data


def load_players_for_game(game_id: int):
    players = supabase.table("players").select("*").execute().data or []

    for p in players:
        #Get the last move this player made in this game
        moves = supabase.table("moves").select("new_position")\
            .eq("player_id", p["id"]).eq("game_id", game_id)\
            .order("id", desc=True).limit(1).execute()

        if moves.data:
            p["current_position"] = moves.data[0]["new_position"]

    return players

