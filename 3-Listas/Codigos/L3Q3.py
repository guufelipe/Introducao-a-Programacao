n_entradas = int(input())
conteudos_1 = []
conteudos_2 = []
conteudos_3 = []




for a in range(n_entradas):
    entrada = input()
    conteudo, n_diario = entrada.split(", ")
    if   n_diario == "1":
        conteudos_1.append(conteudo)
    elif n_diario == "2":
        conteudos_2.append(conteudo)
    elif n_diario == "3":
        conteudos_3.append(conteudo)

n_buscas = int(input())

for b in range(n_buscas):
    conteudo_buscado = input()
    conteudo_achado = False
    diario_encontrado = 0
    for c in (conteudos_1):
        if conteudo_buscado == c:
            conteudo_achado = True
            diario_encontrado = 1
        
    if conteudo_achado == False:
        for d in (conteudos_2):
            if conteudo_buscado == d:
                conteudo_achado = True
                diario_encontrado = 2
                
    if conteudo_achado == False:
        for e in (conteudos_3):
            if conteudo_buscado == e:
                conteudo_achado = True
                diario_encontrado = 3

    if conteudo_achado:
        print(f"Informacoes sobre {conteudo_buscado} estao no Diario {diario_encontrado}")
    
    elif not conteudo_achado:
        print(f"Nenhum dos diarios possui informacoes sobre {conteudo_buscado}")
