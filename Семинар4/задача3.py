#3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
n = int(input("Введите число: "))
from random import random
data = []
for j in range(n):
    data.append(int(random()*n))
print (data)

s = []
for i in data:
    if data.count(i) == 1:
        s.append(i)
print(s)        
