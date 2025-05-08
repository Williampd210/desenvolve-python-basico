import random
numeros = [random.randint(-100, 100) for _ in range(20)]
print("Lista ordenada, sem modificar a lista original:",(sorted(numeros)))
print("Lista original:",(numeros))
print("O maior valor é:",(max(numeros)))
print("E está no indice:",numeros.index(max(numeros)))
print("O menor valor é:",(min(numeros)))
print("E está no indice:",numeros.index(min(numeros)))
