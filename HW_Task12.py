# Петя задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Есть две подсказки: сумма этих 
# чисел  = S, а их произведение = P. Помогите Кате отгадать числа.   


sum = int(input('Результат суммы двух загаданных чисел: '))
mult = int(input('Результат умножения двух загадынных чисел: '))
for num1 in range(sum):
    for num2 in range(mult):
        if sum == num1 + num2 and mult == num1 * num2:
            print(num1, num2)
        