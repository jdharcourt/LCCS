# James Harcourt
# Q5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
#
# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct message is printed.

users = ["Brain", "Matthew", "Daithi", "James", "Brian", "Admin"]

name = input("Enter your name: ")

if len(users) != 0:
    if name in users:
        if name == 'Admin':
            print('You are an admin')
        else:
            print(f'Hello, {name}')
    else:
        print ("You are not a user")
else:
    print("We need some users")