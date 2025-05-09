## Primeiro ponto
pares = [i for i in range(20,51) if i % 2 ==0]
print(pares)
## Segundo ponto
lista = [1,2,3,4,5,6,7,8,9]
quadrado = []
print("Lista original:",lista)
for i in range(len(lista)):
    elemento = lista[i] * lista[i]
    quadrado.append(elemento)
print("Quadrado da lista:",quadrado)
## Terceiro ponto
lista = [i for i in range(1,100) if i % 7 == 0]
print(lista)
## Quarto ponto
lista = []
for i in range(0,30,3):
    if i % 2 == 0:
        print((i),"- par")
    else:
        print((i),"- impar")
    