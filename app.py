from flask import Flask, render_template, url_for
import os

app = Flask(__name__)
main_menu = [{'name':'Главная', 'path': '/'}, 
             {'name':'О нас', 'path': 'about'}]

@app.route('/')
@app.route('/home')
def index():
    
    return render_template("main.html", menu=main_menu)


@app.route('/about')
def about():
    return render_template("about.html", menu=main_menu)


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f'<h1>User {name} - {id}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
