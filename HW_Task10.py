# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

from random import randint
kol_coin = int(input('Введите количество монет: '))
sum_eagle = 0
sum_tail = 0
for i in range(kol_coin):
    side = randint(0, 1)
    print(side, end= ' ')
    if side == 1:
        sum_eagle += 1
    else:
        sum_tail += 1
print(f'\n{sum_eagle} шт лежит вверх орлом')
print(f'{sum_tail} шт лежит вверх решкой')
if sum_tail < sum_eagle:
    print(f'Надо перевернуть {sum_tail} шт, чтобы все монеты были повернуты вверх одной и той же стороной.')
elif sum_eagle < sum_tail: 
    print(f'Надо перевернуть {sum_eagle} шт, чтобы все монеты были повернуты вверх одной и той же стороной.')
else:
    print(f'Надо перевернуть {sum_eagle} "орла/ов", чтобы все монеты были повернуты вверх одной и той же стороной.')


