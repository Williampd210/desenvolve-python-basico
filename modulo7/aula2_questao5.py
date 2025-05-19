import random
def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []
    for palavra in palavras:
        if len(palavra) > 3:
            primeira = palavra[0]
            ultima = palavra[-1]
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = primeira + ''.join(meio) + ultima
            nova_frase.append(palavra_embaralhada)
        else:
            nova_frase.append(palavra)
    return ' '.join(nova_frase)
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
