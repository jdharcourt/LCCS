import time
l = []
sum = 0

def p():
    start = time.perf_counter()
    print("Hello World")
    end = time.perf_counter()
    diff = start - end
    l.append(diff)

for i in range(1000000):
    p()


for i in l:
    sum += i
    mean = sum / len(l)

print(mean)


