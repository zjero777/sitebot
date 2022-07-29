from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, EmailField
from wtforms.validators import DataRequired, length, Email, InputRequired



class FeedbackForm(FlaskForm):
    name = StringField('Имя',
                       validators=[InputRequired(),
                                   length(min=5, max=20)],
                       render_kw={"placeholder": "Введите ваше имя"})
    
    phone = StringField('Телефон',
                        validators=[InputRequired(),
                                    length(min=5, max=20)],
                        render_kw={"placeholder": "Введите ваш телефон"})

    check = StringField('Номер расходной/товароной накладной',
                       render_kw={"placeholder": "Введите номер документа покупки (необязательно)"})

    
    email = EmailField('Адрес электронной почты',
                       render_kw={"placeholder": "Введите ваш email (необязательно)"})

    message = TextAreaField('Сообщение',
                            validators=[DataRequired(message='!!!'),
                                        length(min=2, max=500)],
                            render_kw={"placeholder": "Введите ваше сообщение", "rows": 5, "style": "resize: none;"})
    # recaptcha = RecaptchaField()
