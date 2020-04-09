import json

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Store:
    products = {}
    title = None
    file = '/home/anton/Документы/Training/products.txt'

    @staticmethod
    def _read_from_file():
        try:
            with open(Store.file, 'r') as read_file:
               return json.load(read_file)
        except:
            return {}

    @staticmethod
    def _write_to_file():
        with open(Store.file, 'w') as write_file:
            json.dump(Store.products, write_file)

    @staticmethod
    def _add_product(product, number_of_products=1):
        Store.products[product.name] = Store.products.get(product.name, [0, 0])
        Store.products[product.name][0] = product.price
        Store.products[product.name][1] += number_of_products

    @staticmethod
    def _show_case(product=None):
        if product is None:
            print(f'Ассортимент магазина {Store.title}:')
            for k, v in Store.products.items():
                print(f'Количество товара {k}: {v[1]}, суммарная стоимость: {v[1] * v[0]}')
        elif product in Store.products:
            print(f'Количество товара {product}: {Store.products.get(product)[1]}, '
                  f'суммарная стоимость: {Store.products[product][0] * Store.products[product][1]}')
        else:
            print(f'Товар {product} отсутсвует в магазине.')

    @staticmethod
    def _check_user_input(user_input):
        try:
            user_input = float(user_input)
            if user_input > 0:
                return user_input
            else:
                raise ValueError
        except ValueError:
            return False

    @staticmethod
    def manager():
        if Store.title is None:
            Store.title = input('Введите наименование магазина: ')
            Store.products = Store._read_from_file()
        while True:
            if not Store.products:
                print('Наш магазин совсем пуст :( Давайте добавим хотябы один товар.')
                product_name = input('Введите имя товара: ').upper()
                product_count = Store._check_user_input(input('Введите количество товара: '))
                product_price = Store._check_user_input(input('Введите стоимость товара за штуку: ').replace(',', '.'))
                if product_count and product_price:
                    product = Product(product_name, product_price)
                    Store._add_product(product, int(product_count))
                else:
                    print('Пожалуйста, введите корректные данные для количества и стоимости товара.')
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
                    print(f'Спасибо, что выбрали наш магазин {Store.title}!')
                    if Store.products:
                        Store._write_to_file()
                    break
                elif user_choise == 'Y':
                    product_name = input('Введите наименование товара: ').upper()
                    product_count = Store._check_user_input(input('Введите количество товара: '))
                    product_price = Store._check_user_input(input('Введите стоимость товара за штуку: ')
                                                            .replace(',', '.'))
                    if product_count and product_price:
                        if product_name not in Store.products:
                            product = Product(product_name, product_price)
                            Store._add_product(product, int(product_count))
                        elif product_name in Store.products:
                            Store.products[product_name][1] += int(product_count)
                            Store.products[product_name][0] = product_price
                    else:
                        print('Пожалуйста, введите корректные данные для количества и стоимости товара.')
                        continue
                elif user_choise in Store.products:
                    Store._show_case(user_choise)
                elif user_choise == 'ALL':
                    Store._show_case()
                else:
                    print('Пожалуйста, сделайте выбор из предложенных вариантов.')


Store.manager()


