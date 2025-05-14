numero = input("Digite o número: ")
if len(numero) == 8:
    numero = '9' + numero
elif len(numero) != 9:
    print("Número inválido")
print("Numero completo:", numero[:5] + '-' + numero[5:])