from Deck import Deck
from Player import Player

def main():
    # Initialize the deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # Create players by prompting for their names
    player1 = Player(input("Enter player 1's name: "))
    player2 = Player(input("Enter player 2's name: "))
    player3 = Player(input("Enter player 3's name: "))

    # List of player names
    player_names = [player1.name, player2.name, player3.name]

    # Initialize players using the names provided
    players = [Player(name) for name in player_names]

    # Deal 5 cards to each player
    for _ in range(5):
        for player in players:
            player.draw_card(deck)

    # Display each player's hand
    for player in players:
        print(f"{player.name}'s hand: {player.show_hand()}")

if __name__ == "__main__":
    main()