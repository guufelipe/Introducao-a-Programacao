protetor_solar = False
dinheiro = 0
clima = "ensolarado"
entrada = ""

while (entrada != "ir para a praia"):
    entrada = input()
    if(entrada == "separar dinheiro"):
        dinheiro_adcionado = float(input())
        dinheiro += dinheiro_adcionado
    elif(entrada == "passar protetor"):
        protetor_solar = True
    elif(entrada == "choveu"):
        clima = "chuvoso"
    elif(entrada == "parou de chover"):
        clima = "ensolarado"
else:
    if(clima == "chuvoso"):
        print("Hoje não vai dar pra ir, chuvinha barrou")
    elif(clima == "ensolarado"):
        print("Hoje tem sol e mar!")

        if(protetor_solar == False and dinheiro < 10.00):
            print("Você não chegou muito bem, chame um médico!")
        elif(protetor_solar == False and dinheiro >= 10.00):
            print("O novo camarão do CIn foi criado")
        elif(protetor_solar == True and dinheiro < 10.00):
            print("Só faltou uma aguinha de coco...")
        elif(protetor_solar == True and dinheiro >= 10.00):
            print("Aí sim! Hoje rendeu!")

