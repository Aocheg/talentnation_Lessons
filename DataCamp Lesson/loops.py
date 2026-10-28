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

