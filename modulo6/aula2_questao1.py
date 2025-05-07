import random
numeros = [random.randint(-100, 100) for _ in range(20)]
print("Lista ordenada, sem modificar a lista original:" ,(sorted(numeros)))
print("Lista original:" ,(numeros))
print("O maior indice é: ",(max(numeros)))
print("O menor indice é: ",(min(numeros)))