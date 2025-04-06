#вновь конспект старосты
'''
# import random

# def view_arr(arr2):
#     for i in arr2:
#         print(end="\n")
#         for j in range(len(i)):
#             if j==len(i)-1:
#                 print(i[j], end=";")
#             else:
#                 print(i[j], end=",")
#     print(end="\n")

# # arr2 = [[1,2,3,4], [5,6,7,8]]

# # print (arr2)

# def get_random_array(size, crit):
#     arr = random.choices(range(crit), k=size)
#     return arr

# def create_multi_arr(row,col,crit):
#     arr2 = []
#     for i in range(row):
#         arr2.append(get_random_array(col, crit))
#     return arr2

# view_arr(create_multi_arr(3,3,10))
'''

#теперь домашка (не факт что к этой паре, хаха)

#Задача 1: Задайте двумерный массив символов (тип char [,]).
#Создать строку из символов этого массива.
'''
arr=[['a','b','c'],['d','e','f']]
for i in arr:
    for j in i: 
        print (j, end='')
'''

#Задача 2: Задайте строку, содержащую латинские буквы в
#обоих регистрах. Сформируйте строку, в которой все
#заглавные буквы заменены на строчные.
'''
a= 'AbCdEfG'
print(a.lower())
'''

#Задача 3: Задайте произвольную строку. Выясните, является
#ли оно палиндромом
'''
text= "учуя молоко я около мяучу"
#text= 'просто текст без приколов'
REtext=text[::-1]

if text.replace(' ', '')==REtext.replace(' ', ''):
    print ("да")
else:
    print("нет")
'''

#Задача 4*(необязательная): Задайте строку, состоящую из
#слов, разделенных пробелами. Сформировать строку, в
#которой слова расположены в обратном порядке. В полученной
#строке слова должны быть также разделены пробелами.
'''
text= "учуя молоко я около мяучу"
for i in text.split():
    print(i, end=' ')
'''
#всё