""" naming_styles.py 
Example of Naming Styles and Choosing names according to the PEP-8
"""
from typing import List
from math import sqrt
#######################
#     Naming Styles
#######################

###### FUNCTIONS ######
# ✅ Recommended
def count_elements(numbers:List[int])-> int:
    return len(numbers)
# ❌ Not recommended
def ce(numbers):
    return len(numbers)

###### VARIABLES ######
# ✅ Recommended
my_list = [1, 2, 3]
filename = 'data.txt'
a = 5
# ❌ Not recommended
list = [1, 2, 3]
Filename = 'data.txt'
ocs = 5

###### CLASS ######
# ✅ Recommended
class Cookie:
    def __init__(self, color) -> None:
        self.color = color
# ❌ Not recommended
class cookie:
    def __init__(self, color) -> None:
        self.color = color
        
###### METHOD ######
# ✅ Recommended
class Cookie:
    def __init__(self, color) -> None:
        self.color = color
    def show_color(self) ->None:
        print(self.color)
# ❌ Not recommended
class cookie:
    def __init__(self, color) -> None:
        self.color = color
    def showColor(self) ->None:
        print(self.color)
        
###### CONSTANTS ######
# ✅ Recommended
LANGUAGE = 'Python'
FIRST_TERM_FIBONACCI = 0
GOLDEN_CONSTANT = (1 + sqrt(5)) / 2

# ❌ Not recommended
lenguage = 'Python'
FIRSTTERMFIBONACCI = 0
GoldenCONSTANT = (1 + sqrt(5)) / 2

#######################
#     Choose Names
#######################
###### VARS ######

# ✅ Recommended
full_name = "Alejandro Jaimes"
first_name, last_name = full_name.split()
print(f"{last_name}, {first_name}")

# ❌ Not recommended
c = "Alejandro Jaimes"
x, y = c.split()
print(f"{y}, {x}")

###### FUNCTIONS ######

# ✅ Recommended
def sum_odd_numbers(numbers: List[int]) ->int:
    return sum([number for number in numbers if number % 2 != 0])

# ❌ Not recommended
def sodd(numbers: List[int]) ->int:
    return sum([number for number in numbers if number % 2 != 0])