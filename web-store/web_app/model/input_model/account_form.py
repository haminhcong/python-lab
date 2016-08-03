from flask_wtf import Form
from wtforms import StringField, PasswordField, validators

from web_app.model import account_services


class LoginForm(Form):
    account_name = StringField('Account name', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

    def validate(self):
        check_validate = True
        rv = Form.validate(self)
        if not rv:
            check_validate = False
        return check_validate


class RegistrationForm(Form):
    account_name = StringField('Account Name', [validators.Length(min=4, max=25),
                                                validators.regexp('[a-zA-Z0-9]', message='only accepts  digit, lower and upper case')])
    customer_name = StringField('Customer Name')
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.email('must be email format')])
    address = StringField('Address')
    phone_number = StringField('Phone Number',[validators.regexp('[0-9]', message='must be digit')])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField('Repeat Password')

    def validate(self):
        check_validate = True
        rv = Form.validate(self)
        if not rv:
            check_validate = False
        if self.account_name.errors.__len__() == 0:
            check_exist = account_services.get_user_name_and_roles_info(self.account_name.data)
            if check_exist:
                self.account_name.errors.append('Account name exists!')
                check_validate = False
        return check_validate
