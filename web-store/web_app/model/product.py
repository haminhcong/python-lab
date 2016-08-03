from web_app import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(100), unique=True)
    product_name = db.Column(db.String(200))
    description = db.Column(db.String(400))
    main_image = db.Column(db.String(200))
    price = db.Column(db.Integer)
    warranty = db.Column(db.Integer)
    manufacture_id = db.Column(db.Integer, db.ForeignKey('manufacture.id'))
    promotion = db.Column(db.String(400))
    type = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'product',
        'polymorphic_on': type
    }

    #    def __init__(self, product_code, product_name, description, main_image, price, warranty, manufacture, images,
    #                 comments, promotion):
    def __init__(self, product_code, product_name, description, main_image, price, warranty, manufacture, promotion):
        self.product_code = product_code
        self.product_name = product_name
        self.description = description
        self.main_image = main_image
        self.price = price
        self.warranty = warranty
        self.manufacture = manufacture
        # self.images = images
        # self.comments = comments
        self.promotion = promotion


class Laptop(Product):
    __tablename__ = 'laptop'
    id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    processor = db.Column(db.String(200))
    memory = db.Column(db.String(200))
    storage = db.Column(db.String(200))
    graphic_card = db.Column(db.String(200))
    laptop_screen_id = db.Column(db.Integer, db.ForeignKey('laptop_screen.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'laptop',
    }

    def __init__(self, product_code, product_name, description, main_image, price, warranty, manufacture,
                 promotion, processor, memory, storage, graphic_card, screen):
        Product.__init__(self, product_code, product_name, description, main_image, price, warranty, manufacture,
                         promotion)
        self.processor = processor
        self.memory = memory
        self.storage = storage
        self.graphic_card = graphic_card
        self.screen = screen


class Manufacture(db.Model):
    __tablename__ = 'manufacture'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    products = db.relationship('Product', backref='manufacture', lazy='dynamic')


class LaptopScreen(db.Model):
    __tablename__ = 'laptop_screen'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Float)
    resolution_width = db.Column(db.Integer)
    resolution_height = db.Column(db.Integer)
    laptops = db.relationship('Laptop', backref='screen', lazy='dynamic')

    def __init__(self, size, resolution_width, resolution_height):
        self.size = size
        self.resolution_width = resolution_width
        self.resolution_height = resolution_height


class HotSaleProduct(db.Model):
    __tablename__ = 'hot_sale_product'
    id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
