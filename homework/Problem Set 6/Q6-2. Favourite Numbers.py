# James Harcourt
# Q6-2. Favourite Numbers: Use a dictionary to store people’s favourite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favourite number for each person, and store each as a value in your dictionary. Print each person’s name and their favourite number.
#
# Use a for loop to cycle over the dictionary, this gives us the keys. Then use the .get() method inside the loop to access the value, i.e., their favourite number.

names = {'matthew':5,'mark':23,'luke':32,'john':1,'paul':12}

for name in names:
    print(f"Name: {name.title()} -- Number: {names.get(name)}")