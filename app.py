from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dfnj100gPG@localhost/sitebot.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = '&*(%&$^$&%*&(^(*&%^$&*5978539487JKHGgdsuyrh'

db = SQLAlchemy(app)


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True, index=True)
    name = db.Column(db.String(30), nullable=True)
    path = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return '<Menu Item %r - %r - %r>' % self.id, self.name, self.path

main_menu = [{'name':'Главная', 'path': '/'}, 
             {'name':'О нас', 'path': 'about'}]


@app.route('/home')
@app.route('/')
def index():
    try:
        main_menu = Menu.query.all() 
        
    except Exception as e:
        main_menu = []
    
    return render_template("main.html", menu=main_menu)


@app.route('/about')
def about():
    return render_template("about.html", menu=main_menu)


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f'<h1>User {name} - {id}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
