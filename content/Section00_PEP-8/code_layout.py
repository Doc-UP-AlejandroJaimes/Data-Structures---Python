""" code_layout.py 
Example of code layout according to the PEP-8
"""
from typing import List
#######################
#     Blank Likes
#######################

###### Two blank lines: class and top-level functions ######
# ✅ Recommended
class Animal:
    def __init__(self, name:str, food:str, age:int) -> None:
        self.name = name
        self.food = food
        self.age  = age
        
        
class Dog(Animal):
    def __init__(self, breed:str) -> None:
        self.breed = breed
        
# ❌ Not recommended
class Animal:
    def __init__(self,name,food,age):
        self.name = name
        self.food = food
        self.age  = age
class Dog(Animal):
    def __init__(self, breed:str) -> None:
        self.breed = breed

###### One blank lines: methods ######
# ✅ Recommended
class Animal:
    def __init__(self, name:str, food:str, age:int) -> None:
        self.name = name
        self.food = food
        self.age  = age
        
    def eat(self):
        return f'The animal called {self.name} eat {self.food}'
    
        
class Dog(Animal):
    def __init__(self, breed:str) -> None:
        self.breed = breed
        
    def bark(self)->None:
        print("I can bark! Woof woof!!")
        
# ❌ Not recommended
class Animal:
    def __init__(self,name,food,age):
        self.name = name
        self.food = food
        self.age  = age
    def eat(self):
        return 'The animal called',self.name,' eat ', self.food
class Dog(Animal):
    def __init__(self, breed:str) -> None:
        self.breed = breed
    def bark(self)->None:
        print("I can bark! Woof woof!!")

###### blank lines sparingly inside functions to show clear steps ######
# ✅ Recommended
def calculate_variance(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers = sum_numbers + number
    mean = sum_numbers / len(numbers)

    sum_squares = 0
    for number in numbers:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(numbers)

    return mean_squares - mean**2
# ❌ Not recommended
def calculate_variance(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers = sum_numbers + number
    mean = sum_numbers / len(numbers)
    sum_squares = 0
    for number in numbers:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(numbers)
    return mean_squares - mean**2