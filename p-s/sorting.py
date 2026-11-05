# SORTING
# Sorting mean arranging items in a particular order.

"""python give us 2 ways to sort data
1. sorted(): this create new sorted list without changing dthe original list."""
numbers = [8, 3, 10, 1]

result = sorted(numbers)
print(result)
print(numbers)

"""2. .sorted(): this sorts the original list directly. it changes the existing list rather than creating a new one."""
numbers = [8, 3, 10, 1]
numbers.sort()
print(numbers)


scores = [45, 90, 20, 75]
new_scores = sorted(scores, reverse=True)

print(new_scores)
print(scores)

# Write one line of Python code that creates a new list called ascending_temps, containing the temperatures arranged from the lowest to the highest.
temperature = [32, 18, 25, 40, 15]

ascending_temps = sorted(temperature)
print(ascending_temps)
print(temperature)