
#Qtd de jogos em promoção = N
n = int(input())


for i in range(n):
    sequencia_faltando = ""
    nome = input()
    numero_sequencia = int(input())
    if (numero_sequencia == 2):
        print("Achei a sequel! Hora da diversão!")
    elif (numero_sequencia > 2):
        for repeticao in range(2, numero_sequencia):
           
            if (repeticao == numero_sequencia -1):
                sequencia_faltando += (str(repeticao))
                
            else:
                sequencia_faltando += ( str(repeticao) + ", ")
        print(f'Achamos {nome} {numero_sequencia}, mas você ainda precisa jogar o {sequencia_faltando} antes desse.')
    



    