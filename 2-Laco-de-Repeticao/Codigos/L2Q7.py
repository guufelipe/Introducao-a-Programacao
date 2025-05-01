rodadas = int(input())

saldo_A = 0
saldo_G = 0 
saldo_F = 0
saldo_M = 0

tentativas_corretas = 0
tentativas_erradas = 0

#rodadas
for i in range (rodadas):
    print(f'Rodada numero {i + 1}')
    nome_jogador = input()
    print(f'Jogador: {nome_jogador}')
    aposta_jogador = int(input())
    print(f'Valor apostado: {aposta_jogador}')
    qtd_acertos = int(input())
    print(f'Acreditando que acerta {qtd_acertos} vezes em 3 tentativas')
    qtd_apostadores = int(input())  
    print(f'{qtd_apostadores} amigos apostaram contra')
    if (qtd_apostadores == 3):
        print(f'Parece que {nome_jogador} está sendo subestimado!')

    valor_apostado_A = 0
    valor_apostado_G = 0
    valor_apostado_F = 0
    valor_apostado_M = 0

    situacao_artur = False
    situacao_guga = False
    situacao_frej = False
    situacao_misheldon = False

    #apostas:
    for apostas in range (qtd_apostadores):
        
        
        nome_apostador = input()
        if (nome_apostador == "Artur"):
          situacao_artur = True
        elif (nome_apostador == "Guga"):
          situacao_guga = True
        elif(nome_apostador == "Frej"):
          situacao_frej = True
        elif(nome_apostador == "Misheldon"):  
          situacao_misheldon = True
        valor_apostado = int(input())
        print(f'{nome_apostador} apostou {valor_apostado}')


        if nome_apostador == "Artur":
            valor_apostado_A = valor_apostado
        elif nome_apostador == "Guga":
            valor_apostado_G = valor_apostado
        elif nome_apostador == "Frej":
            valor_apostado_F = valor_apostado
        elif nome_apostador == "Misheldon":
            valor_apostado_M = valor_apostado
    

    tentativas_corretas = 0
    tentativas_erradas = 0
    
    for tentativas in range (3, 0, -1):    
        expressao = input()
        if(expressao != "Receba!"): 
            print(f"Errou! Restam {tentativas -1} tentativas")
            tentativas_erradas += 1
        else:
            tentativas_corretas += 1

    if (tentativas_corretas == qtd_acertos):
        if (nome_jogador == "Artur"):
          saldo_A += (valor_apostado_F + valor_apostado_G + valor_apostado_M)
          if (situacao_frej == True):
              saldo_F -= valor_apostado_F
          if (situacao_guga == True):  
              saldo_G -= valor_apostado_G
          if (situacao_misheldon == True):  
              saldo_M -= valor_apostado_M

        if (nome_jogador == "Guga"):
          saldo_G += (valor_apostado_F + valor_apostado_A + valor_apostado_M)
          if (situacao_frej == True):
              saldo_F -= valor_apostado_F
          if (situacao_artur == True):
              saldo_A -= valor_apostado_A
          if (situacao_misheldon == True): 
              saldo_M -= valor_apostado_M

        if (nome_jogador == "Frej"):
            saldo_F += (valor_apostado_M + valor_apostado_A + valor_apostado_G)
            if (situacao_artur == True):
                saldo_A -= valor_apostado_A
            if (situacao_guga == True):  
                saldo_G -= valor_apostado_G
            if (situacao_misheldon == True): 
                saldo_M -= valor_apostado_M
        if (nome_jogador == "Misheldon"):
            saldo_M += (valor_apostado_F + valor_apostado_G + valor_apostado_A)
            if (situacao_frej == True):
                saldo_F -= valor_apostado_F
            if (situacao_guga == True): 
                saldo_G -= valor_apostado_G
            if (situacao_artur == True):
                saldo_A -= valor_apostado_A
    
    else:
        #Quando o jogador perder a aposta
        if (nome_jogador == "Artur"):
            saldo_A -= (aposta_jogador * qtd_apostadores)
            if (situacao_guga == True):
                saldo_G += aposta_jogador
            if (situacao_frej == True):
                saldo_F += aposta_jogador
            if (situacao_misheldon == True):  
                saldo_M += aposta_jogador

        elif (nome_jogador == "Guga"):
          saldo_G -= (aposta_jogador * qtd_apostadores)
          if(situacao_frej == True):
            saldo_F += aposta_jogador
          if (situacao_misheldon == True):
            saldo_M += aposta_jogador
          if (situacao_artur == True):
            saldo_A += aposta_jogador

        elif (nome_jogador == "Frej"):
            saldo_F -= (aposta_jogador * qtd_apostadores)
            if (situacao_misheldon == True):
              saldo_M += aposta_jogador
            if (situacao_artur == True):
              saldo_A += aposta_jogador
            if (situacao_guga == True):
               saldo_G += aposta_jogador

        elif (nome_jogador == "Misheldon"):
            saldo_M -= (aposta_jogador * qtd_apostadores)
            if (situacao_guga == True):
                saldo_G += aposta_jogador
            if (situacao_artur):
                saldo_A += aposta_jogador
            if (situacao_frej == True):
                saldo_F += aposta_jogador

print("Fim de jogo, o resultado foi:")
print(f'Artur ficou com {saldo_A} de saldo')
print(f'Frej ficou com {saldo_F} de saldo')
print(f'Guga ficou com {saldo_G} de saldo')
print(f'Misheldon ficou com {saldo_M} de saldo')