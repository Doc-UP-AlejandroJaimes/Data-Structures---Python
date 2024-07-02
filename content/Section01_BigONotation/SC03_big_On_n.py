"""
Represents concept Big O(n^2)

Example: Sort list with bubble sort.
"""
def bubble_sort(array: list[int])->list[int]:
    # auxiliar variables
    i = 0
    swapped = True
    swaps = 0
    while(swapped):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                swaps += 1
        if swaps == 0:
            swapped = False
        else:
            swaps = 0    
    return array
        
def run()->None:
    array = [3,1,2,6,4,7,5]
    sorted_array = bubble_sort(array)
    print(sorted_array)
    
if __name__ == "__main__":
    run()