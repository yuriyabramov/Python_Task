# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число. Примечание: Пользователь может 
# вводить значения списка или список задан изначально.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

from random import randint
nums = []
size = int(input('Введите размер списка: ')) 
for i in range(size):
    nums.append(randint(0,10))
print(*nums)
sdvig = int(input('Введите на сколько сдвинуть: ')) % len(nums)
nums = nums[-sdvig:] + nums[:-sdvig]
print(*nums)
