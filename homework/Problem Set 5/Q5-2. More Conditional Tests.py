# James Harcourt
# Q5-2. More Conditional Tests:  Try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
#
# Tests for equality and inequality with strings (comparison on strings is case sensitive)
# Tests using the string lower() method (lower() is often used on user input to be compared with a stored value which is in lower case)
# Numerical tests involving equality == and inequality !=, greater than > and less than <, greater than or equal to >=, and less than or equal to <=
# Tests using the and keyword and the or keyword
# Test whether an item is in a list  (use in keyword ) 
# Test whether an item is not in a list (use not in keywords)

equality = "Equal"
inequal = "Inequal"

number1 = 5
number2 = 55

items = ["Car", "Van", "Truck", "Bus"]
find = "Van"

print(f"Is equality == inequal? {equality == inequal}")
print(f"Is equality != inequal? {equality != inequal}")

print(f"Is equality.lower() == inequal.lower()? {equality.lower() == inequal.lower()}")
print(f"Is equality.lower() != inequal.lower()? {equality.lower() != inequal.lower()}")

print(f"Numbers equal? {number1 == number2}")
print(f"Numbers not equal? {number1 != number2}")

print(f"Is equality != inequal and numbers !=? {equality != inequal and number1 != number2}")

for item in items:
    if item.lower() == find.lower():
        print(f"Found {item} in list")

