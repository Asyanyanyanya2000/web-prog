#конспект 8 занятия

'''
# Создайте словарь, который хранит информацию о человеке. Допустим, человека зовут "Том", ему 39 лет, 
# он работает в компание SuperCorp и в работе использует языки программирования Python и JavaScript. 
# Сохраните всю эту информацию в словаре. Затем выведите эту информацию из словаря на консоль

person = {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]}
 
print("Name: ", person.get("name"))
print("Age: ", person["age"])
print("Company: ", person["company"])
print("Languages: ", person["languages"])

# Пусть дан следующий список, которые хранит несколько словарей:

people = [
    {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
    {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
    {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
]

# Каждый словарь в списке представляет программиста, где поле "name" представляет имя,
#  а поле "languages" - список используемых языков программирования. 
# Выведите на консоль из каждого словаря имя и последний язык программирования, чтобы получился следуюший консольный вывод:

# Name:  Tom
# Last language:  JavaScript
# Name:  Bob
# Last language:  C#
# Name:  Sam
# Last language:  Java

'''
#домашнюю не дали