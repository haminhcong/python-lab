from flask import render_template, session, redirect,url_for
from app.model.db_service.service import DbService
from functools import wraps


class ViewResult:
    def __init__(self, view_name, model,redirect_dest=None, option=None):
        self.view_name = view_name
        self.model = model
        self.redirect_dest = redirect_dest
        self.option = option
        # for x in self.args:
        # print(x)


def set_login_user(function):
    @wraps(function)
    def new_function(*args):
        view_result = function(*args)
        model = view_result.model
        if not session.get('logged_in'):
            model['logged_in'] = None
        else:
            model['logged_in'] = session.get('logged_in')
            model['login_account'] = session.get('login_account')
            model['login_name'] = session.get('login_name')
        if view_result.option is None:
            return render_template(view_result.view_name, model=model)
        elif view_result.option == 'redirect':
            return redirect(url_for(view_result.redirect_dest))

    return new_function


def check_role(role_needed):
    def true_decorator(function):
        def new_function(*args):
            is_authorized = False
            db_connect = DbService();
            if session.get('logged_in'):
                login_account = session.get('login_account')
                user_roles = db_connect.get_user_roles(login_account)
                for role in user_roles:
                    if role_needed == role:
                        is_authorized = True
            else:
                return render_template('error.html', user=None)
            if not is_authorized:
                return render_template('error.html', user=session.get('login_account'))
            else:
                return function(*args)

        return new_function

    return true_decorator
