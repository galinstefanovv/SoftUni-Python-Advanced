def shop_from_grocery_list(*data):
    budget = data[0]
    inventory = data[1]
    purchased = []
    for product in data[2::]:
        product_name = product[0]
        product_price = float(product[1])
        if product_name not in purchased and product_name in inventory:
            if budget >= product_price:
                budget = abs(budget - product_price)
                purchased.append(product_name)
                inventory.remove(product_name)
            else:
                break
    if len(inventory) == 0:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(str(x) for x in inventory)}."




print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))