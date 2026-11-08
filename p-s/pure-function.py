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

# Important: A function returning a value does not automatically make it pure. 
# We must also consider whether it changes external state."""

# 2 types of functions 
# """1. Inpure Functions: this function usually depend of variable from ouside the 
# function or outside its input  to give its required results.
# e.g declaring a global variable and using it inside a function"""

discount = 100

def calculate_price(price):
    return price - discount
print(calculate_price(1000))

# """2. Pure Functions: This functions does not depend on any external variables 
# to get its result, it receives all it need through its arguments 
# and avoid external side effect."""

def calculate_price(price, discount):
    return price - discount
print(calculate_price(1000, 100))

# independent drills on functions

# Imagine you're managing a library. You want to calculate how many books 
#remain after some books are borrowed.

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
"""- It receives all necessary information through its parameters.
- It doesn't depend on global variables.
- It doesn't modify external data.
- The same inputs always produce the same output.
"""

# understanding side effect

books = ["python", "Java", "Go"]

def add_book(book):
    books.append(book)
    return books
print(add_book(books))
# The above function is a inpure function because it has an external
# variable modfying the orginal output.

def add_book(books, book):
    new_books = books + [book]
    return new_books


# The above is a pure function because:

"""It receives books and book as arguments.
It doesn't depend on a global variable.
books + [book] creates a new list rather than modifying the original list.
It returns the new list without changing the caller's original list.
"""

"""Important: Passing an external object as an argument doesn't automatically 
make a function pure. What matters is whether the function modifies that object 
or causes other side effects."""

# Edge Cases
def calculate_discount(price, discount):
    if discount >0:
        return price - discount
    return price
print(calculate_discount(1000, 100))
print(calculate_discount(1000, 0))
print(calculate_discount(1000, -50))
""" the above function is a pure function with the following reasons
 - It receives all the information it needs through its parameters.
- It does not depend on external variables.
- It does not modify external data.
- The same inputs always produce the same outputs.

Important lesson: A function does not become impure simply because it receives zero or 
a negative number. 
Purity is about how the function behaves, not whether its input values are unusual."""