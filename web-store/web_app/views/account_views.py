from flask import  session, flash,  request
from web_app.views.shared_works import ViewResult, set_login_user
from web_app import app
from web_app.model.db_service import account_services
from web_app.model import customer
from web_app.model.input_model.account_form import RegistrationForm, LoginForm


@app.route('/account/login', methods=['GET', 'POST'])
@set_login_user
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        service = account_services.DbService()
        login_account = customer.Account(form.account_name.data, form.password.data)
        login_info = service.get_login_info(login_account)
        if login_info is None:
            flash('Invalid User name or password!')
        else:
            session['login_account'] = login_info.account.account_name
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
        service = account_services.DbService()
        new_account = customer.Customer(account_name=form.account_name.data, password=form.password.data,
                                        customer_name=form.customer_name.data, address=form.address.data,
                                        mobile_phone=form.phone_number.data, email=form.email.data)
        login_info = service.add_new_account(new_account)
        session['register_account'] = login_info.account_name
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
