n = int(input())
criaturas = []
tamanho_criaturas = 0

criaturas_ordenadas = []
lista_final = ""
cont_criaturas = 0

for a in range(n):
    nome = input()
    nome_repetido = False
    for b in (criaturas):
        if (b == nome):
            nome_repetido = True
        else:
            nome_repetido = nome_repetido
    if not (nome_repetido):
        criaturas.append(nome)

#Criando um for que vai percorrer o indice/tamanho da lista criaturas do ultimo pro primeiro.
for _ in range((len(criaturas)-1)):
  for d in range(len(criaturas)-1):
    if criaturas[d] > criaturas[d+1]:
        criaturas[d], criaturas[d+1] = criaturas[d+1], criaturas[d]





print(*criaturas, sep=", ")

##POSSO USAR LISTA[J], LISTA[J+1] = LISTA[J+1], LISTA[J]