import random
from collections import Counter
lista1 = [random.randint(0,50) for _ in range(20)]
lista2 = [random.randint(0,50) for _ in range(20)]
interseccao = sorted(list(set(lista1) & set(lista2)))
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)
print("lista1 - ",lista1)
print("lista2 - ",lista2)
print("Interseccao - ",interseccao)
print("Contagem")
for n in interseccao:
    print(f"{n}: (lista1={contagem_lista1[n]}, lista2={contagem_lista2[n]})")


