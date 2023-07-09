# Дан список чисел. Определите, сколько в нем
# встречается разных чисел(не имеющих дубликатов).

import random
print(my_list := [random.randint(0, 7) for _ in range(int(input('Введите количество чисел: ')))])
print(len(set(my_list)))