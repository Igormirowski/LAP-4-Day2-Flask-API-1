from curses.panel import new_panel
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

players = [
    {'id': 1, 'name': 'Lebron James', 'age': 37},
    {'id': 2, 'name': 'Kevin Durant', 'age': 32},
    {'id': 3, 'name': 'Kyrie Irving', 'age': 30}
]

@app.route('/')
def hello():
    return f"Hello world"

@app.route('/players', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify(players)
    elif request.method == "POST":
        # I want to create a player / Player(data)
        new_player = request.json
        # print("*"*10)
        # print(data)
        # print("*"*10)
        last_id = players[-1]['id'] # access last player id
        new_player['id'] = last_id + 1 
        players.append(new_player)

        # add the player to my list/ add player to your db
        # return "player was created"
        return f"{new_player['name']} was created", 201
  
# Dynamic value / player
@app.route('/player/<int:player_id>')
def shwo(player_id):
    try:
        return next(player for player in players if player['id'] == player_id)
    except:
        # raise BadRequest(f"We do not have player with that id:{player_id}")
        raise Exception(f"We do not have player with that id:{player_id}")



if __name__ == "__main__": 
    app.run()
