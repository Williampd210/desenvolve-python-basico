frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")
palavra_ordenada = sorted(objetivo.lower())
anagramas = []
for palavra in frase.split():
    if sorted(palavra.lower()) == palavra_ordenada:
        anagramas.append(palavra)
print("Anagramas:", anagramas)
