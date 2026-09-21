# James Harcourt
# Using the given list declaration of scores below, and producing a nice, neatly formatted output to the user

scores = [95, 83, 60, 85, 4, 97, 42, 98, 14, 86, 99, 97, 74, 90, 54, 90, 68, 94, 68, 84, 19, 83, 25, 99, 22, 89, 33, 92, 26, 99, 91, 84, 81, 99, 18, 85, 14, 97, 63, 82, 93, 98, 43, 95, 64, 86, 93, 100, 65, 80]

def sum():
    sums = 0
    for score in scores:
        sums += score
    return(sums)


def avg():
    l = len(scores)
    s = sum()
    average = s / l
    return(average)

def lowest():
    prev = scores[0]
    for score in scores:
        if score < prev:
            prev = score
        else:
            continue
    return(prev)

def highest():
    prev = scores[0]
    for score in scores:
        if score > prev:
            prev = score
        else:
            continue
    return(prev)

def mode():
    l = len(scores)
    scores.sort()
    m = (l // 2) - 1
    m = int(m)
    return(scores[m])

print(mode())






