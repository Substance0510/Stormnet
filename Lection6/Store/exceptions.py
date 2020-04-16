from decor_output import *


class ProductPriceCountException(Exception):

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