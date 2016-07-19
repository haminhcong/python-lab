from flask import render_template, session, flash, redirect, request, url_for
from app.views.shared_works import ViewResult, set_login_user
from app import app
from app.model.db_service.service import DbService
from app.model import customer
from app.model.input_model.form import RegistrationForm, LoginForm


@app.route('/account/login', methods=['GET', 'POST'])
@set_login_user
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        service = DbService()
        login_account = customer.Account(form.account_name.data, form.password.data)
        login_info = service.get_login_info(login_account)
        if login_info is None:
            flash('Invalid User name or password!')
        else:
            session['login_account'] = login_info.account.account_name
            session['login_name'] = login_info.customer_name
            session['logged_in'] = True
            return ViewResult(view_name=None, model={}, option='redirect', redirect_dest='index')

    if session.get('register_account'):
        form.account_name.data = session.get('register_account')
        form.password.data = session.get('register_password')
        session.pop('register_account', None)
        session.pop('register_password', None)
    model = {'form': form, 'title': 'Login'}
    return ViewResult('login.html', model)


@app.route('/account/register', methods=['GET', 'POST'])
@set_login_user
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        service = DbService()
        new_account = customer.Customer(account_name=form.account_name.data, password=form.password.data,
                                        customer_name=form.customer_name.data, address=form.address.data,
                                        mobile_phone=form.phone_number.data, email=form.email.data)
        login_info = service.add_new_account(new_account)
        session['register_account'] = login_info.account_name
        session['register_password'] = login_info.password
        flash('Thanks for registering')
        return ViewResult('register.html', model={}, option='redirect', redirect_dest='login')
    model = {'form': form, 'title': 'Home page'}
    return ViewResult('register.html', model)


@app.route('/account/logout', methods=['GET'])
@set_login_user
def logout():
    if session.get('logged_in'):
        session.pop('login_account', None)
        session.pop('login_name', None)
        session.pop('logged_in', None)
    return ViewResult(view_name=None, model={}, option='redirect', redirect_dest='index')
