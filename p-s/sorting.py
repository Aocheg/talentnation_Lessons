# SORTING.
# Sorting mean arranging items in a particular order

"""python give us 2 ways to sort data
1. sorted(): this create new sorted list without changing dthe original list."""
numbers = [8, 3, 10, 1]

result = sorted(numbers)
print(result)
print(numbers)

"""2. .sorted(): this sorts the original list directly. it changes the existing list rather than creating a new one"""
numbers = [8, 3, 10, 1]
numbers.sort()
print(numbers)


scores = [45, 90, 20, 75]
new_scores = sorted(scores, reverse=True)

print(new_scores)
print(scores)

# Write one line of Python code that creates a new list called ascending_temps, 
# containing the temperatures arranged from the lowest to the highest.
temperature = [32, 18, 25, 40, 15]

ascending_temps = sorted(temperature)
print(ascending_temps)
print(temperature)

# The above code identified that: 
"""sorted() arranges values in ascending order by default.
Assigning the result to ascending_temps stores the new sorted list.
The original temperatures list remains unchanged."""

prices = [500, 200, 800, 100]

result = prices.sort()

print(result)
print(prices)

"""Remember this distinction:
- sorted() sorts and returns a new list.
- .sort() sorts the original list and returns None."""


numbers = [5, 2, 8, 1]
numbers.sort(reverse=True)
print(numbers)

"""What I have learned
- .sort() modifies the original list.
- reverse=True changes the sorting direction to descending.
- .sort() still returns None; reverse=True does not change that."""