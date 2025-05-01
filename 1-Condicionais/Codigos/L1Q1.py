posicao = 0
nome_jogador = (input())

if nome_jogador == "Alisson" or nome_jogador == "Ederson" or nome_jogador == "Weverton":
    posicao = "goleiro"
    print(f'{nome_jogador} foi convocado e jogará como {posicao}!')
    
elif nome_jogador == "Daniel Alves" or nome_jogador == "Danilo" or nome_jogador == "Alex Sandro" or nome_jogador == "Alex Telles" :
    posicao = "lateral"
    print(f'{nome_jogador} foi convocado e jogará como {posicao}!')

elif nome_jogador == "Marquinhos" or nome_jogador == "Thiago Silva" or nome_jogador == "Éder Militão" or nome_jogador == "Bremer":
    posicao = "zagueiro"
    print(f'{nome_jogador} foi convocado e jogará como {posicao}!')

elif nome_jogador == "Casemiro" or nome_jogador == "Fabinho" or nome_jogador == "Fred":
    posicao = "meia"
    print(f'{nome_jogador} foi convocado e jogará como {posicao}!')

elif nome_jogador == "Bruno Guimarães" or nome_jogador == "Lucas Paquetá" or nome_jogador == "Everton Ribeiro":
    posicao = "meia"
    print(f'{nome_jogador} foi convocado e jogará como {posicao}!')

elif nome_jogador == "Neymar" or nome_jogador == "Raphinha" or nome_jogador == "Vini Jr.":
    posicao = "atacante"
    print(f'{nome_jogador} foi convocado e jogará como {posicao}!')

elif nome_jogador == "Antony" or nome_jogador == "Rodrygo" or nome_jogador == "Richarlison":
    posicao = "atacante"
    print(f'{nome_jogador} foi convocado e jogará como {posicao}!')

elif nome_jogador == "Pedro" or nome_jogador == "Gabriel Jesus" or nome_jogador == "Gabriel Martinelli":
    posicao = "atacante"
    print(f'{nome_jogador} foi convocado e jogará como {posicao}!')

else: 
    print(f'{nome_jogador} não foi convocado, mas quem sabe na próxima?')
