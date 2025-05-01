dfr_gols = 0
fim_jogo = False

##Jogo 1(OITAVAS DE FINAL)
favoritismoBr = int(input())
nomeOponente1 = input()
favoritismoOponente1 = int(input())
golsBR1 = int(input())
golsOPO1 = int(input())
dfr_gols = golsBR1 - golsOPO1

if golsBR1 < golsOPO1:
    if golsBR1 < golsOPO1:
        fim_jogo = True
    print(f'Infelizmente essa seleção dx {nomeOponente1} era muito forte para o Brasil.')
    
if not fim_jogo and (golsBR1 > golsOPO1):
    if dfr_gols == 1:
        favoritismoBr += 10
    elif dfr_gols == 2:
        favoritismoBr += 20
    elif dfr_gols >= 3:
        favoritismoBr += 30
    print("Quem é que segura o Brasil???")

if not fim_jogo and (golsBR1 == golsOPO1):
    if (favoritismoBr < favoritismoOponente1):
            fim_jogo = True
            print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
    else:
        print("No sufoco, o Brasil conseguiu ganhar!!!")
        
##Jogo 2(QUARTAS DE FINAL)
if not fim_jogo:
    nomeOponente2 = input()
    favoritismoOponente2 = int(input())
    golsBR2 = int(input())
    golsOPO2 = int(input()) 
    dfr_gols = golsBR2 - golsOPO2

    if not fim_jogo and (golsBR2 < golsOPO2):
        if golsBR2 < golsOPO2:
            fim_jogo = True
        print(f'Infelizmente essa seleção dx {nomeOponente2} era muito forte para o Brasil.')
        
    if not fim_jogo and (golsBR2 > golsOPO2):
        if dfr_gols == 1:
            favoritismoBr += 10
        elif dfr_gols == 2:
            favoritismoBr += 20
        elif dfr_gols >= 3:
            favoritismoBr += 30
        print("Quem é que segura o Brasil???")
        
    if not fim_jogo and (golsBR2 == golsOPO2):
        if (favoritismoBr < favoritismoOponente2):
                fim_jogo = True
                print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
        else:
            print("No sufoco, o Brasil conseguiu ganhar!!!")

##Jogo 3(SEMI-FINAL)

if not fim_jogo:
    nomeOponente3 = input()
    favoritismoOponente3 = int(input())
    golsBR3 = int(input())
    golsOPO3 = int(input())
    dfr_gols = golsBR3 - golsOPO3

    if not fim_jogo and (golsBR3 < golsOPO3):
        if golsBR3 < golsOPO3:
            fim_jogo = True
        print(f'Infelizmente essa seleção dx {nomeOponente3} era muito forte para o Brasil.')
        
    if not fim_jogo and (golsBR3 > golsOPO3):
        if dfr_gols == 1:
            favoritismoBr += 10
        elif dfr_gols == 2:
            favoritismoBr += 20
        elif dfr_gols >= 3:
            favoritismoBr += 30
        print("Quem é que segura o Brasil???")
        
    if not fim_jogo and (golsBR3 == golsOPO3):
        if (favoritismoBr < favoritismoOponente3):
                fim_jogo = True
                print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
        else:
            print("No sufoco, o Brasil conseguiu ganhar!!!")

##Jogo 4( FINAL) 
if not fim_jogo:
    nomeOponente4 = input() 
    favoritismoOponente4 = int(input())
    if favoritismoBr > favoritismoOponente4:
        print("O BRASIL VAI SER HEXAAAAAAAA")
    elif favoritismoBr == favoritismoOponente4:
        print("O BRASIL VAI SER HEXAAAAAAAA")
    else:
        print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {nomeOponente4} na simulação')