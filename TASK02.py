# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

N=int(input('Введите число: '))

mnog=[]
i=2
while i<=N:
    while N%i==0:
       mnog.append(i)
       N=N/i
    i+=1
print(f'простые множетели введенного числ {mnog}')