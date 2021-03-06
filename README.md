# Day 2 Flask framework / APi 


## Step by step guide &notes to create API:

- createfile app.py
- copy stuff from [link](https://palletsprojects.com/p/flask/)
```
from flask import Flask, escape, request
app = Flask(__name__)
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!' 
```
- `pipenv shell` (virtual environment) (In case of no access isntall : `pip install pipenv`)
- `pipenv install flask`
- Check name of your virtual environment`pipenv --venv` / `pipenv --where`
- COMMAND + Shift + P : > reload windown
- COMMAND + Shift + P (interpreter pick from link venv(vid22))

- change line 9 to `return f"hello world"`
- `pipenv install --dev pep8 autopep8`
- remove request and escape from import top line 
- add on bottom
```
if __name__ == "__main__": 
    app.run()
```
## Port 5000 issue
- lsof -i:5000
- system preferences --> disable AIrplay Receiver
[link](https://twissmueller.medium.com/resolving-the-problem-of-port-5000-already-being-in-use-dd2fe4bad0be)

# CONTINUE :
- Terminal: `python app.py` (go into link to see)

- `pipenv install gunicorn` (only on MAC) move to production 
[link](https://gunicorn.org/)
- add scripts to pipfile

```
[scripts]
start = "gunicorn app:app"
```
- new file wsgi.py (connect python with web -->gunicorn)
- wsgi.py : 
```
from app import app
if __name__ == "__main__":
    app.run()
```

- `pipenv run start` (see port 8000)
- add dev script: (to use it instead of python app.py)
```
dev = "bash -c \"export FLASK_ENV='development' && flask run\" "
```
- `pipenv run dev`
- Debugger PIN number 776-665-337
- see CRUD routes.md file

## START (setup done)
- create new route `/players`
- add array of cats or players (or any data u want)
- add jsonify
- add create player (instead of creating ne route we `add options` in the same line using method)
- import request


- hoppscotch.io 
-`pipenv install flask-cors` 
- import cors:
```
from flask_cors import CORS

CORS(app)
```
(may need restart server after CORS)
- hoppscotch check if POST working 

- add dynamic player / dynamic valuse
- check `http://localhost:5000/players/1` and try id 6
- add werkzeug BadRequest (replace Exception and import on top!)

- add NotFound(import)


- `pipenv run pip >> requirements.txt` see file 

## USEFUL LINKS
- `https://gunicorn.org/`
- `https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/`
- `https://werkzeug.palletsprojects.com/en/1.0.x/exceptions/?highlight=exceptions#module-werkzeug.exceptions`
- `https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.route`
