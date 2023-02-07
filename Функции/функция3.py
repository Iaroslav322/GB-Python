import sympy


print('\n 1. Определить корни')
x = sympy.Symbol('x')
a = sympy.solve((x ** 2 + 3) / (3 * (x + 1)),x)
print(a)

print(f'\n 2. Найти интервалы, на которых функция возрастает: ')
print(sympy.solve((x ** 2 + 3) / (3 * (x + 1)) > 0,x))
print(f'\n 3. Найти интервалы, на которых функция убывает: ')
print(sympy.solve((x ** 2 + 3) / (3 * (x + 1)) < 0,x))

print("4. Построить график")
sympy.plotting.plot((x ** 2 + 3) / (3 * (x + 1)))

print(f'\n 5. Вычислить вершину: ')
f = (x ** 2 + 3) / (3 * (x + 1))
diff =  sympy.diff(f,x)
print(diff)
print(sympy.solve(diff,x))

print(f'\n 6. Определить промежутки, на котором f > 0: ')
print(sympy.solve(diff > 0,x))
print(f'\n 7. Определить промежутки, на котором f < 0: ')
print(sympy.solve(diff < 0,x))
