#Qtd de decodificações:
n = int(input())
sequencias_fibonacci = []
termo = 0
codigo_ascii = ""
posicoes_atualizada = []
codigos_para_traduzir = []
traducao = []
traducao_str = ""

#Mensagens a serem decodificadas:
for i in range(n):
    indice_desejado, posicoes = input().split(" ") 
    #Vendo o elemento que na sequencia de fibonacci
    for j in (indice_desejado):
        ultimo=1
        penultimo=0
            #Se ele deseja encontrar o indice 0 ou 1 na lista de fibonacci vai ser == 0 ou 1
        if indice_desejado == 0:
            sequencias_fibonacci.append(["0"])
        elif indice_desejado == 1:
            sequencias_fibonacci.append(["1"])
        else:
            #Contar os numeros fibonacci até o n-ésimo numero a partir de 2
            for count in range(2 , int(indice_desejado) +1):
                termo = ultimo + penultimo
                penultimo = ultimo
                ultimo = termo
                termo = str(termo)
    sequencias_fibonacci.append(termo)            
    
    posicoes_atualizada.append(posicoes.split("-"))

for i in range(n):
    n_fibonacci_atual = sequencias_fibonacci[i]
    
    a = int(posicoes_atualizada[i][0])
    b = int(posicoes_atualizada[i][-1])

    codigo_ascii = n_fibonacci_atual[a] + n_fibonacci_atual[b]
    codigos_para_traduzir.append(codigo_ascii)

for i in range(n):
    codigo = int(codigos_para_traduzir[i])
    traducao.append(chr(codigo))

for i in range (len(traducao)):
    traducao_str += traducao[i]

print(traducao_str)