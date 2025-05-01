entrada = ""
suspeitos = []
seq_suspeitos = ""


while (entrada != "ja temos nossa lista de suspeitos"):
    entrada = input()
    if (entrada == "novo suspeito - altissima periculosidade"):
        nome_suspeito = input()
        suspeitos.insert(0, nome_suspeito)
    
    elif(entrada == "novo suspeito - pouco perigoso"):
        nome_suspeito = input()
        suspeitos.append(nome_suspeito)
    
    elif(entrada == "livre de suspeita, pode remover"):
        nome_suspeito = input()
        suspeitos.remove(nome_suspeito)
    
    elif(entrada == "sujeito mais perigoso do que pensavamos"):
        posicao_atual = int(input())
        posicao_novo = int(input())
        ## Selecionando os suspeitos
        novo = suspeitos[posicao_novo]
        anterior = suspeitos[posicao_atual]
        ## Alterando eles de posição
        suspeitos[posicao_novo] = anterior
        suspeitos[posicao_atual] = novo

    elif(entrada == "que estranho, esses dois meliantes… troque-os de lugar"):
        suspeito_1 = input()
        suspeito_2 = input()

        #RECEBENDO O INDICE DOS SUPEITOS
        ind_susp1 = suspeitos.index(suspeito_1)
        ind_susp2 = suspeitos.index(suspeito_2)

        #DELETANDO O PRIMEIRO SUSPEITO
        suspeito1 = suspeitos.pop(ind_susp1)
        #SUBSTITUINDO LUGAR DELE
        suspeitos.insert(ind_susp2, suspeito1)

        #TENHO QUE PEGAR A NOVA POSIÇÂO DO SUSPEITO_2, E ALTERAR pra primeira posição
        novo_ind_susp2 = suspeitos.index(suspeito_2)
        #DELETANDO O SUSPEITO 2
        suspeito2 = suspeitos.pop(novo_ind_susp2)
        #COLOCANDO NA NOVA POSIÇÃO DELE
        suspeitos.insert(ind_susp1, suspeito2)

    elif(entrada == "essa posicao nao esta de acordo, ele nao e tao perigoso assim"):
        nome_suspeito = input()
        suspeitos.remove(nome_suspeito)
        suspeitos.append(nome_suspeito)
    
    elif(entrada == "como a lista esta ficando?"):
        seq_suspeitos = " "
        seq_suspeitos = seq_suspeitos.join(suspeitos)

        print(seq_suspeitos)

else:
    print("O resultado final ficou assim:")
    seq_suspeitos = " "
    seq_suspeitos = seq_suspeitos.join(suspeitos)
    
    print(seq_suspeitos)