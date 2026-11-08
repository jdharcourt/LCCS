import random
import time as t

start = t.time()
num = random.randint(1, 10000001)
found = False
it = 0 
i = 0


numbers = list(range(1, 10000001))
random.shuffle(numbers)
og = numbers[:]


numbers.sort()

while found == False:
    middle = (len(numbers)) // 2
    middle = int(middle)
    if numbers[middle] == num:
        found = True
    elif numbers[middle] > num:
        numbers = numbers[:middle]

    else:
        numbers = numbers[middle + 1:]

    it += 1


print(it)
print(f"found {num} in:")
end = t.time()
print(end-start)
print()


while True:
    for item in og:
        i = item
        if i == num:
            print(f"At position {i}")
            break
