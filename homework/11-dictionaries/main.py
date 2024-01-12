import json

with open("./shop.json", "r") as f:
    shop = json.load(f)

item_just = 9
colour_just = item_just + 10

display_shop = {
    f"{item.split('_')[0].ljust(item_just).capitalize()} {item.split('_')[1].capitalize()}": price for item, price in shop.items()
}
cart = []
codes = {
    "50off": 0.5,
    "50on": 1.5,
    "free": 0
}

while True:
    print(" - Item".ljust(item_just+4) + "Pattern".ljust(item_just+1) + "Price  "  + "\n")
    print("".join(f" - {str((item+':')).ljust(colour_just)} £{format(price/100, '.2f')}   ({list(shop.keys())[list(display_shop.keys()).index(item)]})\n" for item, price in display_shop.items()))

    buying = input("Enter an item to buy or exit to exit\n>> ").lower()

    if buying == "exit":
        break

    if buying in shop:
        cart.append(shop[buying])
    else:
        print("Item not recognised")

total = 0
for cost in cart:
    total += cost

code = input("Enter any discount codes you may have\n>> ")
if code in codes.keys():
    total *= codes[code]

print(f"Total: £{format(total/100, '.2f')}")
