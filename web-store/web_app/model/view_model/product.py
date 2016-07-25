class HomeViewProduct:
    def __init__(self, product_code, product_name, main_image, price, promotion):
        self.product_code = product_code
        self.product_name = product_name
        self.price = price
        self.main_image = main_image
        self.promotion = promotion


class SearchResultProduct:
    def __init__(self, product_name: str, product_code: str, price: int, image:str):
        self.product_name = product_name
        self.product_code = product_code
        self.price = price
        self.image = image
class JsonData:
    def __init__(self,result):
        self.result = result