import random
import os

# Define o caminho base
caminho_base = r"C:\Users\Com 3\Downloads\Aulas Desenvolve\Modulo 7"

# Define os caminhos dos arquivos
caminho_palavras = os.path.join(caminho_base, "gabarito_forca.txt")
caminho_enforcado = os.path.join(caminho_base, "gabarito_enforcado.txt")

# Lê o arquivo de palavras
with open(caminho_palavras, "r", encoding="utf-8") as f:
    palavras = [linha.strip() for linha in f if linha.strip()]

# Escolhe uma palavra aleatória
palavra_secreta = random.choice(palavras).lower()

# Lê o arquivo de estágios do enforcado
with open(caminho_enforcado, "r", encoding="utf-8") as f:
    linhas_enforcado = [linha.rstrip('\n') for linha in f.readlines()]
    estagios_enforcado = [
        '\n'.join(linhas_enforcado[i:i+5]) for i in range(0, len(linhas_enforcado), 6)
    ]

# Função para imprimir o enforcado
def imprime_enforcado(erros):
    print(estagios_enforcado[erros])

# Inicia o jogo
letras_descobertas = ["_" for _ in palavra_secreta]
letras_erradas = []
tentativas = 0
max_erros = 6

print("Bem-vindo ao jogo da forca!")
print("A palavra tem", len(palavra_secreta), "letras.")
print(" ".join(letras_descobertas))

# Loop principal
while tentativas < max_erros and "_" in letras_descobertas:
    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("Digite apenas uma letra válida.")
        continue

    if letra in letras_descobertas or letra in letras_erradas:
        print("Você já tentou essa letra.")
        continue

    if letra in palavra_secreta:
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                letras_descobertas[i] = letra
        print("Boa! Você acertou uma letra.")
    else:
        tentativas += 1
        letras_erradas.append(letra)
        print("Letra incorreta.")
        imprime_enforcado(tentativas)

    print(" ".join(letras_descobertas))
    print("Letras erradas:", ", ".join(letras_erradas))

# Resultado final
if "_" not in letras_descobertas:
    print("\nParabéns! Você acertou a palavra:", palavra_secreta)
else:
    print("\nVocê perdeu. A palavra era:", palavra_secreta)
    imprime_enforcado(tentativas)
