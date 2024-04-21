import random
class SnakeAndLadderGame:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.last_dice_values = []
        self.consecutive_sixes = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def roll_two_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)

    def move_player(self, player):
        total_dice_value = self.roll_two_dice()
        if total_dice_value == 12:
            self.consecutive_sixes += 1
        else:
            self.consecutive_sixes = 0

        if self.consecutive_sixes >= 3:
            total_dice_value = 0
            self.consecutive_sixes = 0

        current_position = player.get_position()
        new_position = min(current_position + total_dice_value, self.board.size)
        final_position = self.board.get_position(new_position)
        if final_position:
            player.move(final_position - new_position)
        else:
            player.move(total_dice_value)

        return total_dice_value, current_position, player.get_position()

    def play_game(self):
        current_player_index = 0
        while len(self.players) > 1:
            player = self.players[current_player_index]
            dice_value, initial_position, final_position = self.move_player(player)
            print(f"{player.name} rolled a {dice_value} and moved from {initial_position} to {final_position}")
            if final_position >= self.board.size:
                final_position = self.board.size
                print(f"{player.name} wins the game")
                self.players.remove(player)
                if len(self.players) == 1:
                    print(f"{self.players[0].name} wins the game!")
                    return
            if dice_value == 12:
                print(f"{player.name} rolled a 12 and gets an extra turn.")
            else:
                current_player_index = (current_player_index + 1) % len(self.players)
                self.consecutive_sixes = 0
