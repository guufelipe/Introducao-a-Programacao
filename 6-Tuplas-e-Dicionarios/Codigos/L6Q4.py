animais = {
    'cachorro': (['gato'], ['coleira', 'ração', 'ursinho de pelúcia']),
    'gato': (['cachorro', 'hamster', 'peixe'], ['bola de lã', 'caixa de areia', 'ração', 'ratinho de brinquedo']),
    'hamster': (['cachorro', 'gato'], ['ração', 'roda para hamster', 'serragem']),
    'peixe': (['gato'], ['aquário', 'filtro', 'ração'])
}

#CACHORRO E HAMSTER E PEIXE
animais_consulta = input().split(' e ')
rn = input()
if rn == "sim ":
    rn = True
elif rn == "nao":
    rn = False

relacao_inimigos = []
animais_listados = True
ha_inimigos = False


#Conferindo se todos os animais estão listados no dicionario
for i in animais_consulta:
    if i not in animais.keys():
        print(f"Sérgio, o animal {i} não estava nas suas potenciais escolhas, logo ele não pode ser analisado.")
        animais_listados = False

if animais_listados:
    for i in animais_consulta:
        # Se são Recem Nascidos:
        if rn:
            if i == animais_consulta[0]:
                print("Como os animais são recém nascidos, eles podem ser adotados juntos!")       
                print("Segue aqui as necessidades dos animais:")
                print(f"As necessidades do(a) {i} são:")
                for j in range(len(animais[i][1])):
                    print(f"- {animais[i][1][j]};")
            
            elif i == animais_consulta[-1]:
                print(f"As necessidades do(a) {i} são:")
                for j in range(len(animais[i][1])):
                    print(f"- {animais[i][1][j]};")
                print("Dito isso, vamos adotá-los!!!")
            
            else:
                print(f"As necessidades do(a) {i} são:")
                for j in range(len(animais[i][1])):
                    print(f"- {animais[i][1][j]};")


        #Se não são Recem Nascidos:
        else:
        #Conferindo os inimigos
            for j in animais_consulta:
                if j in animais[i][0]:
                    ha_inimigos = True
                    print(f"Sérgio, o(a) {i} tem o(a) {j} como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos")


if animais_listados:                    
    if not ha_inimigos and not rn:
        for i in animais_consulta:
            if i == animais_consulta[0]:
                print("Segue aqui as necessidades dos animais:")
                print(f"As necessidades do(a) {i} são:")
                for j in range (len(animais[i][1])):
                    print(f"- {animais[i][1][j]};")
            
            elif i == animais_consulta[-1]:
                print(f"As necessidades do(a) {i} são:")
                for j in range (len(animais[i][1])):
                    print(f"- {animais[i][1][j]};")
                print("Dito isso, vamos adotá-los!!!")              
            else:
                print(f"As necessidades do(a) {i} são:")
                for j in range (len(animais[i][1])):
                    print(f"- {animais[i][1][j]};")