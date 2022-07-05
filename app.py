from flask import Flask

app = Flask(__name__)

players = [
    {'id': 1, 'name': 'Lebron James', 'age': 37},
    {'id': 2, 'name': 'Kevin Durant', 'age': 32},
    {'id': 3, 'name': 'Kyrie Irving', 'age': 30}
]

@app.route('/')
def hello():
    return f"Hello world"

@app.route('/players')
def index():
    return f"Hello world"

if __name__ == "__main__": 
    app.run()
