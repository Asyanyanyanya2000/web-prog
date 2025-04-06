#переименовать в просто 9 сем пу

#напишите функцию которая сортирует кортеж, состоит из целых чисел по возрастанию и возвращает его 
# если хотя бы 1 элемент не является целым числом нужно вернуть кортеж в изначальном виде 
#  b.insert(0,i)
'''
def tpl_sort(a):
    for i in a:
        if i%1>0:
            return a
    return tuple(sorted(a))
tpl=(1,2,4,3,5,7)
print(tpl_sort(tpl))
'''

#принимаеит картеж и случ элемент. найти все от первого вхождения элемента до второго
# и создать с этим второй кортеж 
'''
def slicer(a,el):
    for i in a:
        if el == i:

'''
'''
def slicer(a,el):
    if el in a:
        if a.count(el)>1:
            first=a.index(el)
            second=a.index(el,first+1)+1
            return a[first,second]
        else:
            return a[a.index(el):]
    else:
        return()

a=3
tpl=(1,2,4,3,5,7)
print(slicer(tpl,a))
'''

#дан словарь(нет), вывести оценку по истории и имя

#прринт(наименование кортежа[куда зайти][насколько][глубоко][ключии!])
#{ключ:значение, и тп}
'''
t={'cl':[{'a':{'b':10}},{'a':{'b':20}},{'a':{'b':30}}]}
for inex in t['cl']:
    print(inex['a']['b'])
'''

#копия с доски
'''
# Напишите функцию tpl_sort(), которая сортирует кортеж, состоит и целых чисел по возрастанию,
# и возвращает его. Если хотя бы один элемент не является целым числом, вернуть кортеж в 
# изначальном виде

# def tpl_sort(tpl):
#     for c in tpl:
#         if c%1 > 0:
#             return tpl
#     return tuple(sorted(tpl))
# tpl = (1,3.125,2,4,5)
# print(tpl_sort(tpl))

# Функция slicer() на вход принимает кортеж и случайный элемент. 
# Требуется вернуть новый кортеж, начинающийся с первого появления элемента 
# в нем и заканчивающийся вторым его появлением включительно.
# Если элемента нет вовсе – вернуть пустой кортеж.
# Если элемент встречается только один раз, то вернуть кортеж, 
# который начинается с него и идет до конца исходного.

# def slicer(tpl, elem):
#     if elem in tpl:
#         if tpl.count(elem) > 1:
#             first = tpl.index(elem)
#             second = tpl.index(elem, first+1)+1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(elem):]
#     else:
#         return ()
# tpl = (1,3.125,2,4,5,2)
# print(slicer(tpl,11))

# Дан словарь {'class':{'student':{'name':'Mike','marks':{'physics':70,'history':80}}}}. 
# Выведите на экран имя студента и его оценку по истории

# test = {'class':[{'student':{'name':'Mike','marks':{'physics':70,'history':80}}},
#                 {'student':{'name':'Max','marks':{'physics':30,'history':90}}},
#                 {'student':{'name':'Lake','marks':{'physics':11,'history':50}}}]
#         }

# for student in test['class']:
#     print("Имя студента: ", student['student']['name'])
#     for (name, mark) in student['student']['marks'].items():
#         print("Оценка по" , name, ":", mark)
#     print()
'''