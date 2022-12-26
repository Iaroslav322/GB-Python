#1. Вычислить число c заданной точностью d
from decimal import *
n = int(input('Введите число N: '))
getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN,
        Emin=-999999, Emax=999999, capitals=1,
        clamp=0, flags=[], traps=[InvalidOperation,
        DivisionByZero, Overflow])
getcontext().prec = 10
Decimal(n)
print ()


