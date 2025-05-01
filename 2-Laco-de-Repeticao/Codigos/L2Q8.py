
cont_dia = 0
cont_noite = 0

## declarando atividades diurnas:
atividades_diurnas = ""
jantar = False
centrinho = False
lual = False
festa = False

## declarando atividades noturnas
atividades_noturnas = ""
praia_amor = False
surf = False
lancha = False
praia_pipa = False
chapadao = False
buggy = False
tirolesa = False



atividades_noite = ""
atividades_dia = input()
while(atividades_dia != "NOITE"):
    if (atividades_dia != "NOITE"):
        cont_dia += 1
    if (atividades_dia == "Ir para a Praia do Amor"):
        if (praia_amor == False):
            atividades_diurnas += "Ir para a Praia do Amor" + "\n"
            praia_amor = True
        else:
           cont_dia -= 1 
           atividades_diurnas += "[INVALIDO]" + "\n"
    elif (atividades_dia == "Passeio de Lancha"):
        if (lancha == False):
            atividades_diurnas += "Passeio de Lancha" + "\n"
            lancha = True
        else:
            cont_dia -= 1
            atividades_diurnas += "[INVALIDO]" + "\n"
    elif (atividades_dia == "Surf na Praia de Pipa"):
        if (surf == False):
            atividades_diurnas += "Surf na Praia de Pipa" + "\n"
            surf = True
        else:
            cont_dia -= 1
            atividades_diurnas += "[INVALIDO]" + "\n"
    elif (atividades_dia == "Por do sol no chapadão"):
        if (chapadao == False):   
            atividades_diurnas += "Por do sol no chapadão" + "\n"    
            chapadao = True
        else:
            cont_dia -= 1
            atividades_diurnas += "[INVALIDO]" + "\n"
    elif (atividades_dia == "Passeio de buggy"):
        if (buggy == False):
            atividades_diurnas += "Passeio de buggy" + "\n"    
            buggy = True
        else:
            cont_dia -= 1
            atividades_diurnas += "[INVALIDO]" + "\n"
    elif (atividades_dia == "Arborismo e Tirolesa"):
        if(tirolesa == False):
            atividades_diurnas += "Arborismo e Tirolesa" + "\n"
            tirolesa = True
        else:
            cont_dia -= 1
            atividades_diurnas += "[INVALIDO]" + "\n"
    elif (atividades_dia != "NOITE" and atividades_dia != "Ir para a Praia do Amor" and atividades_dia != "Surf na Praia de Pipa" and atividades_dia != "Por do sol no chapadão" and atividades_dia != "Passeio de buggy" and atividades_dia != "Arborismo e Tirolesa" and atividades_dia != ""):
          cont_dia -= 1
          atividades_diurnas += "[INVALIDO]" + "\n"
    
    atividades_dia = input()


if (cont_dia %2 == 0):
    while (atividades_noite != "Oba, Tudo planejado!!"):
        atividades_noite = input()
        if (atividades_noite != "Oba, Tudo planejado!!"):
            cont_noite += 1

        if (atividades_noite == "Jantar gastronômico"):
            if (jantar == False) :
                atividades_noturnas += "Jantar gastronômico" + "\n"
                jantar = True
            else:
                cont_noite -= 1
                atividades_noturnas += "[INVALIDO]" + "\n"
        elif (atividades_noite == "Passear pelo centrinho"):
            if (centrinho == False):
                atividades_noturnas += "Passear pelo centrinho" + "\n"
                centrinho = True
            else:
                cont_noite -= 1
                atividades_noturnas += "[INVALIDO]" + "\n"
        elif (atividades_noite == "Luau"):
            if (lual == False):
                atividades_noturnas += "Luau" + "\n"
                lual = True
            else:
                cont_noite -= 1
                atividades_noturnas += "[INVALIDO]" + "\n"
        elif (atividades_noite == "Festa com DJ"):
            if(festa == False):
                atividades_noturnas += "Festa com DJ" + "\n"
                festa = True
            else:
                cont_noite -= 1
                atividades_noturnas += "[INVALIDO]" + "\n"

        elif (atividades_noite != "Oba, Tudo planejado!!" and atividades_noite != "Passear pelo centrinho" and atividades_noite != "Luau" and atividades_noite != "Festa com DJ"):
            cont_noite -= 1
            atividades_noturnas += "[INVALIDO]" + "\n"

else:
    for i in range (2):
        atividades_noite = input()
        cont_noite += 1
        if (atividades_noite == "Jantar gastronômico"):
            if (jantar == False) :
                    atividades_noturnas += "Jantar gastronômico" + "\n"
                    jantar = True
            else: 
                cont_noite -= 1
                atividades_noturnas += "[INVALIDO]" + "\n"        
        elif (atividades_noite == "Passear pelo centrinho"):
            if (centrinho == False):
                atividades_noturnas += "Passear pelo centrinho" + "\n"
                centrinho = True
            else: 
                cont_noite -= 1
                atividades_noturnas += "[INVALIDO]" + "\n"
        elif (atividades_noite == "Luau"):
            if (lual == False):
                atividades_noturnas += "Luau" + "\n"
                lual = True
            else:
                cont_noite -= 1
                atividades_noturnas += "[INVALIDO]" + "\n"
        elif (atividades_noite == "Festa com DJ"):
            if(festa == False):
                atividades_noturnas += "Festa com DJ" + "\n"
                festa = True
            else:
                cont_noite -= 1
                atividades_noturnas += "[INVALIDO]" + "\n"
        elif (atividades_noite != "Oba, Tudo planejado!!" and atividades_noite != "Passear pelo centrinho" and atividades_noite != "Luau" and atividades_noite != "Festa com DJ"):
            cont_noite -= 1
            atividades_noturnas += "[INVALIDO]" + "\n"


print("Roteiro emitido!")
print("DIA:")
if(atividades_diurnas != ""):
    print(atividades_diurnas [:-1])

print( "NOITE:")
if(atividades_noturnas != ""):
    print(atividades_noturnas [:-1])

print(f'Venha curtir esse dia em Pipa com um roteiro com {cont_dia + cont_noite} atividade(s)!')