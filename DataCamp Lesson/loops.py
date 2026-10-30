total_ingredients = 7
ingredients_checked = 0

while ingredients_checked < total_ingredients:
    ingredients_checked += 1

    if ingredients_checked < 4:
        print("More than half remaining")
    elif ingredients_checked <= 6:
        print("Nearly finished checking")

    else:
        print("All ingredients verified!")

# PYTHON FUNCTONS TO BE USED 

recent_orders = [15.92, 28.50, 42.75, 18.99, 55.00, 31.25, 22.99, 67.50]

smallest_order = min(recent_orders)
largest_order = max(recent_orders)
total_revenue = sum(recent_orders)

print("Smallest order:", smallest_order)
print("Largest order:", largest_order)
print("Total revenue:", total_revenue)


# MODULES 
# String Module

import string

print(string.ascii_lowercase)

print(string.punctuation)


# BUILDING A VALID PASSOWRD

# def validate_passord(password):
#     if validate_passord(password) >= 8:
#         for char in password:
#             if char in string.punctuation:
#                 return True
#     return False
# is_valid = validate_passord(user_passorwd)

# print("Is the password Valid?", is_valid)


# ADDING A KEYWAORD ARGUMENNT.

product = 'Wireless Mouse'

def clean_text(text,lower=True):

    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        return clean_text.lower()
print(clean_text(product))


# CLACULATING A DISCOUNT.

original_price = 899.99

def calculate_discount(price,discount_percent=15,round_result=True):
    # SINGLE-LINE DOCSTRINGS 
    """Calculate the discount price of a product"""

    discount_price = price - (price*(discount_percent/100))

    if round_result == True:
        return round(discount_price, 2)
    else:
        return discount_price
    
final_price = calculate_discount(price=original_price,discount_percent=25,round_result=False)
print(final_price)
print(calculate_discount.__doc__)


def clean_text(text,lower=True):

    # MULTI-LINE DOCSTRINGS.
    """"
    Clean text by swapping spcaces to underscores and converting to lowercase.
        Args:
            text (str): A string to be cleaned.
            lower (bool): Whether to convert the text to lowercase.
        
        Returns:
            text (str): Cleaned string.
    """


    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        return clean_text.lower()
print(help(clean_text))


# ADDING ARBITRARY ARGUMENTS

def concat(*args):
    """Concatenates multiple string arguments with spaces between them."""

    result = ""

    for arg in args:
        result += " " + arg
    return result
print(concat("Python", "is", "great!"))