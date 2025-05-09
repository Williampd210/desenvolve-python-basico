frase = input("Digite uma frase:")
vogais = 'a,e,i,o,u'
consoantes = 'bcdfghjklmnpqrstvwxyz'
lista_vogais = sorted([x for x in frase if x in vogais])
lista_consoantes = ([x for x in frase if x in consoantes])
print("Vogais: ",lista_vogais)
print("Consoantes",lista_consoantes)
