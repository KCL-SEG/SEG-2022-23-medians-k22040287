# Ayan Mahmood - medians task

# import floor from maths module
from math import floor

def medianGet(numbers):
    numbers.sort()
    print(numbers)
    middle = 0
    if len(numbers) % 2 == 0:
        middle == len(numbers) // 2
        print(numbers[middle + 1])
        print(numbers[middle])
        return (numbers[(middle + 1)] + numbers[middle]) / 2
    else:
        return numbers[int(len(numbers) / 2)]

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break


print(medianGet(numbers))
