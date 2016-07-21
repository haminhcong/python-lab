from app.model.db_service import db_connection
from app.model.customer import Customer, UserLoggedInInfo


class DbService:
    def __init__(self):
        self.db_connect = db_connection.get_db()

    def get_user_name_and_roles_info(self, account_name):
        query = "SELECT id,customer_name FROM customer WHERE account_name ='{}'".format(account_name)
        data = self.db_connect.execute(query).fetchone()
        roles = self.get_user_roles(data['id'])
        user_info = UserLoggedInInfo(account_name=account_name,customer_name=data['customer_name'],roles=roles)
        return user_info

    def check_account_if_exists(self, check_account_name):
        query = "select * from customer WHERE customer.account_name='" + check_account_name + "'"
        data = self.db_connect.execute(query)
        if len(data.fetchall()) <= 0:
            return False
        else:
            return True

    def add_new_account(self, new_account):
        query = 'INSERT INTO customer(account_name,customer_name,email,address,mobile_phone,password) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}")'.format(
            new_account.account.account_name,
            new_account.customer_name,
            new_account.email, new_account.address, new_account.mobile_phone,
            new_account.account.password)
        self.db_connect.execute(query)
        self.db_connect.commit()
        account_id = self.db_connect.execute(
            'SELECT id FROM customer WHERE account_name ="{}"'.format(new_account.account.account_name)).fetchone()[
            'id']
        user_role_id = \
            self.db_connect.execute('SELECT id FROM role WHERE role.name ={}'.format("\'user\'")).fetchone()['id']
        self.db_connect.execute(
            'INSERT INTO account_role(account_id,role_id) VALUES({0},{1})'.format(account_id, user_role_id))
        self.db_connect.commit()
        return new_account.account

    def get_account_id(self,account_name):
        query = 'SELECT id FROM customer WHERE account_name ="{}"'.format(account_name)
        return self.db_connect.execute(query).fetchone()['id']

    def get_user_roles(self, account_id):
        query_role_id = "select role_id  from account_role WHERE account_id='{}'".format(account_id)
        data_role_id = self.db_connect.execute(query_role_id)
        data_list = []
        for z in data_role_id:
            x = z['role_id']
            query_role_name = "select name  from role WHERE id='{}'".format(x)
            role_name = self.db_connect.execute(query_role_name).fetchone()['name']
            data_list.append(role_name)
        return data_list

    def get_login_info(self, check_account):
        query = "select id,account_name,customer_name,password from customer WHERE customer.account_name='{}'".format(
            check_account.account_name)
        data = self.db_connect.execute(query)
        account_info = data.fetchone()
        if account_info is None:
            return None
        else:
            check_password = account_info['password']
            if check_account.password != check_password:
                return None
            else:
                roles = self.get_user_roles(account_info['id'])
                return Customer(account_name=check_account.account_name, customer_name=account_info['customer_name'],
                                roles=roles)
