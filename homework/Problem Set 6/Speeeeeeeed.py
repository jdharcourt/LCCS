import time



def count(number):
    
    n = 0
    while n < number:
        n += 1
    
    return n


number = int(input('Enter a number to count: '))

start = time.time()
final = count(number)
end = time.time()

print()
print(f"Counted to {final} in {end-start}")