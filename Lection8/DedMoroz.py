from json import dump as jdump
from json import dumps as jdumps
from fpdf import FPDF

class DedMoroz:
    def __init__(self, name:str, behavior:bool, gifts=None):
        self.name = name
        self.behavior = behavior
        self.gifts = gifts

        self._print_welcome_message()
        if isinstance(self.gifts, dict):
            self._print_gifts_dict()
        elif isinstance(self.gifts, list):
            self._print_gifts_list()
        elif self.gifts is None and self.behavior:
            print('к сожалению, у Дедушки Мороза не хватило на всех подарков. '
                  'Не расстраивайся, он обязательно что-нибудь придумает ;)')
        elif self.gifts is not None and not isinstance(self.gifts, (dict, list)):
            raise Exception('Не поддерживаемый формат подарков.')
        self._write_file()

    def _print_welcome_message(self):
        print(f'Здравствуй, мой дорогой друг, {self.name}. В этом году твоё поведение было',
              'хорошим.' if self.behavior else 'не очень хорошим.', 'Поэтому, за такое поведение, Дедушка Мороз тебе',
              'принёс: ' if self.behavior else 'ничего не принёс.\nПостарайся в следующем году.')

    def _print_gifts_dict(self):
        for gift, count in self.gifts.items():
            print(f'{gift}: {count}')

    def _print_gifts_list(self):
        print(*self.gifts, sep=', ')

    def _write_file(self):
        file = '/home/anton/PycharmProjects/training/DedMoroz/' + str(self.name) + '.txt'
        with open(file, 'w') as wf:
            wf.write(self.name + '\n' + str(self.behavior) + '\n')
            jdump(self.gifts, wf)

    def write_file_pdf(self):
        file = '/home/anton/PycharmProjects/training/DedMoroz/' + str(self.name) + '.pdf'
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(100, 10, txt=self.name)
        pdf.cell(100, 10, txt=str(self.behavior))
        pdf.output(file)



recipient1 = DedMoroz('Anton', True, {'Загородный коттедж со всеми удобствами': 1,
                                      'Новый автомобиль иномарка': 2, 'Квартира в Минске': 3,
                                      'Денежный приз': '5 миллионов долларов США'})
print()
recipient1.write_file_pdf()

recipient2 = DedMoroz(name='Kate', behavior=True, gifts=['Квартира в Минске', 'Новая иномарка',
                                                         'Загородный коттедж', 'Путёвка на Мальдивы.'])
print()

recipient3 = DedMoroz(name='BadBoy', behavior=False)
print()

recipient4 = DedMoroz(name='GoodBoy', behavior=True)
print()

#recipient5 = DedMoroz(name='TestBoy', behavior=True, gifts='Падаруначки...')