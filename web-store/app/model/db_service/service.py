from app.model.db_service import db_connection
from app.model.view_model.product import HomeViewProduct
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

    def get_user_roles(self,account_name):
        pass