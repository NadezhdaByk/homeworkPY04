# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

with open('file.txt', 'r', encoding='utf-8') as file:
    arr1 = [str(i) for i in file.read()]
with open('file1.txt', 'r', encoding='utf-8') as file:
    arr2 = [str(i) for i in file.read()]
print(arr1)
print(arr2)

for i in range(len(arr1)-1):
    if arr1[i]=='^':
       arr1[i+1]='x'
for i in range(len(arr2)-1):
    if arr2[i]=='^':
       arr2[i+1]='x'
print(arr1)
print(arr2)

while "x" in arr1:
       arr1.remove("x") 
while "x" in arr2:
       arr2.remove("x")
print(arr1)
print(arr2)

while "^" in arr1:
       arr1.remove("^") 
while "^" in arr2:
       arr2.remove("^")
print(arr1)
print(arr2)    

mnog1="".join(arr1)
mnog2="".join(arr2)
print(mnog1)
print(mnog2)
arr1=list(mnog1.split('+'))
print(arr1)
arr2=list(mnog2.split('+'))
print(arr2)
arr=[]
for i in range(len(arr1)):
    arr1[i]=int(arr1[i])
    arr2[i]=int(arr2[i])
    arr.append(arr1[i]+arr2[i])
print(arr)

arr_new=[]
for i in range(len(arr)-2):
    j=len(arr)-i-1
    arr_new.append(str(arr[i])+'x^'+str(j))
arr_new.append(str(arr[len(arr)-2])+'x')
arr_new.append(str(arr[len(arr)-1]))
print(arr_new)

mnog_itog="+".join(arr_new)
print(mnog_itog)

data=open('file3.txt', 'w', encoding='utf-8')
data.write(mnog_itog)
data.close()