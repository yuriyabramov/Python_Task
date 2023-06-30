num = int(input('Введите число: '))
count = 1
result = 1
while count <= num:
    result *= count
    count += 1
print(f'Факториал {num} = {result}')