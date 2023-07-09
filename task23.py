# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером) 

# from random import randint
# nums = []
# size = int(input('Введите размер списка: ')) 
# for i in range(size):
#     nums.append(randint(0,10))
# print(*nums)
# count = 0
# for i in range(0, len(nums)-1):
#     if nums[i-1] < nums[i]:
#         count += 1
# print(count)


import random
print(my_list := [random.randint(0, 5) for _ in range(int(input('Введите размер списка: ')))])
print(len([i for i in range(1, len(my_list)) if my_list[i - 1] < my_list[i]]))