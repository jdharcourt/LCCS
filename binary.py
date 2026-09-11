integer = False
ran = 0
final = []

number = input("Enter a number: ")

if number.isdigit():
    integer = True
else:
    integer = False

if not integer:
    print("The number is not an integer.")

try:
    digits = [int(digit) for digit in str(number)]
except ValueError:
    print("Error: Please enter a valid integer.")
    digits = []
    exit()

print(digits)

print(len(digits))

length = len(digits)


for digit in enumerate(reversed(digits)):
    binary = digit * (2 ** ran)
    ran += 1
    final.append(binary)


print(final)