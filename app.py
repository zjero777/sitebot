from flask import Flask, jsonify, redirect, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import re
from feedback import FeedbackForm
from flask_mail import Mail, Message



app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
mail = Mail(app)



class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   nullable=False, unique=True, index=True)
    title = db.Column(db.String(30), nullable=False)
    ref = db.Column(db.String(300))
    priority = db.Column(db.Integer)
    handler = db.Column(db.String(20))
    ext_title = db.Column(db.String(80))
    intro = db.Column(db.String(300))
    icon_svg_name = db.Column(db.String(20))
    button_text = db.Column(db.String(80))

    def __repr__(self):
        return '<Menu Item %r - %r - %r>' % self.id, self.name, self.path


class Table_hotline(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   nullable=False, unique=True, index=True)
    brand = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20))
    url = db.Column(db.String(300))

    def __repr__(self):
        return f'<Table_hotline {self.id} - {self.brand}>'

class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   nullable=False, unique=True, index=True)
    name = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    work_time = db.Column(db.String(100), nullable=False)
    target = db.Column(db.String(100))
    # coordinates = db.Column(db.String(100)) 

    def __repr__(self):
        return f'<Table Service {self.id} - {self.name}>'
         
         


def format_phone(phone):
    # split string for pnone number by comma
    phone_list = phone.split(',')
    for phone in phone_list:
        # remove all non-digit characters
        phone = re.sub('\D', '', phone)

        # format phone number
        phone = phone[0] + '(' + phone[1:4] + ')' + \
            phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]

    return phone_list


def get_menu_items():
    try:
        main_menu = Menu.query.order_by(Menu.priority.asc()).all()
    except Exception as e:
        main_menu = []
    return main_menu


'''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   nullable=False, unique=True, index=True)
    name = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(100))
    work_time = db.Column(db.String(100))
    target = db.Column(db.String(100))
    coordinates = db.Column(db.String(100)) 
'''

def get_service_list():
    try:
        service_list = Services.query.all()
    except Exception as e:
        service_list = []
    return service_list
    


def get_tab_hotlines():
    try:
        tab_hotlines = Table_hotline.query.order_by(
            Table_hotline.brand.asc()).all()
    except Exception as e:
        tab_hotlines = []
    return tab_hotlines


def get_index_by_handler(menu, handler):
    for menu_item in menu:
        if menu_item.handler == handler:
            return menu.index(menu_item)


def send_email(subject, formdata):
    # ['email'], ['phone'], ['name'], ['message'], ['check']
    sender = formdata['email']
    if not sender:
        sender = 'nomail@mail'
    check = formdata['check']
    if not check:
        check = 'Не заполнено'
    
    msg = Message(subject, sender=sender, recipients=app.config['ADMINS'])
   
    msg.html = f'''
    <h4>Имя клиента: {formdata['name']}</h4>
    <p>E-mail: {sender}</p>
    <p>Телефон: {formdata['phone']}</p>
    <p>Расходная накладна: {formdata['check']}</p>
    <p>Сообщение: {message}</p>'''
    
    mail.send(msg)


@app.route('/home')
@app.route('/')
def index():
    main_menu = get_menu_items()
    return render_template("main.html", menu=main_menu)


app.jinja_env.filters['format_phone'] = format_phone


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
        tab = Table_hotline.query.filter(
            Table_hotline.brand.ilike('%'+filter_str+'%')).all()
    # jsonify({"data": {"val": val}})
    return render_template("hot-lines.html", menu=main_menu, tab=tab, filter_str=filter_str)


@app.route('/our-services', methods=['GET', 'POST'])
def our_services():
    main_menu = get_menu_items()
    service_list = get_service_list()
    if request.method == 'GET':
        return render_template("our-services.html", menu=main_menu, service_list=service_list)
    
    selected_service = request.form.get("service")
    return render_template("our-services.html", menu=main_menu, service_list=service_list, selected_service=selected_service)


@app.route('/kbt')
def kbt():
    main_menu = get_menu_items()
    return render_template("kbt.html", menu=main_menu)


@app.route('/open-chat')
def open_chat():
    main_menu = get_menu_items()
    return render_template("main.html", menu=main_menu, open_chat=True)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    main_menu = get_menu_items()
    index = get_index_by_handler(main_menu, 'feedback')
    form = FeedbackForm()
    if form.validate_on_submit():
        
        send_email('Сообщение с dns-sc.ru',  form.data)
        flash('Спасибо за обращение!', 'alert alert-success')
        return redirect(url_for('index'))

    return render_template("feedback.html", form=form, menu=main_menu, index=index)


@app.route('/message')
def message():
    return render_template("modal-message.html")


if __name__ == '__main__':
    app.run(debug=True)
