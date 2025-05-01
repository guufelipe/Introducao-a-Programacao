#jogador_1
n_1 = input()
bola_1 = int(input())
f_1 = int(input())
gols_1 = int(input())
aprvmt_1 = ((gols_1/f_1) * 100)

#jogador_2
n_2 = input()
bola_2 = int(input())
f_2 = int(input())
gols_2 = int(input())
aprvmt_2 = ((gols_2/f_2) * 100)

#jogador_3
n_3 = input()
bola_3 = int(input())
f_3 = int(input())
gols_3 = int(input())
aprvmt_3 = ((gols_3/f_3) * 100)

lugar1 = "a" 
lugar2 = "a"
lugar3 = "a"

#CASO NAO HAJA EMPATE e JOGADOR 1 GANHAR
if bola_1 > bola_2 and bola_1 > bola_3:
    lugar1 = n_1
    if bola_2 > bola_3:
        lugar2 = n_2
        lugar3 = n_3
    elif bola_3 > bola_2:
        lugar2 = n_3
        lugar3 = n_2
#SE TIVER TIVER EMPATE e JOGADOR1 ganhar  
    else:
        if aprvmt_2 > aprvmt_3:
            lugar2 = n_2
            lugar3 = n_3
        elif aprvmt_3 > aprvmt_2:
            lugar2 = n_3
            lugar3 = n_2
    print (f'{lugar1}\n{lugar2}\n{lugar3}')
    print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    if bola_1 <=10:
        print(f'{lugar1}?! Sei não hein Galvão…')
    else:
        print(f'{lugar1}! Dessa vez o hexa vem pra casa!!')
        
#CASO NAO HAJA EMPATE e JOGADOR 2 GANHAR
elif bola_2 > bola_1 and bola_2 > bola_3:
    lugar1 = n_2
 
    if bola_1 > bola_3:
        lugar2 = n_1
        lugar3 = n_3
    elif bola_3 > bola_1:
        lugar2 = n_3
        lugar3 = n_1
#SE TIVER TIVER EMPATE e JOGADOR1 ganhar
    else:
        if aprvmt_1 > aprvmt_3:
            lugar2 = n_1
            lugar3 = n_3
        elif aprvmt_3 > aprvmt_1:
            lugar2 = n_3
            lugar3 = n_1
    print (f'{lugar1}\n{lugar2}\n{lugar3}')
    print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    if bola_2 <=10:
        print(f'{lugar1}?! Sei não hein Galvão…')
    else:
        print(f'{lugar1}! Dessa vez o hexa vem pra casa!!')

#CASO NAO HAJA EMPATE e JOGADOR 2 GANHAR
elif bola_3 > bola_1 and bola_3 > bola_2:
    lugar1 = n_3
 
    if bola_1 > bola_2:
        lugar2 = n_1
        lugar3 = n_2
    elif bola_2 > bola_1:
        lugar2 = n_2
        lugar3 = n_1
#SE TIVER TIVER EMPATE e JOGADOR1 ganhar
    else:
        if aprvmt_1 > aprvmt_2:
            lugar2 = n_1
            lugar3 = n_2
        elif aprvmt_2 > aprvmt_1:
            lugar2 = n_2
            lugar3 = n_1
    print (f'{lugar1}\n{lugar2}\n{lugar3}')
    print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    if bola_3 <=10:
        print(f'{lugar1}?! Sei não hein Galvão…')
    else:
        print(f'{lugar1}! Dessa vez o hexa vem pra casa!!')

#3º definido 
## Jogador1 == 3º lugar
elif bola_1 < bola_2 and bola_1 < bola_3:
    lugar3 = n_1
    if bola_2 == bola_3:
        if aprvmt_2 > aprvmt_3:
            lugar1 = n_2
            lugar2 = n_3
            nome_campeao = n_2
            bola_campeao = bola_2
        else:
            lugar1 = n_3
            lugar2 = n_2
            nome_campeao = n_3
            bola_campeao = bola_3
    print("Tite está mais indeciso do que nunca!")
    print(f'{lugar1}\n{lugar2}\n{lugar3}')
    print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")
    if bola_campeao <= 10:
        print(f'{nome_campeao}?! Sei não hein Galvão…')
    else:
        print(f'{nome_campeao}! Dessa vez o hexa vem pra casa!!')

##  Jogador 2 == 3º lugar
elif bola_2 < bola_1 and bola_2 < bola_3:
    lugar3 = n_2
    if bola_1 == bola_3:
        if aprvmt_1 > aprvmt_3:
            lugar1 = n_1
            lugar2 = n_3
            nome_campeao = n_1
            bola_campeao = bola_1
        else:
            lugar1 = n_3
            lugar2 = n_1
            nome_campeao = n_3
            bola_campeao = bola_3
    print("Tite está mais indeciso do que nunca!")
    print(f'{lugar1}\n{lugar2}\n{lugar3}')
    print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")
    if bola_campeao <= 10:
        print(f'{nome_campeao}?! Sei não hein Galvão…')
    else:
        print(f'{nome_campeao}! Dessa vez o hexa vem pra casa!!')

## Jogador3 == 3º lugar
elif bola_3 < bola_1 and bola_3 < bola_2:
    lugar3 = n_3
    if bola_1 == bola_2:
        if aprvmt_1 > aprvmt_2:
            lugar1 = n_1
            lugar2 = n_2
            nome_campeao = n_1
            bola_campeao = bola_1
        else:
            lugar1 = n_2
            lugar2 = n_1
            nome_campeao = n_2
            bola_campeao = bola_2
    print("Tite está mais indeciso do que nunca!")
    print(f'{lugar1}\n{lugar2}\n{lugar3}')
    print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")
    if bola_campeao <= 10:
        print(f'{nome_campeao}?! Sei não hein Galvão…')
    else:
        print(f'{nome_campeao}! Dessa vez o hexa vem pra casa!!')
        
##TODOS EMPATAM
elif bola_1 == bola_2 == bola_3: 
    print("Tite está mais indeciso do que nunca!")
   #Jogador 1 Vencer
    if aprvmt_1 > aprvmt_2 and aprvmt_1 > aprvmt_3:
        print(f'{n_1}')
        if aprvmt_2 > aprvmt_3:
            print(f'{n_2}\n{n_3}')
            print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")
        elif aprvmt_3 > aprvmt_2: 
            print(f'{n_3}\n{n_2}')
            print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")
        if bola_1 <= 10:
            print(f'{n_1}?! Sei não hein Galvão…')
        else:
            print(f'{n_1}! Dessa vez o hexa vem pra casa!!')
    ## Jogador 2 Vencer
    if aprvmt_2 > aprvmt_1 and aprvmt_2 > aprvmt_3:
        print(f'{n_2}')
        if aprvmt_1 > aprvmt_3:
            print(f'{n_1}\n{n_3}')
            print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")   
        elif aprvmt_3 > aprvmt_1: 
            print(f'{n_3}\n{n_1}')
            print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")
        if bola_2 <= 10:
            print(f'{n_2}?! Sei não hein Galvão…')
        else:
            print(f'{n_2}! Dessa vez o hexa vem pra casa!!')
            
        ## Jogador 3 Vencer
    if aprvmt_3 > aprvmt_1 and aprvmt_3 > aprvmt_2:
        print(f'{n_3}')
        if aprvmt_1 > aprvmt_2:
            print(f'{n_1}\n{n_2}')
            print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")
        elif aprvmt_2 > aprvmt_1: 
            print(f'{n_2}\n{n_1}')
            print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")
        if bola_3 <= 10:
            print(f'{n_3}?! Sei não hein Galvão…')
        else:
            print(f'{n_3}! Dessa vez o hexa vem pra casa!!')