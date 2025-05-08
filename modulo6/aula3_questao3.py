import random
lista = [19, 22, -10, 4, -2, -3, 5, 6, -17, -4, -1, 67, 98, -23, -6]
inicio_fatia_maior, tam_fatia_maior = 0,0
inicio_fatia_atual, tam_fatia_atual = 0,0
for i in range(len(lista)):
    if lista[i] < 0:
        tam_fatia_atual += 1
        if tam_fatia_atual == 1:
            inicio_fatia_atual = i
    else: 
        if  tam_fatia_atual > tam_fatia_maior:
                tam_fatia_maior = tam_fatia_atual
                inicio_fatia_maior = inicio_fatia_atual
        tam_fatia_atual = 0
print(lista)
del lista [inicio_fatia_maior:inicio_fatia_maior+tam_fatia_maior]
print(lista)