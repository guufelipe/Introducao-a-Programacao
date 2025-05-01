historico = []
batalhas_vencidas = 0
batalhas_empatadas = 0
batalhas_perdidas = 0

def classificar_motosserra(a, b, c):

    # /////  MOTOSSERRA SUPREMA /////
    if (a >= 750) and (b >= 7) and (c >= 8):
        return "Motosserra Suprema"
    # /////  MOTOSSERRA AVANÇADA /////
    elif (a >= 500) and (b >= 6) and (c >= 6):
        return "Motosserra Avançada"
    # /////  MOTOSSERRA NORMAL /////
    else:
        return "Motosserra Normal"

def calcular_forca():
    return (energia_denji + (controle_denji * precisão_denji))

for i in range (3) :
    if i == 0:
        vilao = "Makima"
    elif i == 1:
        vilao = "Reze"
    elif i == 2:
        vilao = "Santa Claus"
    
    energia_denji = int(input())
    controle_denji = int(input())
    precisão_denji = int(input())
    força_inimigo = int(input())

    print(f"### Rodada {i + 1} - {vilao} ###")
    print(f"O Denji ira se transformar na {classificar_motosserra(energia_denji, controle_denji, precisão_denji)} para enfrentar o {vilao}")

    #Calculando resultado da batalha
        #denji vence:
    if calcular_forca() > força_inimigo :
        print(f"Denji saiu vitorioso nessa batalha contra o {vilao}")
        historico.append(f"Rodada {i+1}: {classificar_motosserra(energia_denji, controle_denji, precisão_denji)} - Vitoria")
        batalhas_vencidas += 1

        #denji perde:
    elif calcular_forca() < força_inimigo :
        print(f"Denji não conseguiu força o suficiente para derrotar o {vilao}")
        historico.append(f"Rodada {i+1}: {classificar_motosserra(energia_denji, controle_denji, precisão_denji)} - Derrota")
        batalhas_perdidas += 1

        #denji perde:
    elif calcular_forca() == força_inimigo :
        print(f"Como pode ser possível?? Denji possui a mesma força que o {vilao}")
        historico.append(f"Rodada {i+1}: {classificar_motosserra(energia_denji, controle_denji, precisão_denji)} - Empate")
        batalhas_empatadas += 1

print("### Resultado Final ###")
print(*historico, sep= "\n")

if batalhas_vencidas == 3:
    print("Nenhum dos 3 inimigos foram capazes de derrotar o Denji!")

elif batalhas_perdidas == 3:
    print("Hoje não foi um dia bom para o Denji, perdeu todas as batalhas")

elif (batalhas_vencidas == 1) and (batalhas_perdidas == 1) and (batalhas_empatadas == 1):
    print("Hoje foi um dia equilibrado para o Denji, conseguiu ganhar, perder e empatar")

elif (batalhas_vencidas > batalhas_perdidas) and (batalhas_vencidas > batalhas_empatadas):
    print("Denji conseguiu derrotar a maioria de seus inimigos")

elif (batalhas_perdidas > batalhas_vencidas) and (batalhas_perdidas > batalhas_empatadas):
    print("Dia péssimo para o Denji, perdeu a maioria de suas batalhas")

elif(batalhas_empatadas > batalhas_vencidas) and (batalhas_empatadas > batalhas_perdidas):
    print("Dia duro para o Denji, empatou de mais")