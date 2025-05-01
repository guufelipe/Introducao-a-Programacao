nome_invencao = input()

nome_etapa = ""
status_etapa = ""
total_falhas = 0
despesa_total = 0
etapa_realizada = 0

#loop se a etapa não for desistir ou concluir

while (nome_etapa != "concluir" and nome_etapa != "desistir"):
    nome_etapa = input()

    #se etapa for "dar um plus"

    if (nome_etapa == "dar um plus"):
        custo_etapa = int(input())
        print(f"Agora o(a) {nome_invencao} ficou ainda mais legal! Pena que precisei gastar R${custo_etapa}")
        despesa_total += custo_etapa

    #se não for "dar um plus"    

    elif (nome_etapa != "concluir" and nome_etapa != "desistir" and nome_etapa != "dar um plus" ):
        custo_etapa = int(input())
        tentativas_etapa = int(input())

        #loop das tentativas
        
            #vai pedir novos status enquanto for "incorreto" ou "ainda não chegar no numero de tentativas"
        cont = 0
        status_etapa = ""
        while (status_etapa != "correto" and cont < tentativas_etapa):
            cont += 1
            status_etapa = input()
            despesa_total += custo_etapa

                #O que vai fazer se for "incorreto":

            if (status_etapa == "incorreto"):
                total_falhas += 1
                print(f"Ainda não consegui {nome_etapa} corretamente, e essa tentativa me custou R${custo_etapa}")

                
                  
        #O que vai fazer se for "correto" ou acabar as tentativas :    
        else:
            if (status_etapa == "correto"):
                etapa_realizada += 1
                print(f"Oba! consegui {nome_etapa}, o que me custou R${custo_etapa}")
            if (cont >= tentativas_etapa or status_etapa == "correto") :       
                print(f"ANDAMENTO DO PROJETO: Etapas realizadas - {etapa_realizada} ; Tentativas falhas - {total_falhas}")
#se desistir ou concluir      
else:
    print(f"A jornada da construção do(a) {nome_invencao} acaba aqui.")
    if (nome_etapa == "concluir"):
        print(f"Uhuuu, finalmente o(a) {nome_invencao} tá pronto(a)! Esse projeto me custou R${despesa_total}")
    elif (nome_etapa == "desistir"):
        print(f"Infelizmente, o sonho do(a) {nome_invencao} foi interrompido e levou junto com ele R${despesa_total}")
