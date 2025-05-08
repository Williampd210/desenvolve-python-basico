lista = ["www.google.com", "www.gmail.com", "wwww.github.com", "www.reddit.com", "www.yahoo.com"]
print(lista)
dominios = [url[4:-4] for url in lista]
print(dominios)