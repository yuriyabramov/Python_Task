#Задача 6. Напишите программу, проверяющую: билет из 6 цифр счастливый или нет. 

# 1 способ
# ticket = input('Введите шестизначный номер билета: ')
# if len(ticket) != 6:
#     print(f'Ошибка ввода! Число {ticket} не шестизначное!')
# else:
#     left = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
#     right = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
#     if left == right:
#         print('Yes')
#     else:
#         print('NO')

# 2 способ
import random
ticket = random.randrange(100000, 999999, 1)
res = [int(x) for x in str(ticket)]
left = int(res[0]) + int(res[1]) + int(res[2])
right = int(res[3]) + int(res[4]) + int(res[5])
if left == right:
    print(f' {ticket} --> Yes')
else:
    print(f' {ticket} --> No')