import re
arquivo_entrada = "frase.txt"
arquivo_saida = "palavras.txt"
with open(arquivo_entrada, "r", encoding="utf-8") as f:
    conteudo = f.read()
palavras = re.findall(r'\b[a-zA-ZÀ-ÿ]+\b', conteudo)
with open(arquivo_saida, "w", encoding="utf-8") as f:
    for palavra in palavras:
        f.write(palavra + "\n")
with open(arquivo_saida, "r", encoding="utf-8") as f:
    print(f.read())
