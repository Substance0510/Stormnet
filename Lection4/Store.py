class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Store(Product):
    products = {}

    def add_product(self, number_of_products=1):
        Store.products[self.name] = Store.products.get(self.name, 0) + number_of_products

    def show_case(self=None):
        if self is None:
            for x, y in Store.products.items():
                print(f'Количество товара {x}: {y}, суммарная стоимость: {globals().get(x).price * y}')
        elif self.name in Store.products:
            print(f'Количество товара {self.name}: {Store.products.get(self.name)}, '
                  f'суммарная стоимость: {self.price * Store.products.get(self.name)}')
        else:
            print(f'Товар {self.name} отсутсвует в магазине.')

pomidorka = Store('pomidorka', 11)
pomidorka.add_product(3)
ogurok = Store('ogurok', 9)
ogurok.add_product(5)
kartoha = Product('kartoha', 23)

Store.add_product(kartoha, 9)

ogurok.show_case()
pomidorka.show_case()
Store.show_case(kartoha)

print()
Store.show_case(ogurok)
print()
Store.show_case()