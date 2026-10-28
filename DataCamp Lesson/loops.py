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