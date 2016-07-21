from flask import render_template, session
from app.views.shared_works import ViewResult
from app.views.shared_works import set_login_user
from app import app
from app.model.db_service.product_services import DbService


@app.route('/index')
@app.route('/')
@set_login_user
def index():
    service = DbService()
    hot_sale_product_list = service.get_hot_sale_products()
    model = {'product_list': hot_sale_product_list, 'title': 'Home page'}
    return ViewResult('index.html', model)


# if __name__ == '__main__':
#    app.run()
