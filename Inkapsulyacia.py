class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Название товара должно быть больше двух символов') 
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка скидка')
        if self.discount > self.max_discount:
            self.discount = self.max_discount
    
    def discounted(self):
        return self.price - self.price * self.discount / 100
    
    def sell(self, item_count=1):
        if item_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        self.stock -= item_count

    def __repr__(self):
        return f'<product name: {self.name}, price: {self.price}, stock: {self.stock}>'
    
# product1 = Product('Телефон', 100, 50)
# print(product1)
# product1.sell(5)
# print(product1)

class Phone(Product):
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
    
    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'
    
phone = Phone("Iphone", 50000, 'Красный')
print(phone)
print(phone.color)

class Divan(Product):
    def __init__(self, name, price, color, texture, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.texture = texture
    
    def __repr__(self):
        return f'<Диван name: {self.name}, price: {self.price}, stock: {self.stock}>'

my_divan = Divan("Iphone", 20000, 'Бежевый', 'Велюр')
print(my_divan)
print(my_divan.color)
print(my_divan.texture)