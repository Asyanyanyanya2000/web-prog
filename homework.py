# 1
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. 
# Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N - 1 номер оставшихся карточек (различные числа от 1 до N). 
# Программа должна вывести номер потерянной карточки.
'''
def fact(a):
    if a == 1:
        return a
    else:
        return a * fact(a - 1)

def card(n):
    a= fact(n)
    for i in range(n-1):
        x=int(input())
        a/=x
    return int(a)

def text(a):
    if a==0:
        print( "проверьте количество всех карт в колоде")
    else:
        print ("вот поретянная карта: ",a)

n=int(input("введите количество всех карт, а после все найденные:"))
text(card(n))
'''
# 2
# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
'''
a= str(input('введите строку: '))
b=0
for i in range(len(a)): 
    if i%3==0:
        a= a[:i-b]+a[i-b+1:]
        b+=1
    
print (a)
'''

# 3
# Дано натуральное число A. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A. 
'''
a = int(input("введите число фибоначи: "))
x0,x1,xa=0,1,a-1
i=1
while a>=xa:
    if a==xa:
        print ('номер в ряду:', i)
        break 
    xa,x0=x1 + x0,x1
    x1=xa
    i+=1
if a<xa:
    print ('не является числом Фибоначчи')
'''

# 4
# Дана последовательность натуральных чисел x1, x2, ..., xn
# Стандартным отклонением называется величина:
# σ=√(((x1-s)2+(x2-s)2+…+(xn-s))/(2n-1))
# где s=(x1+x2+…+xn)/n — среднее арифметическое последовательности.
# Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
'''
sum = 0
arr = []
a = ''
while a != 0:
    a = int(input('ведите натуральное чило, для остановки 0: '))
    sum += a
    arr.append(a)

s = sum / (len(arr) - 1)

answer = 0
for i in arr[:-1]:
    answer += (i - s) ** 2
    
print('стандартное отклонение:',(answer / (len(arr) - 2))**0.5)
'''
# 5
# треугольник Паскаля

n=int(input('введите количество строк: '))
nom = [1]
i=0

def new_row(arr):
    j=0
    row = []
    while j <= int(len(arr)):
        if j==0 or int(len(arr))==int(len(row)) :
            row.append(1)
        else:
            a=int(arr[j-1])+int(arr[j])
            row.append(a)
        j+=1 
    return row

while i<n:
    print(nom)
    i+=1
    nom = new_row(nom)

'''
while i<n:
    print(nom)
    i+=1
    j=0
    row = []
    while j <= int(len(nom)):
        if j==0 or int(len(nom))==int(len(row)) :
            row.append(1)
        else:
            a=int(nom[j-1])+int(nom[j])
            row.append(a)
        j+=1 
    nom = row
'''