class Field:
    """
    Вместо стандартного создания плейна по заданным размерам, динамично создаёт плейн по заданным
    размерам букв letter_width - ширина, letter_height - высота буквы.
    Адекватно отображает цифры в размерах от 5 до 10 ;)
    """

    def __init__(self, render_message: str, letter_width: int = 7, letter_height=7, mark='*',
                 background=' ', reverse=False):
        self.letter_width = letter_width
        self.letter_height = letter_height
        self.render_message = render_message
        self.mark = mark
        message_height = self.letter_height
        message_width = (self.letter_width + 1) * len(self.render_message)
        if reverse:
            self.mark, background = background, self.mark
        self.field = [[background for w in range(message_width)] for h in range(message_height)]
        self.elements = {0: self.zero, 1: self.one, 2: self.two, 3: self.three, 4: self.four,
                         5: self.five, 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

    def zero(self, coord=0):
        for z in range(self.letter_height):
            if z == 0:
                for w in range(self.letter_width):
                    self.field[z][coord+w] = self.mark
            elif z == self.letter_height - 1:
                for w in range(self.letter_width):
                    self.field[z][coord+w] = self.mark
            else:
                self.field[z][coord] = self.mark
                self.field[z][coord+self.letter_width - 1] = self.mark

    def one(self, coord=0):
        for z in range(self.letter_height):
            self.field[z][coord+self.letter_width // 2] = self.mark
            if z == 1:
                self.field[z][coord+self.letter_width // 2 - 1] = self.mark
            elif z == 2:
                self.field[z][coord+self.letter_width // 2 - 2] = self.mark
            elif z == self.letter_height - 1:
                for w in range(self.letter_width):
                    self.field[z][coord + w] = self.mark

    def two(self, coord=0):
        for w in range(1, self.letter_width - 1):
            self.field[0][coord+w] = self.mark
        for w1 in range(self.letter_width):
            self.field[self.letter_height - 1][coord+w1] = self.mark
        self.field[1][coord] = self.mark
        width_index = self.letter_width - 2
        for z in range(1, self.letter_height - 1):
            self.field[z][coord + width_index - z] = self.mark

    def three(self, coord=0):
        self.field[1][coord] = self.mark
        self.field[1][coord + self.letter_width - 3] = self.mark
        self.field[2][coord + self.letter_width - 4] = self.mark
        for w in range(1, self.letter_width - 1):
            self.field[0][coord+w] = self.mark
        for z in range(3, self.letter_height - 1):
            self.field[z][coord + z] = self.mark
        for w1 in range(self.letter_width):
            self.field[self.letter_height - 1][coord+w1] = self.mark

    def four(self, coord=0):
        for z in range(self.letter_height):
            self.field[z][coord + self.letter_width - 1] = self.mark
        for w in range(self.letter_width - 1):
            self.field[self.letter_height // 2 - 1][coord + w] = self.mark
        for z1 in range(1, self.letter_height // 2):
            self.field[z1 - 1][coord + self.letter_width // 2 - z1] = self.mark

    def five(self, coord=0):
        for w in range(1, self.letter_width):
            self.field[0][coord + w] = self.mark
        for w1 in range(1, self.letter_width - 1):
            self.field[self.letter_height // 2][coord + w1] = self.mark
        for w2 in range(self.letter_width - 1):
            self.field[self.letter_height - 1][coord + w2] = self.mark
        for z in range(1, self.letter_height // 2):
            self.field[z][coord + 1] = self.mark
        for z1 in range(self.letter_height // 2, self.letter_height):
            self.field[z1][coord + self.letter_width - 1] = self.mark

    def output(self):
        for out in self.field:
            print(*out)

    def put_mark(self, x, y):
        self.field[y][x] = self.mark

    def _constructor(self, inp_string):
        count = 0
        for elem in inp_string:
            if int(elem) in self.elements:
                self.elements.get(int(elem))(coord=count)
                count += self.letter_width + 1
        self.output()

    @staticmethod
    def create_object():
        """
        Псевдо UI. Создаёт динамическое поле под введённую пользоватлем строку,
        тем самым не давая выходить за пределы поля. Не даёт изменять остальные атрибуты объекта.
        """
        while True:
            user_input = input('Введите набор цифр для печати: ').replace(' ', '').replace(',', '')
            for inp in user_input:
                if not inp.isdigit():
                    print('Вводите только цифры от 0 до 9.')
                    user_input = False
                    break
            if user_input:
                new_field = Field(render_message=user_input)
                new_field._constructor(user_input)
                break


Field.create_object()
message1 = Field(render_message='012345', letter_width=10, letter_height=10)

#message1.output()