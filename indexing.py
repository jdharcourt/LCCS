

names = ["James", "Daithi", "Poopy", "Big H", "Conor"]

index = input("Enter a number or a new name to add it to the list: ")

for name in names:
    if name.upper():
        temp = name
        del name
        names.append(temp.lower())
print(names)

try: 
    index = int(index)
    integer = True
    string = False
except ValueError:
    index = str(index)
    string = True
    integer = False

if integer:
    try:
        print(names[index])
    except IndexError:
        print("Index out of range")

elif string:
    if index in names:
        print('Name already exists')
    else:
        names.append(index.lower())
        print("New list: ", names)
