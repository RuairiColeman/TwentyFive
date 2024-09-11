import random
from Card import Card

# Define the suits and ranks for the cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
}

class Deck:
    def __init__(self):
        # Initialize the deck with 52 cards (one for each combination of suit and rank)
        self.cards = [Card(suit, rank, value) for suit in suits for rank, value in ranks.items()]

    def shuffle(self):
        # Shuffle the deck of cards
        random.shuffle(self.cards)

    def deal_one(self):
        # Deal one card from the deck
        return self.cards.pop()