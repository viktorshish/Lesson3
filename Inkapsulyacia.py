class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Название товара должно быть больше двух символов') 
        self.price = price
        self.stock = stock
        self.discount = discount
        self.max_discount = max_discount
    