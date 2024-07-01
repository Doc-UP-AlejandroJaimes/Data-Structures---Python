"""
Represents concept Big O(n)
"""
def print_items(n:int)->None:
    for item in range(1, n + 1):
        print(item)
        
def run()->None:
    n = 15
    print_items(n)
    
if __name__ == "__main__":
    run()