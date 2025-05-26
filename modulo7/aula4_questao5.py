caminho_arquivo = "meus_livros.csv"
livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["A Revolução dos Bichos", "George Orwell", 1945, 112],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["O Sol é Para Todos", "Harper Lee", 1960, 336],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 480],
    ["Ensaio Sobre a Cegueira", "José Saramago", 1995, 320],
    ["O Hobbit", "J.R.R. Tolkien", 1937, 310],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417]
]
with open(caminho_arquivo, "w", encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
        f.write(linha)
print(f"Arquivo '{caminho_arquivo}' criado com sucesso!")
