from web_app.views.shared_works import ViewResult
from web_app.views.shared_works import set_login_user
from web_app import app
from web_app.model.product import  Product,HotSaleProduct
from flask import session
@app.route('/index')
@app.route('/')
@set_login_user
def index():
    hot_sale_product_list = Product.query.join(HotSaleProduct,Product.id == HotSaleProduct.id).all()
    model = {'product_list': hot_sale_product_list, 'title': 'Home page'}
    return ViewResult('index.html', model)


# if __name__ == '__main__':
#    web_app.run()
