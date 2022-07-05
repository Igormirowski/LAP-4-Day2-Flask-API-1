# Day 2 Flask framework / APi 



- file app.py
- copy stuff from https://palletsprojects.com/p/flask/

from flask import Flask, escape, request
app = Flask(__name__)
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'m 

- `pipenv shell` (virtual environment) (In case of no access isntall : `pip install pipenv`)
- `pipenv install flask`
- Check name of your virtual environment`pipenv --venv` / `pipenv --where`
- COMMAND + Shift + P : > reload windown
- COMMAND + Shift + P (interpreter pick from link venv(vid22))

- change line 9 to `return f"hello world"`
- `pipenv install --dev pep8 autopep8`
- remove request and escape 
- add if __name__ == "__main__": app.run()
- Terminal: python app.py (go into link to see)


- `pipenv install gunicorn` (only on MAC)
- `https://gunicorn.org/`
- add scripts to pipfile
[scripts]
start = "gunicorn app:app"

- new file wsgi.py (connect python with web -->gunicorn)
- wsgi.py : 
from app import app
if __name__ == "__main__":
    app.run()

- `pipenv run start`
- add dev scriptdev = "bash -c \"export FLASK_ENV='development' && flask run\" "
- `pipenv run dev`
- Debugger PIN number 776-665-337
- copy and paste CRUD routes.md
-

MORE !!!!!!!!!:
23mis15s comand shift P 


- hoopscotch.io 
-`pipenv install flask-cors` (may need restart server)




- pipenv run start (port 8000)
- pipenv run pip freeze >> requirements.txt (TO CHHECK !!!)
## USEFUL LINKS
- `https://gunicorn.org/`
- `https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/`
- `https://werkzeug.palletsprojects.com/en/1.0.x/exceptions/?highlight=exceptions#module-werkzeug.exceptions`
