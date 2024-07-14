"""
Represents concept Big O(1)

Example: Accessing an array element by its index
"""
from typing import List

def search_element_by_index(array:List[int], value:int)-> int:
    try:
      value = array.index(value)
      return value
    except ValueError:
      print("The value doesn't exist")
      return 0

if __name__ == "__main__":
    array = [54, 65, 12, 65, 123]
    print(search_element_by_index(array, 615))