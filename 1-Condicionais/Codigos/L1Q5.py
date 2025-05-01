n_1 = input()
t_1Gols = 0
t_1Erros = 0

n_2 = input()
t_2Gols = 0
t_2Erros = 0

vencedor = 0
qtd_chutes_rest_1 = 5
qtd_chutes_rest_2 = 5
dfr_gols = 0

##CHUTES
ent_1 = input()
qtd_chutes_rest_1 -= 1
if ent_1 == "Gol":
    t_1Gols += 1
else:
    t_1Erros += 1
    
ent_2 = input()
qtd_chutes_rest_2 -= 1
if ent_2 == "Gol":
    t_2Gols += 1
else:
    t_2Erros += 1
    
    
ent_3 = input()
qtd_chutes_rest_1 -= 1
if ent_3 == "Gol":
    t_1Gols += 1
else:
    t_1Erros += 1
    
ent_4 = input()
qtd_chutes_rest_2 -= 1
if ent_4 == "Gol":
    t_2Gols += 1
else:
    t_2Erros += 1
    
ent_5 = input()
qtd_chutes_rest_1 -= 1
if ent_5 == "Gol":
    t_1Gols += 1
else:
    t_1Erros += 1
    
ent_6 = input()
qtd_chutes_rest_2 -= 1
if ent_6 == "Gol":
    t_2Gols += 1
else:
    t_2Erros += 1
if t_1Gols > t_2Gols:
    dfr_gols = (t_1Gols - t_2Gols)
elif t_2Gols > t_1Gols:
    dfr_gols = (t_2Gols - t_1Gols) 
    
if((t_1Gols > t_2Gols) and (qtd_chutes_rest_2 < dfr_gols)) or ((t_1Gols < t_2Gols) and (qtd_chutes_rest_1 < dfr_gols)):
    if t_1Gols > t_2Gols:
        vencedor = n_1
        gols_vencedor = t_1Gols
        gols_perdedor = t_2Gols
        print(f"{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!")
    elif t_2Gols > t_1Gols:
        vencedor = n_2
        gols_vencedor = t_2Gols
        gols_perdedor = t_1Gols
        print(f"{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!")
else:
    ent_7 = input()
    qtd_chutes_rest_1 -= 1 
    if ent_7 == "Gol":
        t_1Gols += 1
    else:
        t_1Erros += 1   
    if t_1Gols > t_2Gols:
        dfr_gols = (t_1Gols - t_2Gols)
    elif t_2Gols > t_1Gols:
        dfr_gols = (t_2Gols - t_1Gols)
        
    if((t_1Gols > t_2Gols) and (qtd_chutes_rest_2 < dfr_gols)) or ((t_1Gols < t_2Gols) and (qtd_chutes_rest_1 < dfr_gols)):
        if t_1Gols > t_2Gols:
            vencedor = n_1
            gols_vencedor = t_1Gols
            gols_perdedor = t_2Gols
            print(f"{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!")
        elif t_2Gols > t_1Gols:
            vencedor = n_2
            gols_vencedor = t_2Gols
            gols_perdedor = t_1Gols
            print(f"{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!")
    else:
        ent_8 = input()
        qtd_chutes_rest_2 -= 1
        if ent_8 == "Gol":
            t_2Gols += 1
        else:
            t_2Erros += 1
        if t_1Gols > t_2Gols:
            dfr_gols = (t_1Gols - t_2Gols)
        elif t_2Gols > t_1Gols:
            dfr_gols = (t_2Gols - t_1Gols)
        
        if((t_1Gols > t_2Gols) and (qtd_chutes_rest_2 < dfr_gols)) or ((t_1Gols < t_2Gols) and (qtd_chutes_rest_1 < dfr_gols)):
            if t_1Gols > t_2Gols:
                vencedor = n_1
                gols_vencedor = t_1Gols
                gols_perdedor = t_2Gols
                print(f"{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!")
            elif t_2Gols > t_1Gols:
                vencedor = n_2
                gols_vencedor = t_2Gols
                gols_perdedor = t_1Gols
                print(f"{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!")
        else:
            ent_9 = input()
            qtd_chutes_rest_1 -= 1
            if ent_9 == "Gol":
                t_1Gols += 1
            else:
                t_1Erros += 1
            if t_1Gols > t_2Gols:
                dfr_gols = (t_1Gols - t_2Gols)
            elif t_2Gols > t_1Gols:
                dfr_gols = (t_2Gols - t_1Gols)        
                
           
            if((t_1Gols > t_2Gols) and (qtd_chutes_rest_2 < dfr_gols)) or ((t_1Gols < t_2Gols) and (qtd_chutes_rest_1 < dfr_gols)):
                if t_1Gols > t_2Gols:
                    vencedor = n_1
                    gols_vencedor = t_1Gols
                    gols_perdedor = t_2Gols
                    print(f"{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!")
                elif t_2Gols > t_1Gols:
                    vencedor = n_2
                    gols_vencedor = t_2Gols
                    gols_perdedor = t_1Gols
                    print(f"{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!")
            else:
                ent_10 = input()
                qtd_chutes_rest_2 -= 1
                if ent_10 == "Gol":
                    t_2Gols += 1
                else:
                    t_2Erros += 1
                if t_1Gols > t_2Gols:
                    vencedor = n_1
                    gols_vencedor = t_1Gols
                    gols_perdedor = t_2Gols
                    print(f"{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!")
                elif t_2Gols > t_1Gols:
                    vencedor = n_2
                    gols_vencedor = t_2Gols
                    gols_perdedor = t_1Gols
                    print(f"{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!")
                elif t_2Gols == t_1Gols:
                    print(f'Ambas as seleções terminaram com {t_1Gols} gols, mas o desempate vai ficar para outro dia.')
        