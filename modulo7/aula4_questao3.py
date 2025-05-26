import re
def contar_personagem(texto, nome):
    padrao = r'\b' + re.escape(nome) + r'\b'
    return len(re.findall(padrao, texto, flags=re.IGNORECASE))
caminho_arquivo = r"C:\Users\Com 3\Downloads\Aulas Desenvolve\Modulo 7\estomago.txt"
linhas = []
maior_linha = ''
maior_tamanho = 0
contagem_nonato = 0
contagem_iria = 0
with open(caminho_arquivo, 'r', encoding='latin-1') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        if len(linha) > maior_tamanho:
            maior_tamanho = len(linha)
            maior_linha = linha.strip()

        contagem_nonato += contar_personagem(linha, 'Nonato')
        contagem_iria += contar_personagem(linha, 'Íria')
print("Primeiras 25 linhas do roteiro:")
for i, linha in enumerate(linhas[:25]):
    print(f"{i + 1}: {linha.strip()}")
print(f"\nNúmero total de linhas: {len(linhas)}")
print(f"Linha com maior número de caracteres: {maior_linha}")
print(f"Menções ao personagem 'Nonato': {contagem_nonato}")
print(f"Menções ao personagem 'Íria': {contagem_iria}")
