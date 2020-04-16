from decor_output import *


class Store:
    products = {}

    def __init__(self, title=None):
        self.title = title

    @staticmethod
    def add_product(product, number_of_products=1):
        Store.products[product.name] = Store.products.get(product.name, [0, 0])
        Store.products[product.name][0] = product.price
        Store.products[product.name][1] += number_of_products

    def show_case(self, product=None):
        if product is None:
            decor_output(f'Ассортимент магазина {self.title}:')
            for k, v in Store.products.items():
                print(f'Количество товара {k}: {v[1]}, суммарная стоимость: {round(v[1] * v[0], 2)}')
            print()
        elif product in Store.products:
            decor_output(f'Количество товара {product}: {Store.products.get(product)[1]}, '
                            f'суммарная стоимость: {round(Store.products[product][0] * Store.products[product][1], 2)}')
        else:
            decor_output(f'Товар {product} отсутсвует в магазине.')