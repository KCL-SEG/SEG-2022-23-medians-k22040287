# Ayan Mahmood - medians task
def medianGet(numbers):
    if len(numbers) % 2 == 0:
        return f"{(numbers[int(len(numbers) / 2)])}/{(numbers[(int(len(numbers) / 2) - 1)])}"
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
