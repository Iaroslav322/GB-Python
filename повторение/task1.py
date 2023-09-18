password = "12345"
count = 3

while count > 0:
    print ('Попытка', count)
    count -= 1
    res = input("Напишите пароль:")
    if res == password:
       print("Доступ открыт!")
    elif res != password:
       print("Доступ закрыт!")
    else:
         break 
else:
    print ("Истрачены все попытки ")  
    quit
        