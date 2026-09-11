name = input("Enter your name: ")

print(f"Hello, {name}!")


it = 0

caps = ""

for letter in name:
    it += 1
    if it % 2 == 0:
        caps += letter.upper()
    else:
        caps += letter.lower()

print(caps)

