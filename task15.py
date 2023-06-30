# Определить самый легкий и самый тяжелый арбуз 
# из произвольного количества и произвольных весов.

from random import randint
kol = int(input('Введите количество арбузов: '))
i = 0
max, min = 0, 15
while i < kol:
    weight = randint(1, 15)
    print(weight, end= ' ')
    if min > weight:
        min = weight
    if max < weight:
        max = weight
    i += 1
print('\n' f'Самый легкий арбуз {min} кг. Самый тяжелый арбуз {max} кг.')
