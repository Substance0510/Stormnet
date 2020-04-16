class Field:
    def __init__(self, height, weidh):
        self.height = height
        self.weidh = weidh
        self.field = [[' ' for w in range(weidh)] for h in range(height)]

    def zero(self, coord):
        for z in range(4):
            if z == 0:
                for w in range(3):
                    self.field[z][coord+w] = 'O'
            elif z == 3:
                for w in range(3):
                    self.field[z][coord+w] = 'O'
            else:
                self.field[z][coord] = 'O'
                self.field[z][coord+2] = 'O'

    def one(self, coord):
        for z in range(4):
            self.field[z][coord] = '1'

    def two(self, coord):
        for w in range(3):
            self.field[0][coord+w] = '2'
        for w in range(3):
            self.field[3][coord+w] = '2'
        self.field[1][coord + 2] = '2'
        self.field[2][coord + 1] = '2'


field1 = Field(5, 5)
field2 = Field(5, 5)
field3 = Field(5, 5)
field1.zero(1)
field2.one(2)
field3.two(1)

for f in field1.field:
    print(f)

for f in field2.field:
    print(f)

for f in field3.field:
    print(f)