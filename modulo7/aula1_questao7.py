import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []
    for nome in nomes:
        criptografado = ''
        for c in nome:
            codigo = ord(c)
            novo_codigo = codigo + chave
            if novo_codigo > 126:
                novo_codigo = 33 + (novo_codigo - 127)
            criptografado += chr(novo_codigo)
        nomes_criptografados.append(criptografado)
    return nomes_criptografados, chave
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
print("nomes =",(nomes))
nomes_cript, chave = encrypt(nomes)
print("Chave_aleatoria =", chave)
print("nomes_cript =", nomes_cript)
