# define the menu of restaurant
menu={
    "Pizza":70,
    "Pasta":50,
    "Burger":60,
    "Salad":40,
    "Coffee":80
}

# greet
print("Welcome to our SIZZL Restaurant")
print("Pizza: Rs70\nPasta: Rs50\nBurger: Rs60\nSalad: Rs40\nCoffee: Rs80")

#pace the order
order_total=0

item_1=input("What would you like to order=")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Your item{item_1} is not available in the menu options")

another_order=input("Do you want to add any other item? (Yes/No)")
if another_order == "Yes":
    item_2=input("What would you like to order=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"The item{item_2} has been added to the menu")
    else:
        print(f"Ordered item{item_2} is not available")

print(f"The total amount of items is {order_total}")

    