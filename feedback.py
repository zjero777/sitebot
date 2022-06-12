from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, EmailField
from wtforms.validators import DataRequired, length, Email, InputRequired



class FeedbackForm(FlaskForm):
    name = StringField('Имя',
                       validators=[InputRequired(),
                                   length(min=5, max=20)],
                       render_kw={"placeholder": "Введите ваше имя"})
    
    email = EmailField('Адрес электронной почты',
                       validators=[InputRequired(),
                                   Email(message="Неправильный адрес почты", check_deliverability=True)],
                       render_kw={"placeholder": "Введите ваш email"})

    message = TextAreaField('Сообщение',
                            validators=[DataRequired(message='!!!'),
                                        length(min=2, max=500)],
                            render_kw={"placeholder": "Введите ваше сообщение", "rows": 5, "style": "resize: none;"})
    recaptcha = RecaptchaField()
