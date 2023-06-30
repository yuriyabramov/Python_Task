# Какое максимальное количество дней оттепели было
# подряд в произвольном количестве всех дней. 

from random import randint
days, count = int(input('Введите количество дней за отчетный период: ')), 0
ottepel, longest = 0, 0
gradus = 0
for i in range(days):
    gradus += randint(-3, 3)
    print(gradus, end= ' ')
    if gradus > 0:
        ottepel += 1
        if ottepel > longest:
            longest = ottepel
    else:
        ottepel = 0
print(f'\n {longest} дня/ей была самая длинная оттепель')
