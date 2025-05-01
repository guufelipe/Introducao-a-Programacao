letra_sorteada = input()
qtd_amigos = int(input())
estado_de_preferencia = input()
estado_vencedor = ""

qtd_letras_vencedor = 0

for i in range(qtd_amigos):
    nome_amigo =  input()
    estado = input()
    qtd_letras = 0
    for letras in range(len(estado)):
        if estado[letras -1] == letra_sorteada:
            qtd_letras += 1
    if qtd_letras > qtd_letras_vencedor:
        qtd_letras_vencedor = qtd_letras
        estado_vencedor = estado        
            
if estado_vencedor == estado_de_preferencia:
    print(f'UHUL!!! Victor vai começar por {estado_vencedor} que é o estado que ele queria e ficara la por {qtd_letras_vencedor} dias.')
else:
    print(f'Eita!!! infelizmente, Victor terá que fazer uma viagem maior e começar pelo estado {estado_vencedor} e ficara la por {qtd_letras_vencedor} dias.')