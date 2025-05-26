caminho_csv = 'spotify-2023.csv'
mais_tocadas_por_ano = {}

with open(caminho_csv, 'r', encoding='latin-1') as f:
    header = f.readline()
    for linha in f:
        if '"' in linha:
            continue
        colunas = linha.strip().split(',')
        if len(colunas) < 10:
            continue
        try:
            track_name = colunas[0]
            artist_name = colunas[1]
            artist_count = int(colunas[2])
            released_year = int(colunas[3])
            streams = int(colunas[8])
            if 2012 <= released_year <= 2022:
                atual = mais_tocadas_por_ano.get(released_year)

                if not atual or streams > atual[3]:
                    mais_tocadas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

        except (ValueError, IndexError):
            continue 
resultado = [mais_tocadas_por_ano[ano] for ano in sorted(mais_tocadas_por_ano)]
print(resultado)
