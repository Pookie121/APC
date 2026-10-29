cart = ["Pen", "Book"]

cart.append("Pencil")
cart.remove("Pen")

item = input("Search item: ")

if item in cart:
    print("Found")

print(cart)
print("Total Items =", len(cart))
