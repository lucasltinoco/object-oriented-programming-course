lista1 = [1,5,2]
# Aponta para mesma área de memória
lista2 = lista1
# Soluções para cópia:
# lista2 = lista1[:]
# lista2 = list(lista1)
# lista2 = lista1.copy()
# lista2 = copy.deepcopy(lista1)
lista2[0] = 3

print(lista1)
print(lista2)

print(id(lista1))
print(id(lista2))

# shallow copy -> copia no primeiro nível
# deep copy -> copia todos os níveis de referência

A = [1, [3, 5, 7], "abc"]
B = A.copy()
B[0] = 3
C=B[1]
C[1]=66
print(A)
print(B)
print(C)