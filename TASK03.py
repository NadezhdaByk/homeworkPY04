# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов
# исходной последовательности.

string=input('Введите последовательность чисел без пробела: ')
spisok=list(string)
sp_new=[]

for i in range(len(spisok)):
    j=0
    flag=1
    while j<len(spisok) and flag==1:
        if spisok[i]==spisok[j] and i!=j:
            flag=0
        j+=1
    if flag==1:
        sp_new.append(spisok[i])
if sp_new==[]:
    print('все числа повторяются')
else:
    print(f'неповторяющиеся числа {sp_new}')