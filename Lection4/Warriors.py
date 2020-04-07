import random
hits = ['нанёс сокрушительный удар воину', 'разогнавшись, хорошенько всадил своё орудие между глаз бойцу',
        'хорошенько поднапрягся и нанёс оглушительный удар сопернику', 'со всей силы вмазал противнику',
        'вспомнив, чему учил учитель, применил бросок через бедро к врагу']

hit_points = [i for i in range(5, 51, 5)]

class Warriors:
    def __init__(self, name):
        self.health = 100
        self.name = name


class Battles:
    def battle(list_of_fighters:tuple):
        warrior1 = random.choice(list_of_fighters)
        warrior2 = list_of_fighters[list_of_fighters.index(warrior1) - 1]
        hit_point = random.choice(hit_points)
        warrior2.health -= hit_point
        print(warrior1.name, random.choice(hits), warrior2.name, f'на -{hit_point}. Остаток здоровья у '
                                                                 f'{warrior2.name}: {warrior2.health} очков.')


barbarian = Warriors('Konan the barbarian')
knight = Warriors('King Artur')
fighters = (barbarian, knight)


while barbarian.health > 0 and knight.health > 0:
    Battles.battle(fighters)

winner = barbarian if barbarian.health > 0 else knight

print(f'{winner.name} вышел победителем из этой битвы с остатком здоровья в {winner.health} очков!!!')