""" whitespace.py 
Example of white spaces according to the PEP-8
"""
from typing import Union
#######################
#     Whitespace in Expressions and Statements
#######################

###### Whitespace Around Binary Operators ######
# ✅ Recommended
def function(default_parameter=5):
    pass
    # ...

# ❌ Not recommended
def function(default_parameter = 5):
    pass
    # ...

######  Avoiding whitespace for indicating default value ######
# ✅ Recommended
x = 10
y = x**2 + 5
z = (x+y) * (x-y)

if x>5 and x%2==0:
    print("x is larger than 5 and divisible by 2!")

a_list = [1, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
a_list[3:4]

# Treat the colon as the operator with lowest priority.
a_list[x+1 : x+2]

# In an extended slice, you must surround both colons
# with the same amount of whitespace.
a_list[3:4:5]
a_list[x+1 : x+2 : x+3]

# You omit the space if you omit a slice parameter.
a_list[x+1 : x+2 :]

# ❌ Not recommended
y = x ** 2 + 5
z = (x + y) * (x - y)

if x >5 and x% 2== 0:
    print("x is larger than 5 and divisible by 2!")
    
if x > 5 and x % 2 == 0:
    print("x is larger than 5 and divisible by 2!")