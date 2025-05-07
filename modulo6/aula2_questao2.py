import random
num_elementos = random.randint(5,20)
elementos = [random.randint(5,20) for _ in  range (num_elementos)]
print("Lista de elementos: ", (elementos))
print("A soma dos valores é: ",(sum(elementos)))
print("A media dos valores é: ",(sum(elementos)/len(elementos)))