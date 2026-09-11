# James Harcourt
# Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename = input("Enter Filename: ")
bare_file = filename.removesuffix('.txt') # Remove .txt extension from filename

print("Stripped filename: ", bare_file)