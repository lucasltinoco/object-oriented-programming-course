import random

dictionary = {}

for i in range(0, 10):
    randomlist = []
    sum = 0
    for i in range(0, 30):
        n = random.random()
        randomlist.append(n)
        sum += n
    dictionary[frozenset(randomlist)] = sum

print(dictionary)
