#5. Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
with open('mn_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('mn_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('mn_1.txt','r') as file:
    mn_1 = file.readline()
    list_of_mn_1 = mn_1.split()


with open('mn_2.txt','r') as file:
    mn_2 = file.readline()
    list_of_mn_2 = mn_2.split()

print(f'{list_of_mn_1} + {list_of_mn_2}')
sum_mn = list_of_mn_1 + list_of_mn_2

with open('sum_mn.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_mn_1} + {list_of_mn_2}')


#sum_of_mn = (list_of_mn_1), '+' (list_of_mn_2)




if len(mn_1) > len(mn_2):
    help_mn = mn_1
    mn_1 = mn_2
    mn_2=help_mn
mn_1 = mn_1.split(' + ')
mn_2 = mn_2.split(' + ')
print(mn_1,mn_2)

count1 =0
count2=len(mn_2)-len(mn_1)
new_mn = ''
for i in range(count2):
    new_mn += mn_2[i] + '+'

ind1 = ''
ind2 = ''

for i in range(len(mn_2) - len(mn_1), len(mn_2)):
    result = 0 
    if i == len(mn_2) - 1:
        result += int(mn_1[-1][:-4]+mn_2[-1][:-4])
        new_mn += str(result) + mn_1[-1][-4:]
    elif i == len(mn_2) - 2:
        result += int(mn_1[-2][:-2]+mn_2[-2][:-2])
        new_mn += str(result) + mn_1[-2][-2:] + ' + ' 
    else:
        result += int(mn_1[count1][:-4]+mn_2[count2][:-4])
        new_mn += str(result) + mn_1[count1][-4:] + ' + ' 
        count1 += 1
        count2 += 2
print(new_mn)