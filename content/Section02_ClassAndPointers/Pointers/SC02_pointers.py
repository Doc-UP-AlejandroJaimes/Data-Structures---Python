"""Pointers

Accesing to the same pointers and show

"""

person = {"Name": "Jhon Doe", "Age": 32, "Phone": "+573158748986"}

person2 = person
# person2["name"] = "Jane Reynolds"
# check reference to the person
print(f"Person Object 1 Id: {id(person)}")
print(f"Person Object 2 Id: {id(person2)}")

# create copy of object and change element
person2 = person.copy()
person2["name"] = "Jane Reynolds"
print("After copy person in person2 and change value name")
print(f"Person Object 1 Id: {id(person)}")
print(f"Person Object 2 Id: {id(person2)}")
