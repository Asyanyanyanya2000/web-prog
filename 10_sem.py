#конспесты Максима 
'''
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print(f"Животное с именем - {self.name} удаленно")

    
    def speak(self):
        raise NotImplementedError("Subclass mast imlement abstract metod")

class Dog(Animal):
    species = "Canis familiar"
    sound = "woof"
    def speak(self):
            return f"{self.name} says {self.sound}"

    def years(self):
        return self.age *7 
        
class Cat(Animal):
    sound = "meaw"
    # def speak(self):
    #     return f"{self.name} says meaw"
    def speak(self):
        return f"{self.name} says {self.sound}"

# dog = Dog("Rex", 3)

# cat = Cat("Puff", 2)

# print(dog.name)
# print(dog.species)
# print(dog.speak())
# print(cat.name)
# print(cat.speak())


animals = [Dog("Rex",3), Cat("Puff", 2)]

for animal in animals:
    print(animal.speak())
'''
#и следущие занятие

'''
class TrCh:
    def __init__(self,sides):
        self.sides = sides
    
    def is_tr(self):
        if all(isinstance(side,(int,float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sort_s=sorted(self.sides)
                if sort_s[0]+sort_s[1]>sort_s[2]:
                    return 'можно'
                return "жаль, не выйдет"
            return "c отрицательными числами ничего не выйдет"
        return 'вводите только числа'

triang1= TrCh([2,3,4])
triang2= TrCh([-2,3,4])
triang3= TrCh(["2",3,4])
print (triang1.is_tr())
'''

'''
class Ni:
    def __init__(self,name,age):
        if name=='Николай':
            self.name=name
        else:
            self.name= f"no, {name} is NIk"
        self.age=age

u1= Ni("ynj",13)
print(u1.name)

'''