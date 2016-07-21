from app.model.db_service import db_connection
from app.model import product
import os
from app.model.view_model.product import HomeViewProduct
from app.model.product import Laptop,Screen
from app import app
class DbService:
    def __init__(self):
        self.db_connect = db_connection.get_db()

    def get_manufacture_list(self):
        data = self.db_connect.execute('select id, name from manufacture')
        manufacture_list = []
        for x in data:
            manufacture_list.append((int(x['id']), x['name']))
        return manufacture_list

    def get_screen_list(self):
        data = self.db_connect.execute('select id,screen_size,resolution_width,resolution_height from laptop_screen')
        screen_list = []
        for x in data:
            screen_list.append((int(x['id']), (
                str(x['screen_size']) + ' inches - ' + str(x['resolution_width']) + 'x' + str(x['resolution_height']))))
        return screen_list

    def check_product_code_if_exists(self, product_code):
        query = "select product_code from product WHERE  product_code='{}'".format(product_code)
        data = self.db_connect.execute(query)
        if len(data.fetchall()) <= 0:
            return False
        else:
            return True

    def add_new_laptop(self, new_laptop:product.Laptop):
        filename, file_extension = os.path.splitext(new_laptop.main_image.filename)
        image_save_location = os.path.join(app.root_path,
                                           'static/product-img/' + str(new_laptop.product_code) + file_extension)
        new_laptop.main_image.save(image_save_location)
        self.db_connect.execute(
            "INSERT INTO  product(product_code, product_name, price, description, promotion, image, warranty, manufacture_id)"
            " VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(
                new_laptop.product_code, new_laptop.product_name, new_laptop.price, new_laptop.description,
                new_laptop.promotion,
                str(new_laptop.product_code) + file_extension, new_laptop.warranty, new_laptop.manufacture
            ))
        self.db_connect.commit()
        query ='SELECT product_id FROM product WHERE product_code ="{}"'.format(new_laptop.product_code)
        product_id = self.db_connect.execute(query).fetchone()['product_id']
        self.db_connect.execute("INSERT INTO laptop(product_id, processor_name, memory, storage, graphic_card, screen_id)"
                                " VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(
            product_id,new_laptop.processor,new_laptop.memory,new_laptop.storage,new_laptop.graphic_card,
            new_laptop.screen))
        self.db_connect.commit()

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

    def get_laptop_list(self):
        data = self.db_connect.execute('select product.product_code, product.product_name,'
                                       ' product.price,product.image, product.promotion '
                                       ' from laptop, product '
                                       'WHERE laptop.product_id = product.product_id')
        data_list = []
        for z in data:
            x = HomeViewProduct(z['product_code'], z['product_name'], z['image'], z['price'], z['promotion'])
            data_list.append(x)
        return data_list

    def get_laptop_detail(self,product_code):
        query = 'SELECT product_code,product_name,image,price,warranty,manufacture.name as manufacture_name,' \
                ' memory,processor_name,storage,graphic_card,screen_size,resolution_width,resolution_height' \
                ' FROM product,laptop,laptop_screen,manufacture WHERE product_code ="{}"' \
                ' AND laptop_screen.id=laptop.screen_id AND laptop.product_id=product.product_id ' \
                ' AND product.manufacture_id=manufacture.id'.format(product_code)
        laptop_info = self.db_connect.execute(query).fetchone()
        if laptop_info ==None:
            return None
        else:
            laptop = Laptop(
                product_code=laptop_info['product_code'],
                product_name=laptop_info['product_name'],
                main_image=laptop_info['image'],
                price=laptop_info['price'],
                warranty=laptop_info['warranty'],
                manufacture=laptop_info['manufacture_name'],
                memory=laptop_info['memory'],
                processor=laptop_info['processor_name'],
                storage=laptop_info['storage'],
                graphic_card=laptop_info['graphic_card'],
                comments=None,
                promotion=None,
                images=None,
                description=None,
                screen=Screen(size=laptop_info['screen_size'],
                              resolution_height=laptop_info['resolution_height'],
                              resolution_width=laptop_info['resolution_width'])

            )
            return laptop


