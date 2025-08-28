import random
# import database  # Alvin's module (commented out for now)

class TurnManager:
    def __init__(self, players):
        self.players = players
        self.current_turn = 0
        self.positions = {player: 0 for player in players}
        self.moves_count = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def play_turn(self):
        player = self.players[self.current_turn]
        dice_value = self.roll_dice()
        self.positions[player] += dice_value
        self.moves_count += 1

        print(f"{player} rolled a {dice_value} → moved to {self.positions[player]}")

        # database.save_move(player, self.positions[player], dice_value)

        if self.positions[player] >= 100:
            print(f"🎉 {player} wins the game in {self.moves_count} moves!")
            # database.save_winner(player, self.moves_count)
            return True

        self.current_turn = (self.current_turn + 1) % len(self.players)
        return False


def run_game(players):
    manager = TurnManager(players)
    game_over = False

    while not game_over:
        game_over = manager.play_turn()
