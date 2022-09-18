# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k=int(input('Введите степень: '))
cof=[]
i=0
for i in range(k+1):
    i=random.randint(0,100)
    cof.append(str(i))
print(cof)
arr=[]
utf={0: "\u2070", 1: "\u00B9",2: "\u00B2",3: "\u00B3", 4: "\u2074", 5: "\u2075",
6: "\u2076", 7: "\u2077", 8: "\u2078", 9: "\u2079"}
for i in range((len(cof)-1), 1, (-1)):
    # if i<=9:
       arr.append('x'+utf[i]+"+")
    # if i>9:
    #     a=i/10
    #     b=i%10
    #     arr.append('x'+utf[a]+utf[b]"+")   
arr.append('x+')
arr.append('')
print(arr)
arr_new=[]
for i in range(len(cof)):
    arr_new.append(cof[i]+arr[i])
print(arr_new)
exs="".join(arr_new)
print(exs)

data=open('file2.txt', 'w', encoding='utf-8')
data.write(exs)
data.close()



