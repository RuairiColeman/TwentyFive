class Player:
    def __init__(self, name):
        # Initialize the Player object with a name and an empty hand
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        # Draw a card from the deck and add it to the player's hand
        self.hand.append(deck.deal_one())

    def show_hand(self):
        # Return a string representation of the player's hand
        return ', '.join(str(card) for card in self.hand)