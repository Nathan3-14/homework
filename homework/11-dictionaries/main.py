import json

with open("./shop.json", "r") as f:
    shop = json.load(f)

item_just = 9
colour_just = item_just + 10

display_shop = {
    f"{item.split('_')[0].ljust(item_just).capitalize()} {item.split('_')[1].capitalize()}": price for item, price in shop.items()
}

print(" - Item".ljust(item_just+4) + "Pattern".ljust(item_just+1) + "Price" + "\n")
print("".join(f" - {str((item+':')).ljust(colour_just)} £{format(price/100, '.2f')}\n" for item, price in display_shop.items()))