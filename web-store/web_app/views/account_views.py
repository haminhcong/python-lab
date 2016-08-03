from flask import  session, flash,  request

from web_app import app
from web_app.model import customer, account_services
from web_app.model.input_model.account_form import RegistrationForm, LoginForm
from web_app.views.shared_works import ViewResult, set_login_user


@app.route('/account/login', methods=['GET', 'POST'])
@set_login_user
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        login_account = customer.Account(form.account_name.data, form.password.data)
        login_info = account_services.get_login_info(login_account)
        if login_info is None:
            flash('Invalid User name or password!')
        else:
            session['login_account'] = login_info.account_name
            return ViewResult(view_name=None, model={}, option='redirect', redirect_dest='index')

    if session.get('register_account'):
        form.account_name.data = session.get('register_account')
        session.pop('register_account', None)
    model = {'form': form, 'title': 'Login'}
    return ViewResult('login.html', model)


@app.route('/account/register', methods=['GET', 'POST'])
@set_login_user
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        new_account = customer.Customer.init_from_user_register_form(register_form=form)
        account_services.add_new_account(new_account)
        session['register_account'] = new_account.account_name
        flash('Thanks for registering')
        return ViewResult('register.html', model={}, option='redirect', redirect_dest='login')
    model = {'form': form, 'title': 'Home page'}
    return ViewResult('register.html', model)


@app.route('/account/logout', methods=['GET'])
@set_login_user
def logout():
    if session.get('login_account'):
        session.pop('login_account', None)
    return ViewResult(view_name=None, model={}, option='redirect', redirect_dest='index')
