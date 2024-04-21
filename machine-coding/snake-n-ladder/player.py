import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move(self, steps):
        if self.position + steps > 100:
            print("Player cannot go more than 100")
            return
        else:      
            self.position += steps

