#By Griffin Corniea 9/8/2025
#Grocry store purchase calculator

def calculate_total_purchase():
    subtotal = 0
    prices = {
        "apple": 1.00,
        "banana": 0.50,
        "bread": 2.00,
        "milk": 3.00,
        "eggs": 2.50
    }


    # Ask for items
    item1 = input("First Item: ").lower()
    item2 = input("Second Item: ").lower()
    item3 = input("Third Item: ").lower()
    item4 = input("Fourth Item: ").lower()
    item5 = input("Fifth Item: ").lower()

    items = [item1, item2, item3, item4, item5]

    # Calculate subtotal

    for item in items:
        if item in prices:
            subtotal += prices[item]
        else:
            print(" ERROR: A item was not found in price list.")

    # Tax stuff
    tax = subtotal * 0.07
    total = subtotal + tax

    # print
    print(total)


calculate_total_purchase()