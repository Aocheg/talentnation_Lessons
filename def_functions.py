# DEFINING FUNCTIONS

def brew_coffee():
    print("Grinding espresso beans")
    print("Brewing hot coffee into the cup")
    print("coffee is ready")
brew_coffee()

def greet_brista():
    print("Hello, brista!")
greet_brista()


# Function with Parameters(Accepting input)
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