import string
def limpar_texto(texto):
    texto = texto.lower()
    return ''.join(c for c in texto if c.isalnum())
while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.strip().lower() == 'fim':
        break
    frase_limpa = limpar_texto(frase)
    if frase_limpa == frase_limpa[::-1]:
        print(f'"{frase}" é palíndromo\n')
    else:
        print(f'"{frase}" não é palíndromo\n')
