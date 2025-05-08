lista = []
tamanho = int(input("Escolha o tamanho da lista, sendo maior que 4:"))
for i in range(tamanho):
    elemento = input()
    lista.append(elemento)
print("Lista original:",' '.join(lista))
print("3 primeiros elementos:",' '.join(lista[0:3]))
print("2 últimos elementos:",' '.join(lista[-2:]))
print("Lista invertida:",' '.join(lista[::-1]))
print("Elementos de índice par:",' '.join(lista[0::2]))
print("Elementos de índice ímpar:",' '.join(lista[1::2]))