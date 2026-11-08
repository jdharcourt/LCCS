# James Harcourt
# Q5-7. Favorite Fruit: Make a list of your favourite fruits, and then write a series of independent if statements that check for certain fruits in your list.
#
# Make a list of your three favourite fruits and call it favourite_fruits.
# Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

fruits = ['Banana', 'Apple', 'Pineapple', 'Mango', 'Orange']

if 'Banana' in fruits:
    print('You must really like Bananas')

if "Apple" in fruits:
    print('You must really like Apples')

if "Grape" in fruits:
    print("You must really like grapes")

if 'Kiwi' in fruits:
    print("You must really like kiwis.")
else:
    print("You dont like kiwis :(")