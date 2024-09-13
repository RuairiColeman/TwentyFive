from Deck import Deck
from Player import Player

class Rules:
    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.dealer_index = 0  # Start with the first player as the dealer
        self.scores = {player.name: 0 for player in players}  # Initialize scores

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

    def check_ace_of_trump(self, trump_card):
        # Check if any player has the Ace of the trump suit at the start of their first turn
        for player in self.players:
            for card in player.hand:
                if card.rank == 'Ace' and card.suit == trump_card.suit:
                    print(f"{player.name} has the Ace of {trump_card.suit} in their hand.")
                    print(f"{player.name}'s hand: {player.show_hand()}")
                    while True:
                        card_to_surrender = input(f"{player.name}, choose a card to surrender: ")
                        for card in player.hand:
                            if str(card) == card_to_surrender:
                                player.hand.remove(card)
                                player.hand.append(trump_card)
                                print(f"{player.name} surrendered the {card_to_surrender}.")
                                print(f"{player.name} stole {trump_card.rank} of {trump_card.suit}.")
                                return True
                        print("Invalid card. Please choose a card from your hand.")
        return False

    def play_turn(self, player):
        # Player plays one card from their hand
        print(f"{player.name}'s turn. Hand: {player.show_hand()}")
        while True:
            card_to_play = input(f"{player.name}, choose a card to play: ")
            for card in player.hand:
                if str(card) == card_to_play:
                    player.hand.remove(card)
                    print(f"{player.name} played the {card_to_play}.")
                    return card
            print("Invalid card. Please choose a card from your hand.")

    def determine_winner(self, cards_played):
        # Determine the winner of the lift based on the rules
        highest_card = None
        winner = None
        for player, card in cards_played.items():
            if highest_card is None or self.compare_cards(card, highest_card):
                highest_card = card
                winner = player
        return winner

    def compare_cards(self, card1, card2):
        # Compare two cards based on the rules
        if card1.suit == card2.suit:
            if card1.rank in ['K', 'Q', 'J'] and card2.rank in ['K', 'Q', 'J']:
                return card1.rank > card2.rank
            elif card1.rank.isdigit() and card2.rank.isdigit():
                if card1.suit in ['Hearts', 'Diamonds']:
                    return int(card1.rank) > int(card2.rank)
                else:
                    return int(card1.rank) < int(card2.rank)
            else:
                return card1.rank > card2.rank
        else:
            return False

    def play_game(self):
        # Main game loop
        starting_player_index = 0
        while any(player.hand for player in self.players):
            cards_played = {}
            for i in range(len(self.players)):
                player = self.players[(starting_player_index + i) % len(self.players)]
                if player.hand:
                    card = self.play_turn(player)
                    cards_played[player] = card
            winner = self.determine_winner(cards_played)
            self.scores[winner.name] += 5
            print(f"{winner.name} wins the lift and now has {self.scores[winner.name]} points.")
            if self.scores[winner.name] >= 25:
                print(f"{winner.name} wins the game!")
                return
            starting_player_index = self.players.index(winner)
        print("Game over! All cards have been played.")
