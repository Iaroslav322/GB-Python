#4. Напишите программу, которая принимает на вход 2 числа.
#Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
#Найдите произведение элементов на указанных позициях(не индексах).
f = open("file.txt", "r")
a, b = f.read().split("\n")
a, b = int(a)-1, int(b)-1
N = int(input("Введите количество чисел: "))
A = []
for i in range(-N, N+1):
    A.append(i)
res = A[a] * A[b]
print(f"Position one: {a+1}\nPosition two: {b+1}\nNumber of elements: {N}\n{A}\n{res}")