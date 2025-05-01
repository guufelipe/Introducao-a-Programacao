#TIME 1
pontos_time_1 = 0
nome_time_1 = input()
resultado_jogo_1_time_1 = input()
resultado_jogo_2_time_1 = input()
#Pontos time 1
if resultado_jogo_1_time_1 == "Ganhou":
    pontos_time_1 += 3
elif resultado_jogo_1_time_1 == "Empatou":
    pontos_time_1 += 1

if resultado_jogo_2_time_1 == "Ganhou":
    pontos_time_1 += 3
elif resultado_jogo_2_time_1 == "Empatou":
    pontos_time_1 += 1

#TIME 2
pontos_time_2 = 0
nome_time_2 = input()
resultado_jogo_1_time_2 = input()
resultado_jogo_2_time_2 = input()
#Pontos time 2
if resultado_jogo_1_time_2 == "Ganhou":
    pontos_time_2 += 3
elif resultado_jogo_1_time_2 == "Empatou":
    pontos_time_2 += 1

if resultado_jogo_2_time_2 == "Ganhou":
    pontos_time_2 += 3
elif resultado_jogo_2_time_2 == "Empatou":
    pontos_time_2 += 1

#TIME 3
pontos_time_3 = 0
nome_time_3 = input()
resultado_jogo_1_time_3 = input()
resultado_jogo_2_time_3 = input()
#Pontos time 2
if resultado_jogo_1_time_3 == "Ganhou":
    pontos_time_3 += 3
elif resultado_jogo_1_time_3 == "Empatou":
    pontos_time_3 += 1

if resultado_jogo_2_time_3 == "Ganhou":
    pontos_time_3 += 3
elif resultado_jogo_2_time_3 == "Empatou":
    pontos_time_3 += 1

#classificados / eliminados

if pontos_time_1 < pontos_time_2 and pontos_time_1 < pontos_time_3:
    print(f'Parabéns aos países {nome_time_2} e {nome_time_3}, vocês estão classificados para as oitavas de finais!!!')

if pontos_time_2 < pontos_time_1 and pontos_time_2 < pontos_time_3:
    print(f'Parabéns aos países {nome_time_1} e {nome_time_3}, vocês estão classificados para as oitavas de finais!!!')

if pontos_time_3 < pontos_time_1 and pontos_time_3 < pontos_time_2:
    print(f'Parabéns aos países {nome_time_1} e {nome_time_2}, vocês estão classificados para as oitavas de finais!!!')