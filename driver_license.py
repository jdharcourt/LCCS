import math


item = input("Enter the cost of the item: $")

if item.isdigit():
    item = float(item)
    if item >= 10000:
        print("Tender")
    elif item >= 500 and item < 10000:
        print("Please get qoutes from 3 suppliers")
    else:
        print("Continue purchase")
else:
    print("Please enter an amount")
    
    