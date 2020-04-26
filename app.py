import os
from flask import Flask
from models import setup_db
from flask_cors import CORS
"""notes for testing localy 
1)you must have the environment vars on the .bashrc file or just on the running terminal
look here for more info https://linuxhint.com/bash-environment-variables/
2)add migration in the models.py file 
3)in testing the project for har
run those command in python3
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
"""

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
