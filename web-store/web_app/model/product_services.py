from web_app.model import product
from sqlalchemy import or_
import os
from web_app.model.view_model.product import HomeViewProduct, SearchResultProduct
from web_app.model.product import Laptop, LaptopScreen, Manufacture, Product
from web_app import db
from web_app import app

def get_manufacture_list():
    data = Manufacture.query.all()
    manufacture_list = []
    for x in data:
        manufacture_list.append((int(x.id), x.name))
    return manufacture_list


def get_screen_list():
    data = LaptopScreen.query.all()
    screen_list = []
    for x in data:
        screen_list.append((int(x.id), (
            str(x.size) + ' inches - ' + str(x.resolution_width) + 'x' + str(x.resolution_height))))
    return screen_list


def check_product_code_if_exists(product_code):
    check_product = Product.query.filter(Product.product_code == product_code).first()
    if check_product is None:
        return False
    else:
        return True


def add_new_laptop(form):
    manufacture = Manufacture.query.filter(Manufacture.id == form.manufacture.data).first()
    screen = LaptopScreen.query.filter(LaptopScreen.id == form.screen.data).first()
    filename, file_extension = os.path.splitext(form.main_image.data.filename)
    image_save_location = os.path.join(app.root_path,
                                       'static/product-img/' + str(form.product_code.data) + file_extension)
    form.main_image.data.save(image_save_location)
    new_laptop = Laptop(product_code=form.product_code.data,
                        product_name=form.name.data,
                        description=form.description.data,
                        main_image=str(form.product_code.data) + file_extension,
                        price=form.price.data,
                        warranty=form.warranty.data,
                        manufacture=manufacture,
                        promotion=form.promotion.data,
                        memory=form.memory.data,
                        processor=form.processor.data,
                        storage=form.storage.data,
                        graphic_card=form.graphic_card.data,
                        screen=screen)
    db.session.add(new_laptop)
    db.session.commit()
    return new_laptop


def get_laptop_list():
    return Product.query.filter(Product.type=='laptop').all()


def get_laptop_detail(product_code):
    return Laptop.query.filter(Laptop.product_code==product_code).first()


def search_product(key: str):
    result_list = []
    data = Product.query.filter(or_(Product.product_code.contains(key), Product.product_name.contains(key))).all()
    for x in data:
        result_product = {'product_code': x.product_code, 'product_name': x.product_name, 'price': x.price,
                          'image': x.main_image}
        result_list.append(result_product)
    return result_list
