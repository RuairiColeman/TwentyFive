from flask import Flask, request, jsonify
from Deck import Deck
from Player import Player
from Rules import Rules

app = Flask(__name__)

# Initialize the deck and shuffle
deck = Deck()
deck.shuffle()
players = []
rules = None

# Create players by prompting for their names
@app.route('/create_players', methods=['POST'])
def create_players():
    global players, rules
    player_names = request.json['player_names']
    players = [Player(name) for name in player_names]
    rules = Rules(players)
    return jsonify({"message": "Players created", "players": player_names})

@app.route('/deal_cards', methods=['POST'])
def deal_cards():
    for _ in range(5):
        for player in players:
            player.draw_card(deck)
    
    # Display the trump card immediately after dealing the hands
    trump_card = rules.display_trump_card()
    
    # Handle the Ace scenario
    if trump_card.rank == 'Ace':
        rules.deals_ace(trump_card)
    elif rules.check_ace_of_trump(trump_card):
        return jsonify({"message": f"{player.name}'s hand: {player.show_hand()}"})
    
    return jsonify({"message": "Cards dealt and trump card displayed", "trump_card": str(trump_card)})

@app.route('/display_trump_card', methods=['GET'])
def display_trump_card():
    trump_card = rules.display_trump_card()
    return jsonify({"trump_card": str(trump_card)})

@app.route('/show_hands', methods=['GET'])
def show_hands():
    hands = {player.name: player.show_hand() for player in players}
    return jsonify(hands)

@app.route('/play_game', methods=['POST'])
def play_game():
    rules.play_game()
    scores = {player.name: player.score for player in players}
    return jsonify({"message": "Game played", "scores": scores})

@app.route('/rotate_dealer', methods=['POST'])
def rotate_dealer():
    rules.rotate_dealer()
    return jsonify({"new_dealer": rules.get_dealer().name})

if __name__ == "__main__":
    app.run(debug=True)