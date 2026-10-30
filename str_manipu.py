# STRINGS MANIPULATIONS
# 1. Strings Methods (Tools)

order = "    lAtTe    "


cleaned = order.strip()

proper = order.strip().title()

order_name = "   espresso   "


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

customer_name = "Golden"
total = 12.0
print(f"Thank you, {customer_name}! Total: N{total:.2f}")


# 4. Splitting and Joining of Strings

raw_order_list = "late,espresso,mocha"
menu_display = ""

# split the comma-seperated string into a list
items = raw_order_list.split(",")

# join the list using newline charater(\n) as the seperator

menu_display = "\n".join(items)

print(menu_display)


sentence = "latte and espresso"
words = sentence.split(" and ")
print(words)

rejoin = "-".join(words)
print(rejoin)




