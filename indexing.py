names = ["James", "Daithi", "Poopy", "Big H", "Conor"]

index = input("Enter a number 0-4: ")

try: 
    index = int(index)
except ValueError:
    print("Not a number")

try:
    print(names[index])
except IndexError:
    print("Index out of range")