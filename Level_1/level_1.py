"""
level_1.py

This is level 1 of Escape Code, an escape room style coding game.
Difficulty level: easy


Your mission is to debug the following code to get the password to unzip
the files for the next level.  

Hint: The intended output should show 10 numbers, but it shows only 5.

Good luck!

Author: Naser Al Madi
Date: May 11, 2024

"""

import random

# Set the seed for reproducibility
random.seed(42)


class Deck:
    """
    A class to represent a deck of cards.
    """

    def __init__(self):
        self.cards = []

        for num in range(10):
            self.cards.append(num)

    def shuffle(self):
        """
        Shuffle the numbers in the list.
        """

        shuffled = []

        i = 0
        while i < len(self.cards):
            index = random.randint(0, len(self.cards) - 1)
            shuffled.append(self.cards[index])
            self.cards.pop(index)
            i += 1

        self.cards = shuffled

    def __str__(self):
        """
        Return a string representation of the deck.
        """

        return str(self.cards)


def main():
    """
    This function creates a deck of cards, shuffles them.
    """

    deck = Deck()
    deck.shuffle()
    # copy the entire password including the square brackets and commas
    print("Level_2 password is:", deck)


if __name__ == "__main__":
    main()
