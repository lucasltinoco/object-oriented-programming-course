# A = (1, 2, 3)
# A[0] = 5
# TypeError: 'tuple' object does not support item assignment

B=(1, [2,3,4], 5)
B[1].append(5)
print(B)
# Mutabilidade