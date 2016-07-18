from flask import g, session
from flask import render_template, session
from app.model.db_service.service import DbService

class ViewResult:
    def __init__(self, view_name, model):
        self.view_name = view_name
        self.model = model
        #for x in self.args:
            #print(x)


def set_login_user(function):
     def new_function(*args):
        if not session.get('logged_in'):
            login_user = None
        else:
            login_user = session.get('login_user')
        view_result = function(*args)
        model = view_result.model
        model['login_user'] =login_user
        return render_template(view_result.view_name,model=model)
     return new_function


def check_role(role_needed):
    def true_decorator(function):
        def new_function(*args):
            is_authorized = False
            db_connect = DbService();
            if(session.get('logged_in') == True):
                login_user = session.get('login_user')
                user_roles = db_connect.get_user_roles(login_user)
                for role in user_roles:
                    if(role_needed == role):
                        is_authorized = True
            else:
                return render_template('error.html',user=None)
            if(is_authorized == False):
                return render_template('error.html',user=session.get('login_user'))
            else:
                return function(*args)
        return new_function
    return true_decorator
