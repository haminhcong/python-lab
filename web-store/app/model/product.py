class Product:
    def __init__(self, code_name, name, description, main_image, price, warranty, manufacture, images,
                 comments, promotion):
        self.code_name = code_name
        self. name = name
        self. description = description
        self.main_image = main_image
        self.price = price
        self.warranty = warranty
        self.manufacture = manufacture
        self.images = images
        self.comments = comments
        self.promotion = promotion


class Laptop(Product):
    def __init__(self, code_name, name, description, main_image, price, warranty, manufacture, images, comments,
                 promotion, processor, memory, storage, graphic_card, screen):
        Product.__init__(self, code_name, name, description, main_image, price, warranty, manufacture, images,
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
