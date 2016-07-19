from app.model.db_service import db_connection
from app.model.view_model.product import HomeViewProduct
from app.model.customer import Customer, Account
import sqlite3
from app import app


class DbService:
    def __init__(self):
        self.db_connect = db_connection.get_db()

    def get_hot_sale_products(self):
        data = self.db_connect.execute('select product.product_code, product.product_name,'
                                       ' product.price,product.image, product.promotion '
                                       ' from best_seller_product, product '
                                       'WHERE best_seller_product.id = product.product_id')
        data_list = []
        for z in data:
            x = HomeViewProduct(z['product_code'], z['product_name'], z['image'], z['price'], z['promotion'])
            data_list.append(x)
        return data_list

    def get_user(self, account):
        data = self.db_connect.execute('select * from customer WHERE customer.account_name=account_name')
        data_list = []
        for z in data:
            x = Customer(z['account_name'], z['password'], z['customer_name'], z['address'], z['mobile_phone'])
            pass
            # Viet them cau lenh querry role cho x.roles
            data_list.append(x)
        return data_list

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
        result = self.db_connect.execute(query)
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

    def get_user_roles(self, account_id):
        query_role_id = "select role_id  from account_role WHERE account_id='{}'".format(account_id)
        data_role_id = self.db_connect.execute(query_role_id)
        data_list = []
        for z in data_role_id:
            x = z['role_id']
            query_role_name = "select name  from role WHERE id='{}'".format(x)
            data_role_name = self.db_connect.execute(query_role_name)
            for z2 in data_role_name:
                x2 = z2['name']
                data_list.append(x2)
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
