import json


def _decor_output(func):
    def wrapper(inp_str):
        print('=' * len(inp_str))
        func(inp_str)
        print('=' * len(inp_str))
    return wrapper


@_decor_output
def decor_output(in_str):
    print(in_str)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Store:
    products = {}
    file = 'products.txt'

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


class ProductPriceCountException(Exception):
    pass


class Manager:

    title = None

    @staticmethod
    def _check_user_input(user_input):
        try:
            user_input = float(user_input)
            if 0 < user_input < 1000:
                return user_input
            else:
                decor_output('Не вводите таких больших чисел ;)')
                raise ProductPriceCountException
        except (ValueError, ProductPriceCountException):
            return False

    @staticmethod
    def _read_from_file():
        try:
            with open(Store.file, 'r') as read_file:
                internal_title = read_file.readline().strip()
                internal_products = json.loads(read_file.readline())
                return internal_title, internal_products
        except(FileNotFoundError, FileExistsError):
            return None, {}

    @staticmethod
    def _write_to_file():
        with open(Store.file, 'w') as write_file:
            write_file.write(Manager.title + '\n')
            json.dump(Store.products, write_file)

    @staticmethod
    def manager():
        Manager.title, Store.products = Manager._read_from_file()
        if Manager.title is None:
            new_store = Store(title=input('Введите наименование магазина: '))
            Manager.title = new_store.title
        else:
            decor_output(f'Добро пожаловать в магазин {Manager.title}!')
            new_store = Store(Manager.title)
        while True:
            if not Store.products:
                decor_output('Наш магазин совсем пуст :( Давайте добавим хотябы один товар.')
                product_name = input('Введите имя товара: ').upper()
                product_count = Manager._check_user_input(input('Введите количество товара: '))
                if not product_count:
                    continue
                product_price = Manager._check_user_input(input('Введите стоимость товара за штуку: ').replace(',', '.'))
                if product_count and product_price:
                    product = Product(product_name, product_price)
                    Store.add_product(product, int(product_count))
                    decor_output('Продукт успешно добавлен на полку магазина!')
                else:
                    decor_output('Пожалуйста, введите корректные данные для количества и стоимости товара.')
                    continue
            else:
                print('Если вы хотите добавить ещё один товар или пополнить количество существующего,'
                      ' или изменить стоимость, введите Y.')
                print('Если вы хотите завершить работу с программой, нажмите N.')
                print('Если вы хотите просмотреть количество и стоимость определённого продукта, '
                      'введите его наименование.')
                print('Если вы хотите увидеть все полки магазина, введите All.')
                user_choise = input('Ваш выбор: ').upper()
                if user_choise == 'N':
                    decor_output(f'Спасибо, что выбрали наш магазин {Manager.title}!')
                    if Store.products:
                        Manager._write_to_file()
                    break
                elif user_choise == 'Y':
                    product_name = input('Введите наименование товара: ').upper()
                    product_count = Manager._check_user_input(input('Введите количество товара: '))
                    product_price = Manager._check_user_input(input('Введите стоимость товара за штуку: ')
                                                              .replace(',', '.'))
                    if product_count and product_price:
                        if product_name not in Store.products:
                            product = Product(product_name, product_price)
                            Store.add_product(product, int(product_count))
                            decor_output('Продукт успешно добавлен на полку магазина!')
                        elif product_name in Store.products:
                            Store.products[product_name][1] += int(product_count)
                            Store.products[product_name][0] = product_price
                            decor_output('Данные по продукту успешно изменены!')
                    else:
                        decor_output('Пожалуйста, введите корректные данные для количества и стоимости товара.')
                        continue
                elif user_choise in Store.products:
                    Store.show_case(new_store, user_choise)
                elif user_choise == 'ALL':
                    Store.show_case(new_store)
                else:
                    decor_output('Пожалуйста, сделайте выбор из предложенных вариантов.')


Manager.manager()