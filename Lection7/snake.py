class Field:

    def __init__(self, weidh, height=10, mark='*', background=' ', reverse=False):
        self.height = height
        self.weidh = weidh
        self.mark = mark
        if reverse:
            self.mark, background = background, self.mark
        self.field = [[background for w in range(weidh)] for h in range(height)]
        self.elements = {0: self.zero, 1: self.one, 2: self.two, 3: self.three, 4: self.four,
                         5: self.five, 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

    def zero(self, coord=0):
        for z in range(5):
            if z == 0:
                for w in range(5):
                    self.field[z][coord+w] = self.mark
            elif z == 4:
                for w in range(5):
                    self.field[z][coord+w] = self.mark
            else:
                self.field[z][coord] = self.mark
                self.field[z][coord+4] = self.mark

    def one(self, coord=0):
        for z in range(5):
            self.field[z][coord+2] = self.mark
            if z == 1:
                self.field[z][coord+1] = self.mark
            elif z == 2:
                self.field[z][coord] = self.mark
            elif z == 4:
                for w in range(5):
                    self.field[z][coord + w] = self.mark

    def two(self, coord=0):
        for w in range(1, 4):
            self.field[0][coord+w] = self.mark
        for w1 in range(5):
            self.field[4][coord+w1] = self.mark
        self.field[1][coord] = self.mark
        self.field[1][coord + 4] = self.mark
        self.field[2][coord + 3] = self.mark
        self.field[3][coord + 2] = self.mark

    def three(self, coord=0):
        for w in range(1, 4):
            self.field[0][coord+w] = self.mark
        self.field[1][coord] = self.mark
        self.field[1][coord + 4] = self.mark
        self.field[2][coord + 3] = self.mark
        self.field[3][coord + 4] = self.mark
        for w1 in range(5):
            self.field[4][coord+w1] = self.mark

    def four(self, coord=0):
        for z in range(5):
            self.field[z][coord + 4] = self.mark
        for w in range(4):
            self.field[2][coord + w] = self.mark
        self.field[0][coord + 2] = self.mark
        self.field[1][coord + 1] = self.mark

    def five(self, coord=0):
        for w in range(1, 5):
            self.field[0][coord + w] = self.mark
        for w1 in range(1, 4):
            self.field[2][coord + w1] = self.mark
        for w2 in range(4):
            self.field[4][coord + w2] = self.mark
        self.field[1][coord + 1] = self.mark
        self.field[3][coord + 4] = self.mark

    def _output(self):
        for out in self.field:
            print(*out)

    def put_mark(self, x, y):
        self.field[y][x] = self.mark

    def _constructor(self, inp_string):
        count = 0
        for elem in inp_string:
            if int(elem) in self.elements:
                self.elements.get(int(elem))(coord=count)
                count += 6
        self._output()

    @staticmethod
    def create_object():
        while True:
            user_input = input('Введите набор цифер для печати: ').replace(' ', '').replace(',', '')
            for inp in user_input:
                if not inp.isdigit():
                    print('Вводите только цифры от 0 до 9.')
                    user_input = False
                    break
            if user_input:
                new_field = Field(weidh=len(user_input)*6)
                new_field._constructor(user_input)
                break


Field.create_object()
field1 = Field(15, 95, mark=' ', background='-', reverse=True)
field2 = Field(10, 100)


# smile
# field1.put_mark(2, 0)
# field1.put_mark(5, 0)
# field1.put_mark(1, 2)
# field1.put_mark(2, 3)
# field1.put_mark(3, 4)
# field1.put_mark(4, 4)
# field1.put_mark(5, 3)
# field1.put_mark(6, 2)