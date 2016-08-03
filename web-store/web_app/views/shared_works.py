from functools import wraps

from flask import render_template, session, redirect,url_for

from web_app.model import account_services
from web_app.model.customer import Customer


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
            model['user_info'] = account_services.get_user_name_and_roles_info(session.get('login_account'))
        if view_result.option is None:
            return render_template(view_result.view_name, model=model)
        elif view_result.option == 'redirect':
            return redirect(url_for(view_result.redirect_dest))

    return new_function


def check_role(role_needed):
    def true_decorator(function):
        def new_function(*args):
            is_authorized = False
            if session.get('login_account'):
                login_account = session.get('login_account')
                user_roles = Customer.query.filter(Customer.account_name==login_account).first().roles
                for role in user_roles:
                    if role_needed == role.role_name:
                        is_authorized = True
            else:
                model=[]
                return render_template('error.html', model=model)
            if not is_authorized:
                model={}
                model['user_info'] = account_services.get_user_name_and_roles_info(session.get('login_account'))
                return render_template('error.html', model=model)
            else:
                return function(*args)

        return new_function

    return true_decorator
