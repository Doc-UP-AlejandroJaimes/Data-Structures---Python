""" comments.py 
Example of comments according to the PEP-8
"""
from typing import Union
#######################
#     Comments
#######################

###### BLOCK COMMENTS ######
# preserve the 79-character line limit
# ✅ Recommended

def highest_element(numbers:int) -> int:
    # Loop over `number` foreach list of numbers and select the highest number
    # Comparing foreach element and returns the highest variable.
    highest = numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i] > highest:
            highest = numbers[i]
    return highest
        
# ❌ Not recommended
def highest_element(numbers:int) -> int:
    # Loop over `number` foreach list of numbers and select the highest number Comparing foreach element and returns the highest variable.
    highest = numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i] > highest:
            highest = numbers[i]
    return highest

###### PARAGRAPH BLOCK COMMENTS ######
# ✅ Recommended
def quadratic_equation(a:int, b:int, c:int) -> Union[float, float]:
    # Calculate the solution to a quadratic equation using the quadratic
    # formula.
    #
    # A quadratic equation has the following form:
    # ax**2 + bx + c = 0
    #
    # There are always two solutions to a quadratic equation, x_1 and x_2.
    x_1 = (-b + (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    x_2 = (-b - (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    return x_1, x_2

###### INLINE COMMENT ######
# ✅ Recommended
student_name = "John Smith"
# ❌ Not recommended
x = "John Smith"  # Student Name

###### DOCUMENT STRINGS ######
# ✅ Recommended
def adder(a, b):
    """Add a to b."""
    return a + b
def quadratic_equation(a:int, b:int, c:int) -> Union[float, float]:
    """ Calculate the solution to a quadratic equation using the quadratic
        formula.
        
        A quadratic equation has the following form:
        ax**2 + bx + c = 0
        
        There are always two solutions to a quadratic equation, x_1 and x_2.
        
    Args:
        a (int): term
        b (int): term
        c (int): term

    Returns:
        Union[float, float]: return both solutions
    """
    x_1 = (-b + (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    x_2 = (-b - (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    return x_1, x_2