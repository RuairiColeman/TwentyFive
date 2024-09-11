class Card:
    # Initialize the Card object with suit, rank, and value
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    # Return a string representation of the card
    def __str__(self):
        return f"{self.rank} of {self.suit}"