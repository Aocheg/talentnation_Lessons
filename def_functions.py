# DEFINING FUNCTIONS
# 1.Defining function

def brew_coffee():
    print("Grinding espresso beans")
    print("Brewing hot coffee into the cup")
    print("coffee is ready")
brew_coffee()

def greet_brista():
    print("Hello, brista!")
greet_brista()


#2.  Function with Parameters(Accepting input)
# adding a placeholder variable into functions

def print_cup_label(customer_name):
    print("-----------------------")
    print("Order: Hot Latte")
    print("Name: "+ customer_name)
    print("------------------------")
print_cup_label("Joy")
print_cup_label("James")

# Using Parameter for Isolation

def print_label(name):
    print("Name on cup:"+ name)

# Pass the data directly into the cell
print_label("John")
print_label("Joyce")
# This print_label function works because is completely 
# isolated and safe. You can pass any strings argument
# directly into the parentheses and it will bind that value to the paremeter locally.

def order_drink(drink, size):
    print("Dispensing "+size + " " + drink)
order_drink("espresso", "large")

# 3 Functions with Return Values (Producing Output)

cups_ordered = 3
price_per_cup = 4.50
customer_receipt = ""

def calculate_price(count, cost):
    total = count * cost
    return total
customer_receipt = calculate_price(cups_ordered, price_per_cup)
print(customer_receipt)

def add_tax(subtotal):
    return subtotal * 1.08
final_total = add_tax(10.0)
print(final_total)