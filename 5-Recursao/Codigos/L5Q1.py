n_iniciais = input().split(" ")
n = int(input())
progressao = []
#Transformando os numeros iniciais em inteiros:
for i in range(len(n_iniciais)):
    n_iniciais[i] = int(n_iniciais[i])
    progressao.append(n_iniciais[i])

razao = n_iniciais[2] - n_iniciais[1]

# Razão : 3
# Lista : 6 9 12 15 18 21 24 27 30

#Tentando calcular a progressão
def calcular_progressao(n):
    #Aqui é o caso base, se o n é == ao tamanho da progressão
    if n == 1:
        return progressao[n-1]
 
    else:
        return  calcular_progressao(n-1) + razao
print(f"Na progressão aritmética cujos três primeiros números são {progressao[0]}, {progressao[1]} e {progressao[2]}, o {n}º elemento é {calcular_progressao(n)} e a razão da progressão é {razao}.")