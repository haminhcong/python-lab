from web_app import db
from web_app.model.customer import Customer, Role, UserLoggedInInfo


def get_user_name_and_roles_info(account_name):
    customer_info = db.session.query(Customer).filter(Customer.account_name == account_name).first()
    if customer_info is None:
        return None
    else:
        user_info = UserLoggedInInfo(account_name=customer_info.account_name,customer_name=customer_info.customer_name, roles=customer_info.roles)
        return user_info


def add_new_account(new_account):
    user_role = Role.query.filter(Role.role_name == 'user').all()
    new_account.roles = user_role
    db.session.add(new_account)
    db.session.commit()


def get_login_info(check_account):
    account_info = Customer.query.filter(Customer.account_name==check_account.account_name).first()
    if account_info is None:
        return None
    else:
        check_password = account_info.password
        if check_account.password != check_password:
            return None
        else:
            return Customer.init_from_customer_db_info(account_info)

