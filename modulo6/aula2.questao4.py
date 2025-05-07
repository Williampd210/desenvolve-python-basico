tamanholista1 = input("Digite a quantidade de elementos da lista 1: ")
valor1 = int(tamanholista1)
lista1 = []
lista2 = []
print(f"Digite os {tamanholista1} elementos da lista 1: ")
for i in range(valor1):
    elemento = input()
    lista1.append(elemento)
tamanholista2 = input("Digite a quantidade de elementos da lista 2: ")
valor2 = int(tamanholista2)
print(f"Digite os {tamanholista2} elementos da lista 2: ")
for i in range(valor2):
    elemento1 = input()
    lista2.append(elemento1)
lista_concat = lista1 + lista2
print(f"Lista intercalada:", ' '.join(lista_concat))