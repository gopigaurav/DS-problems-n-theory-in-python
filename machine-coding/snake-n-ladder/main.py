from board import Board
from player import Player
import unittest

def play_game():
    board = Board()
    players = [Player("Player 1"), Player("Player 2"), Player("Player 3")]
    done = [0, 0, 0]
    winner = None
    left_out = None
    left_out_players = len(players)

    while left_out_players > 1:
        for i, player in enumerate(players):
            if not done[i]:
                dice_roll = player.roll_dice()
                print(f"{player.name} rolled a {dice_roll}")
                player.move(dice_roll)
                player.position = board.check_snake_or_ladder(player.position)
                print(f"{player.name} is now at position {player.position}\n")
                if player.position == 100:
                    done[i] = 1
                    left_out_players -= 1
                    print(f"Congratulations, {player.name} wins!")
                    input(f"Congratulations, {player.name} wins!.")

                    if len(players) == 1:
                        break
        
    print(done)


class TestStringMethods(unittest.TestCase):
    pass

if __name__ == "__main__":
    play_game()
