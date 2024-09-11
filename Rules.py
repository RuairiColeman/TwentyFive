from Deck import Deck
from Player import Player

class Rules:
    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.dealer_index = 0  # Start with the first player as the dealer

    def get_dealer(self):
        return self.players[self.dealer_index]

    def rotate_dealer(self):
        # Rotate the dealer to the next player
        self.dealer_index = (self.dealer_index + 1) % len(self.players)

    def display_trump_card(self):
        # Draw the next card from the deck to be the trump card
        self.deck.shuffle()
        trump_card = self.deck.deal_one()
        print(f"Trumps: {trump_card}")
        return trump_card

    def deals_ace(self, trump_card):
        dealer = self.get_dealer()
        # Check if the trump card is an Ace and give it to the dealer
        if trump_card.rank == 'Ace':
            # Add the trump card to the dealer's hand
            dealer.hand.append(trump_card)
            print(f"{dealer.name} (dealer) receives the Ace of {trump_card.suit} as the trump card.")

            # Prompt the dealer to surrender a card
            print(f"{dealer.name}'s hand: {dealer.show_hand()}")
            while True:
                card_to_surrender = input(f"{dealer.name}, choose a card to surrender: ")
                for card in dealer.hand:
                    if str(card) == card_to_surrender:
                        dealer.hand.remove(card)
                        # for testing purposes, players wont know what card the dealer surrendered
                        print(f"{dealer.name} surrendered the {card_to_surrender}.")
                        return
                print("Invalid card. Please choose a card from your hand.")