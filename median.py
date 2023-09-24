"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        # List comprehension. Splits the input spring into an array of numbers, and converts each int to a float.
        numbers = [float(value) for value in input().split(",")]
        # First we need to sort the list.
        sorted_nums = sorted(numbers)
        list_length = len(sorted_nums)
        median_position = list_length // 2

        if list_length % 2 == 1:
            print(sorted_nums[median_position])
        else:  
            print(((sorted_nums[median_position] + sorted_nums[median_position - 1]) / 2))
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
#print(numbers)
