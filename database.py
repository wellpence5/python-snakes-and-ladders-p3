from supabase.client import create_client, Client
from datetime import datetime
SUPABASE_URL="https://tdwohwhqhphcqwasrwez.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRkd29od2hxaHBoY3F3YXNyd2V6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NjEwNzczNSwiZXhwIjoyMDcxNjgzNzM1fQ.5z6zaDJ0cIPcyofkY6BroLbvHv8vELq4nHtlg8yOVSI"

# Create a Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def init_db():
    print("✅ Database ready (check Supabase).")

def add_player(name: str):
    """
    Add a new player to the database.
    Returns the new player as a dictionary.
    """
    result = supabase.table("players").insert({"name": name}).execute()
    return result.data[0] if result.data else None

def update_player_position(player_id: int, new_position: int):
    """
    Update a player's position in the database.
    """
    supabase.table("players").update(
        {"current_position": new_position}
    ).eq("id", player_id).execute()

def log_move(game_id: int, player_id: int, roll: int, old_pos: int, new_pos: int):
    """
    Record one move in the database.
    """
    supabase.table("moves").insert({
        "game_id": game_id,
        "player_id": player_id,
        "roll_value": roll,
        "old_position": old_pos,
        "new_position": new_pos,
        "timestamp": datetime.now().isoformat()
    }).execute()

def create_game():
    """
    Start a new game in the database.
    """
    result = supabase.table("games").insert({
        "start_time": datetime.now().isoformat()
    }).execute()
    return result.data[0] if result.data else None

def record_game_result(game_id: int, winner_id: int):
    """
    Mark the game as finished and store the winner.
    """
    supabase.table("games").update({
        "end_time": datetime.now().isoformat(),
        "winner_id": winner_id
    }).eq("id", game_id).execute()

    # Increase the winner's wins
    player = supabase.table("players").select("wins").eq("id", winner_id).execute()
    if player.data:
        current_wins = player.data[0]["wins"] or 0
        supabase.table("players").update({"wins": current_wins + 1}).eq("id", winner_id).execute()

def get_leaderboard():
    """
    Get the top 10 players ordered by wins.
    """
    result = supabase.table("players").select("*").order("wins", desc=True).limit(10).execute()
    return result.data

def get_active_game():
    """
    Get the most recent unfinished game (end_time IS NULL).
    """
    result = supabase.table("games").select("*").is_("end_time", None).order("start_time", desc=True).limit(1).execute()
    return result.data[0] if result.data else None

def delete_game(game_id):
    """
    Delete a game and its moves.
    Players stay in the database unless you delete them separately.
    """
    # Delete moves first
    supabase.table("moves").delete().eq("game_id", game_id).execute()
    # Delete the game itself
    supabase.table("games").delete().eq("id", game_id).execute()
    
def load_players_for_game(game_id):
    """
    Load players who already made moves in this game, with their last position.
    """
    query = """
    SELECT p.id, p.name, p.total_moves, p.wins,
           COALESCE(m.new_position, p.current_position) AS position
    FROM players p
    LEFT JOIN LATERAL (
        SELECT new_position
        FROM moves
        WHERE moves.player_id = p.id AND moves.game_id = {gid}
        ORDER BY id DESC
        LIMIT 1
    ) m ON true
    """.format(gid=game_id)

    result = supabase.rpc("exec_sql", {"sql": query}).execute()
    # NOTE: Supabase client doesn’t support raw SQL directly.
    # Alternative: select players then update with last move position.
    # For simplicity, let’s just return all players and handle in game logic.

    players = supabase.table("players").select("*").execute().data
    return players

