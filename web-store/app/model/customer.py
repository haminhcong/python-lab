class Account:
    def __init__(self, account_name, password):
        self.account_name = account_name
        self.password = password


class Customer:
    def __init__(self, account, name, address, mobile_phone, roles):
        self.account = account
        self.name = name
        self.address = address
        self.mobile_phone = mobile_phone
        self.roles = roles


class Role:
    def __init__(self, role_name):
        self.role_name = role_name