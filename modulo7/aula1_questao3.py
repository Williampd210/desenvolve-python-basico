frase = input("Digite a frase: ")
branco = 0
for i in frase:
    if i == " ":
        branco += 1
print("Espaços em branco: ", (branco)) 