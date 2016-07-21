class Product:
    def __init__(self, product_code, product_name, description, main_image, price, warranty, manufacture, images,
                 comments, promotion):
        self.product_code = product_code
        self.product_name = product_name
        self.description = description
        self.main_image = main_image
        self.price = price
        self.warranty = warranty
        self.manufacture = manufacture
        self.images = images
        self.comments = comments
        self.promotion = promotion


class Laptop(Product):
    def __init__(self, product_code: object, product_name: object, description: object, main_image: object, price: object, warranty: object, manufacture: object, images: object,
                 comments: object,
                 promotion: object, processor: object, memory: object, storage: object, graphic_card: object, screen: object) -> object:
        Product.__init__(self, product_code, product_name, description, main_image, price, warranty, manufacture, images,
                         comments, promotion)
        self.processor = processor
        self.memory = memory
        self.storage = storage
        self.graphic_card = graphic_card
        self.screen = screen


class Screen:
    def __init__(self, size, resolution_width, resolution_height):
        self.size = size
        self.resolution_width = resolution_width
        self.resolution_height = resolution_height
