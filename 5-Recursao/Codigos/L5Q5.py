
#DEFININDO AS SEQUENCIAS:
resultado = []
ultima_lista = []
numeros = input().split(", ")
def definirSequencia(num, resultados, ultima_lista):
    if len(num) == 0:
        return resultados
    else:
        ''' Verificando se restam mais de 2 elementos na lista, para ter o controle exato, quando sobrarem
                só dois devemos interagir com eles de forma diferente'''
        if len(num) > 2:
            if int(num[1]) == int(num[0]) + 1:
                ultima_lista.append(num[0])
                #Retirando o primeiro elemento
                num.remove(num[0])
                return definirSequencia(num, resultado, ultima_lista)
            
            else:
                ultima_lista.append(num[0])
                resultados.append(ultima_lista)
                ultima_lista = []
                num.remove(num[0])
                return definirSequencia(num, resultado, ultima_lista)

            ''' Se sobrarem dois numeros e continuarmos interagindo como antes vai apagar o primeiro e vai sobrar
                o ultimo, ele não vai ter proximo elemento e na interação vai dar index out of range'''
        elif len(num) == 2:
            #Se eles forem sequencia adiciona tudo na ultima lista, e insere no resultado.
            if int(num[1]) == int(num[0]) +1:
                ultima_lista.append(num[0])
                ultima_lista.append(num[1])
                num = []
                resultado.append(ultima_lista)
                ultima_lista = []
            
            #Caso contrario, eles não são sequencia e o primeiro item deve ir pra ultima sequencia e o ultimo vai pra sequencia de forma separada.
            else:
                ultima_lista.append(num[0])
                resultado.append(ultima_lista)
                ultima_lista = []
                ultima_lista.append(num[1])
                resultado.append(ultima_lista)
                num = []

            return(definirSequencia(num, resultado, ultima_lista))

#Definindo intervalos:
intervalos = []
intervalo_atual = []
def definirIntervalos(sequencias, intervalos, intervalo_atual):
    if sequencias == []:
        return intervalos
    
    else:
        if len(sequencias[0]) > 1:
            primeiro_numero = int(sequencias[0][0])
            ultimo_numero = int(sequencias[0][-1])
            intervalo_atual.append(primeiro_numero)
            intervalo_atual.append(ultimo_numero)
            intervalos.append(intervalo_atual)
            intervalo_atual = []

        elif len(sequencias[0]) == 1:
            intervalos.append(sequencias[0])
            intervalo_atual = []

        sequencias.remove(sequencias[0])
        return definirIntervalos(sequencias, intervalos, intervalo_atual)

sequencias = (definirSequencia(numeros, resultado, ultima_lista))
intervalos_das_sequencias = (definirIntervalos(resultado, intervalos, intervalo_atual))


saida = ""
for i in range (len(intervalos_das_sequencias)):
    if i < len(intervalos_das_sequencias) - 1:
        if len(intervalos_das_sequencias[i]) == 2:
            saida += (f"[{intervalos_das_sequencias[i][0]}-{intervalos_das_sequencias[i][-1]}], ")
        elif len(intervalos_das_sequencias[i]) == 1:
            saida += (f"[{intervalos_das_sequencias[i][0]}], ")
    
    elif i == len(intervalos_das_sequencias) - 1:
        if len(intervalos_das_sequencias[i]) == 2:
            saida += (f"[{intervalos_das_sequencias[i][0]}-{intervalos_das_sequencias[i][-1]}]")
        elif len(intervalos_das_sequencias[i]) == 1:
            saida += (f"[{intervalos_das_sequencias[i][0]}]")

if len(numeros) != 1:
    print(saida)
else:
    print(f"[{int(numeros[0])}]")