objeto_procurado = input()

objetos_encontrados = input().split(", ")
objetos_repetidos = []
obj_rptd = []
algum_objt_repetiu = False
repeticao_maior = 0


# gancho de alpinismo

#           0                     1                     2                      3               4                5          6
# boné antigo do Dipper, boné antigo do Dipper, novo boné do Dipper, gancho de alpinismo, boné do Soos, boné do Soos, boné do Soos
#           A          ,          A           ,         B          ,           C        ,      D       ,      D     ,      D
#For para selecionar todos os itens repetidos:
for i in range (len(objetos_encontrados)):
    cont = 0
    for j in range ((i +1), len(objetos_encontrados)):
        if (objetos_encontrados[i] == objetos_encontrados[j]):
            if not i in (objetos_repetidos):
                algum_objt_repetiu = True
                objetos_repetidos.append(i)
                objetos_repetidos.append(j)
                cont += 2
                
            else:
              algum_objt_repetiu = True
              if not j in (objetos_repetidos):
                objetos_repetidos.append(j)
                cont += 1
    #Conferindo se o contador atual é maior que o numero de repetição anterior            
    if cont > repeticao_maior:
        repeticao_maior = cont

#Criando uma lista com o nome de cada item repetido uma unica vez para printar            
for i in (objetos_repetidos):
   if not objetos_encontrados[int(i)] in obj_rptd:
        obj_rptd.append(objetos_encontrados[int(i)])

#for para printar os itens repetidos
if algum_objt_repetiu:
    for i in obj_rptd:            
        print(f"Após análises, percebi que {i} foi coletado mais de uma vez...")

#Calculando o coeficiente de erros de viagens interdimensionais:
if algum_objt_repetiu:
    coef = float(len(objetos_encontrados)/repeticao_maior)
    print(f"Certo, o coeficiente de erros de viagens interdimensionais é {coef:.2f}")


if not objeto_procurado in obj_rptd:
    if objeto_procurado in objetos_encontrados:
        print("Você encontrou o item necessário para me ajudar a voltar para minha dimensão! Finalmente voltarei para Gravity Falls!")
    else:
        print("Que pena, você não encontrou o item necessário para me ajudar a voltar para minha dimensão...")
else:
    print("Que pena, você não encontrou o item necessário para me ajudar a voltar para minha dimensão...")

print('''(Como prometido, você retorna ao DA do CIn. Mas, por razões desconhecidas, você se esquece do ocorrido)\nO walkie-talkie está na sua mão. Depois de um tempo, você diz: "Que aparelho velho!"\n(Após pensar sobre o que fazer com o walkie-talkie, você resolve jogá-lo no banheiro do CIn)''')