from flask import Flask, jsonify

app = Flask(__name__)

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
        pass
  

if __name__ == "__main__": 
    app.run()
