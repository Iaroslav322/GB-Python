from sympy import *
import sympy

x = Symbol('x')
y = 2 * x ** 3 + 2 * x ** 2 - 18 * x - 18
print('\n 1. Определить корни')
print(solve(y))

df = diff(y)
df_roots = solve(df)
float(df_roots[0]), float(df_roots[1])


print(f'\n 2. Найти интервалы, на которых функция возрастает: ')
print(solve(df>0))


print(f'\n 3. Найти интервалы, на которых функция убывает: ')
print(solve(df < 0))

sympy.plotting.plot(2 * x ** 3 + 2 * x ** 2 - 18 * x - 18)

from random import uniform

f_diff = sorted(solveset(diff(y), x, Reals).evalf(2))
f_diff.insert(0, f_diff[0] - 1)
f_1 = diff(y)

ext_list = []
print(f'\n 5. Вычислить вершину: ')
for i, val in enumerate(f_diff):
    ext_list.append(f_1.subs(x, uniform(val, f_diff[i] + 1)))
    if i != 0:
        if ext_list[i - 1] < 0 < ext_list[i]:
            print(f"Точка минимума: {val}, {y.subs(x, val).evalf(2)}")
        elif ext_list[i - 1] > 0 > ext_list[i]:
            print(f"Точка максимума: {val}, {y.subs(x, val).evalf(2)}")

print(f'\n 6. Определить промежутки, на котором f > 0: ')
print(solve(y>0))


print(f'\n 7. Определить промежутки, на котором f < 0: ')
print(solve(y<0))