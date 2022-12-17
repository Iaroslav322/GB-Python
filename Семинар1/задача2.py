#2. Напишите программу для проверки ложности утверждения (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(not (x or y or z or w) == (not x and not y and not z and not w))
                print(x, y, z, w)