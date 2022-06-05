from flask import Flask, jsonify, render_template, url_for, request
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
    
class Table_hotline(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True, index=True)
    brand = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20))
    url = db.Column(db.String(300))
    def __repr__(self):
        return f'<Table_hotline {self.id} - {self.brand}>' 

def get_menu_items():
    try:
        main_menu = Menu.query.order_by(Menu.priority.asc()).all()
    except Exception as e:
        main_menu = []
    return main_menu

def get_tab_hotlines():
    try:
        tab_hotlines = Table_hotline.query.order_by(Table_hotline.brand.asc()).all()
    except Exception as e:
        tab_hotlines = []
    return tab_hotlines

@app.route('/home')
@app.route('/')
def index():
    main_menu = get_menu_items()
    return render_template("main.html", menu=main_menu)

@app.route('/hot-lines', methods=['GET', 'POST'])
def hot_lines():
    main_menu = get_menu_items()
    
    if request.method == 'GET':
        tab = get_tab_hotlines()
        return render_template("hot-lines.html", menu=main_menu, tab=tab)

    # if post request, then filter table_hotline by brand
    filter_str = request.form.get("filter")
    # val = 'as'
    # print(val)
    if filter_str is None:
        tab = get_tab_hotlines()
    else:
        tab = Table_hotline.query.filter(Table_hotline.brand.ilike('%'+filter_str+'%')).all()
    return render_template("hot-lines.html", menu=main_menu, tab=tab, filter_str=filter_str) #jsonify({"data": {"val": val}})


@app.route('/our-services')
def our_services():
    main_menu = get_menu_items()
    return render_template("our-services.html", menu=main_menu)

@app.route('/kbt')
def kbt():
    main_menu = get_menu_items()
    return render_template("kbt.html", menu=main_menu)

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f'<h1>User {name} - {id}</h1>'

@app.route('/open-chat')
def open_chat():
    main_menu = get_menu_items()
    return render_template("main.html", menu=main_menu, open_chat=True)

if __name__ == '__main__':
    app.run(debug=True)
