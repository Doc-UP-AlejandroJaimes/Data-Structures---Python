

def highest_element(numbers: int) -> int:
    # Loop over `number` foreach list of numbers and select the highest number
    # Comparing foreach element and returns the highest variable.
    highest = numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i] > highest:
            highest = numbers[i]
    return highest
