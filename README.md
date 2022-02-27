// pipenv
MAC: pipenv shell
WINDOWS: python3 -m pipenv shell

run app: python app.py

// set environment
MAC: export FLASK_ENV=development
WINDOWS: set FLASK_ENV=development
flask run

// Flask-SQLAlchemy
flask db init
flask db migrate
flask db upgrade

flask db init
flask db migrate
flask db upgrade
heroku stack:set container
pipenv install waitress
pipenv lock -r > requirements.txt