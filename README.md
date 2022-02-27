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

heroku login
heroku create ...
flask db init
flask db migrate
flask db upgrade
heroku stack:set container or heroku stack:set heroku-20
pipenv install waitress
pipenv lock -r > requirements.txt