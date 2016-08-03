import json

from flask import request, flash

from web_app import app
from web_app.model import product_services
from web_app.model.input_model.product_form import LaptopForm
from web_app.model.product import Laptop
from web_app.views.shared_works import ViewResult, set_login_user, check_role


@app.route('/product/laptop/create', methods=['GET', 'POST'])
@check_role('admin')
@set_login_user
def create_laptop():
    form = LaptopForm()
    if request.method == 'POST' and form.validate():
        new_laptop = product_services.add_new_laptop(form)
        flash('Create laptop ' + new_laptop.product_name + 'successful!')
        return ViewResult('laptop_index.html', model={}, option='redirect', redirect_dest='laptop_index')
    model = {'form': form, 'title': 'Create new Laptop'}
    return ViewResult('create_laptop.html', model)


@app.route('/laptop/index')
@set_login_user
def laptop_index():
    laptop_list = product_services.get_laptop_list()
    model = {'product_list': laptop_list, 'title': 'Laptop'}

    return ViewResult('laptop_index.html', model)


@app.route('/laptop/detail/<string:product_code>')
@set_login_user
def laptop_detail(product_code):
    laptop_detail_info = product_services.get_laptop_detail(product_code)
    if laptop_detail_info is None:
        model = {'title': 'Error' + product_code}
        return ViewResult('laptop_error.html', model)
    else:
        model = {'laptop': laptop_detail_info, 'title': 'Home page'}
        return ViewResult('laptop_detail.html', model)


@app.route('/search')
def product_search():
    search_key = request.args['search_key']
    search_result_list = []
    if len(search_key)!=0:
        search_result_list = product_services.search_product(search_key)
    return json.dumps(search_result_list)
