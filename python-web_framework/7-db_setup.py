"""web framework flask in progress"""
from flask import Flask request, render_template, flash, redirect, url_for
from flask_sqlalchemy import sqlalchemy
import re
import sys

if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_host = 'localhost'

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URL'] = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = sqlalchemy(app)

    class User(db.Model):
        id =db.Column(db.integer, primary_key=True)
        name = db.Column(db.String(256))
        email = db.Column(db.String(256)), unique=True, nullable=False

    def create_table():
        with app.app_context():
            db.create_all()

    create_tables() #this calls function to create tables

    @app.route('/', strict_slashes=False)
    def index():
        return "Hello, ALX Flask!"
    
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)

