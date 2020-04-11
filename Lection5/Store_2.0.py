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
    file = 'products.txt'
    title = None

    @staticmethod
    def _check_user_input(user_input):
        try:
            user_input = float(user_input)
            if 0 < user_input < 1000:
                return user_input
            else:
                decor_output('Количество и стоимость товара должны быть больше 0 и меньше 1000.')
                raise ProductPriceCountException
        except (ValueError, ProductPriceCountException):
            decor_output('Пожалуйста, введите корректные данные для количества и стоимости товара.')
            return False

    @staticmethod
    def _read_from_file():
        try:
            with open(Manager.file, 'r') as read_file:
                internal_title = read_file.readline().strip()
                internal_products = json.loads(read_file.readline())
                return internal_title, internal_products
        except(FileNotFoundError, FileExistsError):
            return None, {}

    @staticmethod
    def _write_to_file():
        with open(Manager.file, 'w') as write_file:
            write_file.write(Manager.title + '\n')
            json.dump(Store.products, write_file)

    @staticmethod
    def _check_or_create_store():
        Manager.title, Store.products = Manager._read_from_file()
        if Manager.title is None:
            return Store(title=input('Введите наименование магазина: '))
        else:
            decor_output(f'Добро пожаловать в магазин {Manager.title}!')
            return Store(Manager.title)

    @staticmethod
    def _check_and_add_product():
        product_name = input('Введите имя товара: ').upper()
        while True:
            product_count = Manager._check_user_input(input('Введите количество товара: '))
            if not product_count:
                continue
            product_price = Manager._check_user_input(
                input('Введите стоимость товара за штуку: ').replace(',', '.'))
            if not product_price:
                continue
            if product_name not in Store.products:
                product = Product(product_name, product_price)
                Store.add_product(product, int(product_count))
                decor_output('Продукт успешно добавлен на полку магазина!')
                break
            elif product_name in Store.products:
                Store.products[product_name][1] += int(product_count)
                Store.products[product_name][0] = product_price
                decor_output(f'Данные по продукту {product_name} успешно изменены!')
                break

    @staticmethod
    def manager():
        our_store = Manager._check_or_create_store()
        Manager.title = our_store.title
        while True:
            if not Store.products:
                decor_output('Наш магазин совсем пуст :( Давайте добавим хотябы один товар.')
                Manager._check_and_add_product()
            else:
                print('Если вы хотите добавить ещё один товар или пополнить количество существующего,\n'
                      'или изменить стоимость, введите Y.\nЕсли вы хотите завершить работу с программой, введите N.\n'
                      'Если вы хотите просмотреть количество и стоимость определённого продукта,'
                      'введите его наименование.\n'
                      'Если вы хотите увидеть все полки магазина, введите All.')
                user_choise = input('Ваш выбор: ').upper()
                if user_choise == 'N':
                    decor_output(f'Спасибо, что выбрали наш магазин {Manager.title}!')
                    if Store.products:
                        Manager._write_to_file()
                    break
                elif user_choise == 'Y':
                    Manager._check_and_add_product()
                elif user_choise in Store.products:
                    Store.show_case(our_store, user_choise)
                elif user_choise == 'ALL':
                    Store.show_case(our_store)
                else:
                    decor_output('Пожалуйста, сделайте выбор из предложенных вариантов.')


Manager.manager()