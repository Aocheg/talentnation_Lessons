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