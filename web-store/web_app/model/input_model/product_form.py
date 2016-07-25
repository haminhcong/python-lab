from flask_wtf import Form
from wtforms import StringField, validators, TextAreaField, IntegerField, SelectField, FloatField
from web_app import app
from flask_wtf.file import FileField,FileAllowed,FileRequired

from web_app.model.db_service import product_services


class ProductForm(Form):
    product_code = StringField('Product code', [validators.Length(min=4, max=25),
                                                validators.regexp('[a-zA-Z0-9]',
                                                                  message='only accepts  digit, lower and upper case')])
    name = StringField('Product name', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])
    main_image = FileField("Main image",validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    price = IntegerField('Price:', [validators.DataRequired()])
    warranty = IntegerField('Warranty', [validators.DataRequired()])
    with app.app_context():
        manufacture = SelectField(u'Manufacture', choices=product_services.DbService().get_manufacture_list(),coerce=int)
    promotion = TextAreaField('Promotion', [validators.DataRequired()])

    def validate(self):
        check_validate = True
        rv = Form.validate(self)
        if not rv:
            check_validate = False
        if self.product_code.errors.__len__() == 0:
            service = product_services.DbService()
            check_exist = service.check_product_code_if_exists(self.product_code.data)
            if check_exist:
                self.product_code.errors.append('Product code exists!')
                check_validate = False
        if self.price.errors.__len__() == 0:
            int_price = int(self.price.data)
            if int_price % 10000 != 0:
                self.price.errors.append('Price must be mutiply of 10 000!')
                check_validate = False
        return check_validate


class LaptopForm(ProductForm):
    processor = StringField('Processor', [validators.DataRequired()])
    storage = StringField('Storage', [validators.DataRequired()])
    graphic_card = StringField('Graphic card', [validators.DataRequired()])
    memory = StringField('Memory', [validators.DataRequired()])
    with app.app_context():
        screen = SelectField(u'Manufacture', choices=product_services.DbService().get_screen_list(),coerce=int)

