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
    title = db.Column(db.String(30), nullable=False)
    ref = db.Column(db.String(300))
    priority = db.Column(db.Integer)
    handler = db.Column(db.String(20))
    ext_title = db.Column(db.String(80))
    intro = db.Column(db.String(300))
    icon_svg_name = db.Column(db.String(20))

    def __repr__(self):
        return '<Menu Item %r - %r - %r>' % self.id, self.name, self.path



@app.route('/home')
@app.route('/')
def index():
    try:
        main_menu = Menu.query.order_by(Menu.priority.asc()).all()
    except Exception as e:
        print(e)
        main_menu = []
    return render_template("main.html", menu=main_menu)

@app.route('/hot-lines')
def hot_lines():
    return render_template("hot-lines.html")

@app.route('/our-services')
def our_services():
    return render_template("our-services.html")

@app.route('/kbt')
def kbt():
    return render_template("kbt.html")

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f'<h1>User {name} - {id}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
