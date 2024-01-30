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

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = sqlalchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(256))
        email = db.Column(db.String(256), unique=True, nullable=False)

    def create_table():
        with app.app_context():
            db.create_all()

    create_tables() #this calls function to create tables

    @app.route('/add_user', methods=['GET', 'POST'])
    def add_user():
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')

            try:
                new_user = User(name=name, email=email)
                db.session.add(new_user)
                db.session.commit()
                flash("User added succefully!", "success")
            except Exception as e:
                db.session.rollback()
                flash(f"Error adding user: {str(e)}", "error")

            return render_template('add_user.html')
    
    @app.route('/users')
    def users():
        users_list = User.query.all()
        return render_template('users.html', users=users_list)

    
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)

