from web_app import db

class Account:
    def __init__(self, account_name, password):
        self.account_name = account_name
        self.password = password


roles = db.Table('customer_role',
                 db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
                 db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
                 db.PrimaryKeyConstraint('customer_id', 'role_id')
                 )


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    customer_name = db.Column(db.String(100))
    address = db.Column(db.String(100))
    email = db.Column(db.String(100))
    mobile_phone = db.Column(db.String(100))
    roles = db.relationship('Role', secondary=roles,
                            backref=db.backref('customers', lazy='dynamic'))

    def __init__(self, account_name, customer_name, password, address, mobile_phone, email, roles):
        self.account_name = account_name
        self.password = password
        self.customer_name = customer_name
        self.address = address
        self.email = email
        self.mobile_phone = mobile_phone
        self.roles = roles

    @classmethod
    def init_from_customer_db_info(cls,account_info):
        return cls(account_info.account_name,account_info.customer_name, account_info.password,
                           account_info.address, account_info.mobile_phone,  account_info.email, account_info.roles)

    @classmethod
    def init_from_user_register_form(cls,register_form):
        return cls(register_form.account_name.data,register_form.customer_name.data,register_form.password.data,
                   register_form.address.data,register_form.phone_number.data,register_form.email.data,[])


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(30), unique=True)

    def __init__(self, role_name):
        self.role_name = role_name


class UserLoggedInInfo:
    def __init__(self, account_name, customer_name, roles):
        self.account_name = account_name
        self.customer_name = customer_name
        self.roles = roles
