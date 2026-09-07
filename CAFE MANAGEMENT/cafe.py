menu = {
    'pizza' : 50, 'salad': 30, 'burger': 100, 'pop corn': 150, 'chicken puff': 100
}



print("Well Come o our Dev Cafe")
print('pizza : 50\nsalad: 30\nburger: 100\npop corn: 150\nchicken puff: 100')

order_items = input("Enter your items: ")


order_total = 0

if order_items in menu:
    order_total += menu[order_items]
    order = input("Do you want to add anything else(Yes/No):")
    if order == 'Yes':
        order_item2 = input("Enter your second item:")
        if order_item2 in menu:
            order_total += menu[order_item2]
            print(f'your order value {order_total}')

    else:
        print(f"Your order value {order_total}")


else:
    print("You entered a wrong item")


