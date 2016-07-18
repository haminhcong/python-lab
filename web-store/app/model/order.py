class Order():
    def __init__(self, date, items, total, customer):
        self.date = date
        self.items = items
        self.total = total
        self.customer = customer


class Item:
    def __init__(self, product_name, product_code, quantity, price, image):
        self.product_name = product_name
        self.product_code = product_code
        self.quantity = quantity
        self.price = price
        self.image = image
