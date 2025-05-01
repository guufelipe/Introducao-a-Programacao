ano = int(input())

#selecao1
nome_selecao1 = input()
vitorias_time1 = int(input())
empates_time1 = int(input())
pontuacao_1 = ((vitorias_time1 * 3) + empates_time1)

#selecao2
nome_selecao2 = input()
vitorias_time2 = int(input())
empates_time2 = int(input())
pontuacao_2 = pontuacao_2 = ((vitorias_time2 * 3) + empates_time2)

#selecao 3 
nome_selecao3 = input()
vitorias_time3 = int(input())
empates_time3 = int(input())
pontuacao_3 = pontuacao_3 = ((vitorias_time3 * 3) + empates_time3)

tipo_consulta = input()

# Criterio Geral
if tipo_consulta == "Critério Geral":
    # time 1 campeao
    if pontuacao_1 > pontuacao_2 and pontuacao_1 > pontuacao_3 and pontuacao_2 > pontuacao_3:
        print(f'A classificação na copa de {ano} foi:')
        print(f'{nome_selecao1} - {pontuacao_1}')
        print(f'{nome_selecao2} - {pontuacao_2}')
        print(f'{nome_selecao3} - {pontuacao_3}')
    elif pontuacao_1 > pontuacao_2 and pontuacao_1 > pontuacao_3 and pontuacao_3 > pontuacao_2:
        print(f'A classificação na copa de {ano} foi:')
        print(f'{nome_selecao1} - {pontuacao_1}')
        print(f'{nome_selecao3} - {pontuacao_3}')
        print(f'{nome_selecao2} - {pontuacao_2}')
    #time 2 campeao
    elif pontuacao_2 > pontuacao_1 and pontuacao_2 > pontuacao_3 and pontuacao_1 > pontuacao_3:
        print(f'A classificação na copa de {ano} foi:')
        print(f'{nome_selecao2} - {pontuacao_2}')
        print(f'{nome_selecao1} - {pontuacao_1}')
        print(f'{nome_selecao3} - {pontuacao_3}')
    elif pontuacao_2 > pontuacao_1 and pontuacao_2 > pontuacao_3 and pontuacao_3 > pontuacao_1:
        print(f'A classificação na copa de {ano} foi:')
        print(f'{nome_selecao2} - {pontuacao_2}')
        print(f'{nome_selecao3} - {pontuacao_3}')
        print(f'{nome_selecao1} - {pontuacao_1}')
    #time 3 campeao
    elif pontuacao_3 > pontuacao_1 and pontuacao_3 > pontuacao_2 and pontuacao_1 > pontuacao_2:
        print(f'A classificação na copa de {ano} foi:')
        print(f'{nome_selecao3} - {pontuacao_3}')
        print(f'{nome_selecao1} - {pontuacao_1}')
        print(f'{nome_selecao2} - {pontuacao_2}')
    elif pontuacao_3 > pontuacao_1 and pontuacao_3 > pontuacao_2 and pontuacao_2 > pontuacao_1:
        print(f'A classificação na copa de {ano} foi:')
        print(f'{nome_selecao3} - {pontuacao_3}')
        print(f'{nome_selecao2} - {pontuacao_2}')
        print(f'{nome_selecao1} - {pontuacao_1}')

#Ordem Lexicográfica
if tipo_consulta == "Ordem Lexicográfica":
# time 1 campeao
    if nome_selecao1 < nome_selecao2 and nome_selecao1 < nome_selecao3 and nome_selecao2 < nome_selecao3:
        print(f'O times por ordem Lexicográfica da copa de {ano} são:')
        print(f'{nome_selecao1} - {pontuacao_1}')
        print(f'{nome_selecao2} - {pontuacao_2}')
        print(f'{nome_selecao3} - {pontuacao_3}')
    elif nome_selecao1 < nome_selecao2 and nome_selecao1 < nome_selecao3 and nome_selecao3 < nome_selecao2:
        print(f'O times por ordem Lexicográfica da copa de {ano} são:')
        print(f'{nome_selecao1} - {pontuacao_1}')
        print(f'{nome_selecao3} - {pontuacao_3}')
        print(f'{nome_selecao2} - {pontuacao_2}')
#time 2 campeao
    elif nome_selecao2 < nome_selecao1 and nome_selecao2 < nome_selecao3 and nome_selecao1 < nome_selecao3:
        print(f'O times por ordem Lexicográfica da copa de {ano} são:')
        print(f'{nome_selecao2} - {pontuacao_2}')
        print(f'{nome_selecao1} - {pontuacao_1}')
        print(f'{nome_selecao3} - {pontuacao_3}')
    elif nome_selecao2 < nome_selecao1 and nome_selecao2 < nome_selecao3 and nome_selecao3 < nome_selecao1:
        print(f'O times por ordem Lexicográfica da copa de {ano} são:')
        print(f'{nome_selecao2} - {pontuacao_2}')
        print(f'{nome_selecao3} - {pontuacao_3}')
        print(f'{nome_selecao1} - {pontuacao_1}')
#time 3 campeao
    elif nome_selecao3 < nome_selecao1 and nome_selecao3 < nome_selecao2 and nome_selecao1 < nome_selecao2:
        print(f'O times por ordem Lexicográfica da copa de {ano} são:')
        print(f'{nome_selecao3} - {pontuacao_3}')
        print(f'{nome_selecao1} - {pontuacao_1}')
        print(f'{nome_selecao2} - {pontuacao_2}')
    elif nome_selecao3 < nome_selecao1 and nome_selecao3 < nome_selecao2 and nome_selecao2 < nome_selecao1:
        print(f'O times por ordem Lexicográfica da copa de {ano} são:')
        print(f'{nome_selecao3} - {pontuacao_3}')
        print(f'{nome_selecao2} - {pontuacao_2}')
        print(f'{nome_selecao1} - {pontuacao_1}')


        #PQ TA COLOCANDO A SELECAO 1 PRIMEIRO,SE O CASO DELE JA PASSOU