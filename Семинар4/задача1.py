#1. Вычислить число c заданной точностью d
from decimal import Decimal

a = float(input("Введите число: "))
number = Decimal(a)
str = input("Введите точность: ")
print(number.quantize(Decimal(str)))

