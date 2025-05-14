frase = input("Digite uma frase: ")
vogal = 'aeiouAEIOU'
quantidade_vogal = 0
indice = []
for i, letra in enumerate(frase):
    if letra in vogal:
        quantidade_vogal += 1 
        indice.append(i)
print(quantidade_vogal,"vogais")
print("Índices:", indice)