#2. Напишите программу для проверки ложности утверждения (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.
x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            print(x,'AND',y,'OR',z,'=',x and y or z)
