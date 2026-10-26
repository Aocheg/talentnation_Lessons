# STRINGS MANIPULATIONS
# 1. Strings Methods (Tools)

order = "    lAtTe    "


cleaned = order.strip()

proper = order.strip().title()

order_name = "     espresso     "


print(cleaned)
print(proper)
print(order_name.strip().upper())

# 2. String Slicing(Extract part of the Text)

order_1 = "Latte"

abbreviation = order_1[:3]
print(abbreviation)

name = "Gabriel"
print(name[:3])

# 3. String Formatting(Inserting Variables)

order_name = "Godson"
drink = "Latte"
price = 4.50

reciept = f"Order for {order_name}: {drink} N{price:.2f}"

print(reciept)