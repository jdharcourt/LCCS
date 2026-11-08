# James Harcourt
# Q5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
#
# If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.

users = ["Brain", "Matthew", "Daithi", "James", "Brian", "Admin"]

name = input("Enter your name: ")

if name in users:
    if name == 'Admin':
        print('You are an admin')
    else:
        print(f'Hello, {name}')
else:
    print ("You are not a user")