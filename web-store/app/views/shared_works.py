from flask import render_template, session, redirect,url_for
from app.model.db_service import account_services
from functools import wraps


class ViewResult:
    def __init__(self, view_name, model, redirect_dest=None, option=None):
        self.view_name = view_name
        self.model = model
        self.redirect_dest = redirect_dest
        self.option = option
        # for x in self.args:
        # print(x)


def set_login_user(function):
    @wraps(function)
    def new_function(*args, **kwargs):
        view_result = function(*args, **kwargs)
        model = view_result.model
        if not session.get('login_account'):
            model['user_info'] = None
        else:
            db_connect = account_services.DbService()
            model['user_info'] = db_connect.get_user_name_and_roles_info(session.get('login_account'))
        if view_result.option is None:
            return render_template(view_result.view_name, model=model)
        elif view_result.option == 'redirect':
            return redirect(url_for(view_result.redirect_dest))

    return new_function


def check_role(role_needed):
    def true_decorator(function):
        def new_function(*args):
            is_authorized = False
            db_connect = account_services.DbService()
            if session.get('login_account'):
                login_account = session.get('login_account')
                user_roles = db_connect.get_user_roles(db_connect.get_account_id(account_name=login_account))
                for role in user_roles:
                    if role_needed == role:
                        is_authorized = True
            else:
                model=[]
                return render_template('error.html', model=model)
            if not is_authorized:
                db_connect = account_services.DbService()
                model={}
                model['user_info'] = db_connect.get_user_name_and_roles_info(session.get('login_account'))
                return render_template('error.html', model=model)
            else:
                return function(*args)

        return new_function

    return true_decorator
