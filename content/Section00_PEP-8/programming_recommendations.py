""" programming_recommendations.py 
"""
#######################
#     Programming Recommendations
#######################

###### Don’t compare Boolean values to True 
###### or False using the equivalence operator

# ✅ Recommended
def is_bigger(number_1:int, number_2:int) ->str:
    is_bigger = number_1 > number_2
    if is_bigger:
        return f"{number_2} is bigger than {number_1}"

# ❌ Not recommended
def is_bigger(number_1:int, number_2:int) ->str:
    is_bigger = number_1 > number_2
    if is_bigger == True:
        return f"{number_2} is bigger than {number_1}"

###### Use the fact that empty sequences
###### are falsy in if statements
# ✅ Recommended
def check_empty_list(a_list:list) ->None:
    if not a_list:
        print("List is empty!")

# ❌ Not recommended
def check_empty_list(a_list:list) ->None:
    if not a_list:
        print("List is empty!")
        
###### Use is not rather than not 
###### ... is in if statements
# ✅ Recommended
def check_defined_value(value:int) ->str:
    if value is not None:
        return "x exists!"

# ❌ Not recommended
def check_defined_value(value:int) ->str:
    if not value is None:
        return "x exists!"

###### Don’t use if x: when you mean 
###### if x is not None:. 
# ✅ Recommended
def check_defined_value(value:int) ->str:
    if value is not None:
        return "x exists!"

# ❌ Not recommended
def check_defined_value(value:int) ->str:
    if value:
        return "x exists!"
    
###### Use .startswith() and .endswith()
###### instead of slicing.
# ✅ Recommended
word = "cat"
file_name = "whatsapp_ph_01.jpg"

if word.startswith("cat"):
    print("The word starts with 'cat'")
if file_name.endswith(".jpg"):
    print("The file is a JPEG")

# ❌ Not recommended
if word[:3] == "cat":
    print("The word starts with 'cat'")

if file_name[-4:] == ".jpg":
    print("The file is a JPEG")