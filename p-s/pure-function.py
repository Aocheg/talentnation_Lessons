# PURE FUNCTIONS
"""A pure function is a function that allows two important rules:
1. Given the same inputs, it always produces the same output.
it does not modify or affect anythin outside itself(no side effects)."""

def calculate_total(price, quantity):
    return price * quantity
print(calculate_total(500,3))

# In the code above the result depend entirely on the inputs.

# SIDE EFFECT
"""A side effect happens when a function changes something outside its local calculation"""

shop_balance = 5000

def add_to_balance(amount):
    global shop_balance
    shop_balance += amount
    return shop_balance

# """Pure functions are easier to:
# - Test because their outputs are predictable.
# - Debug because they don't secretly modify external state.
# - Reuse because they depend on their inputs.
# - Maintain because their behaviour is easier to understand.

# Important: A function returning a value does not automatically make it pure. We must also consider whether it changes external state."""

# 2 types of functions 
# """1. Inpure Functions: this function usually depend of variable from ouside the function or outside its input  to give its required results.
# e.g declaring a global variable and using it inside a function"""

discount = 100

def calculate_price(price):
    return price - discount
print(calculate_price(1000))

# """2. Pure Functions: This functions does not depend on any external variables to get its result, it receives all it need through its arguments 
# and avoid external side effect."""

def calculate_price(price, discount):
    return price - discount
print(calculate_price(1000, 100))

# independent drills on functions

# Imagine you're managing a library. You want to calculate how many books remain after some books are borrowed.

# Your task is to write a function called: calculate_remaining_books()

# It should accept:
# - total_books
# - borrowed_books
# It should return the number of books remaining.

# Your challenge:

# Write the function yourself.

def calculate_remaining_books(total_books, borrowed_books):
    return total_books - borrowed_books
print(calculate_remaining_books(20,5))

# The above function is a Pure function because:
# - It receives all necessary information through its parameters.
# - It doesn't depend on global variables.
# - It doesn't modify external data.
# - The same inputs always produce the same output.