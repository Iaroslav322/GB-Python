#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
number = int(input("Введите число дня недели от 1 до 7: "))

if number < 1 or number > 7:
    print('Вы ввели число не дня недели ;)')
elif number > 5:
    print('Этот день выходной!')
else:
    print('Этот день рабочий!')