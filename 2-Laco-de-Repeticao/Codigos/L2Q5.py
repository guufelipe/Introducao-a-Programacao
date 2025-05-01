nota = 0
nota_total = 0
lugar_vencedor = ""
nota_vencedor = 0
lugar_perdedor = ""
nota_perdedor = 1000
empate = False
nomes_empates = ""
nota_empate = 0

n = int(input())
for i in range (n):
    nome_lugar = input()
    while(nota >= 0):
        nota = int(input())
        if (nota >= 0):
           nota_total += nota

    else:
        #CONFERINDO SE NÃO HOUVE EMPATE
        if(nota_total != nota_vencedor):

            #CONFERINDO SE LUGAR ATUAL É VENCEDOR DEPOIS DE UM EMPATE
            if (nota_total > nota_vencedor and empate == True) :
                nota_vencedor = nota_total
                lugar_vencedor = nome_lugar
                nota_total = 0
                nota = 0
                nota_empate = 0
                nomes_empates = ""
                empate = False
            
            #CONFERINDO SE LUGAR ATUAL É VENCEDOR
            elif (nota_total > nota_vencedor) :
                nota_vencedor = nota_total
                lugar_vencedor = nome_lugar
                nota_total = 0
                nota = 0
          

            #CONFERINDO SE LUGAR ATUAL É PERDEDOR    
            elif (nota_total < nota_perdedor):
                nota_perdedor = nota_total
                lugar_perdedor = nome_lugar
                nota_total = 0
                nota = 0
          
        #EM CASO DE EMPATE     
        elif (nota_total == nota_vencedor or nota_total == nota_empate):
            empate = True
            #EMPATE NA PRIMEIRAS ENTRADAS
            if ((nota_empate == 0 and nota_total == nota_vencedor) or nota_total == nota_empate):
                if (nomes_empates == ""):
                    nomes_empates = lugar_vencedor
                    nomes_empates += (", " + nome_lugar)
                    nota_empate = nota_total
                    nota_total = 0
                    nota = 0

                else:
                    nomes_empates += (", " + nome_lugar)
                    nota_empate = nota_total
                    nota_total = 0
                    nota = 0
               
            
       


if (empate == False):
    print(f'{lugar_vencedor} ganhou de lavada de {lugar_perdedor}, com {nota_vencedor} vs {nota_perdedor}')

elif (empate == True):
    print(f'{nomes_empates}')
    print("Tantas opções")