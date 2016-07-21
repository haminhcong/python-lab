class Account:
    def __init__(self, account_name, password):
        self.account_name = account_name
        self.password = password


class Customer:

    def __init__(self, account_name,customer_name, password=None,  address=None, mobile_phone=None, email=None, roles = None):
        self.account = Account(account_name, password)
        self.customer_name = customer_name
        self.address = address
        self.email = email
        self.mobile_phone = mobile_phone
        self.roles = roles


class UserLoggedInInfo:
    def __init__(self, account_name, customer_name, roles):
        self.account_name = account_name
        self.customer_name = customer_name
        self.roles = roles


class Role:
    def __init__(self, role_name):
        self.role_name = role_name
