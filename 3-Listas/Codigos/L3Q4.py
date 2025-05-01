tamanho = int(input())
chave = int(input())
sequencia = []
numeros = input()
sequencia = numeros.split(", ")
sequencia_nova = []
str_sequencia = ""
# len_lis [ ¹  ²  ³]
# lista: 1, 2, 3, 4  
# lista[(3+1)% len_lis] = lista[0]

if chave > 0:
    sinal = 1
elif chave < 0:
    sinal = -1
if chave != 0:
    for i in range(tamanho):
        num_novo = 0
        for j in range (i+ (sinal), i + chave + sinal, sinal):
            indice = j % len(sequencia)
            num_novo += int(sequencia[indice])
        sequencia_nova.append(num_novo)
    for k in sequencia_nova:
        k = str(k)
        if( k != sequencia_nova[len(sequencia_nova) -1]):
            str_sequencia += (f"{k}, ")
        
    print(f"Vamos lá Gideãozinho a sequencia final é {str_sequencia[:-2]}")

else:
    num_novo = 0
    for i in range(tamanho):
        sequencia[i] = 0
        sequencia_nova.append(sequencia[i])
    for k in sequencia_nova:
        k = str(k)
        if( k != sequencia_nova[len(sequencia_nova) -1]):
            str_sequencia += (f"{k}, ")
    print(f"Não foi dessa vez Gideãozinho a chave corrompeu e a sequencia ficou assim: {str_sequencia[:-2]}")