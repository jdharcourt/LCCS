# James Harcourt
# Make a list of the numbers from one to one million, and then use a for loop to print the numbers

# James Harcourt
# Make a list of the numbers from one to one million, and then use a for loop to print the numbers
import time

l = []
sum = 0

def timer():
    start = time.perf_counter()
    for i in range(0, 10 ** 3, 10):
        print(i)
    end = time.perf_counter()
    return end-start

for i in range(10):
    t = timer()
    l.append(t)


for i in l:
    sum += i

average = sum / len(l)


print("Mean: ", average)

    
    


