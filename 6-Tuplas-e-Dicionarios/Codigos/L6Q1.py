n = int(input())
nomes = []
especies = []
datas = []
chaves = []
valores = []
aniversariantes = []

#Separando as informações por cada animalzinho
for i in range (n): 
    [i.append(j) for i, j in zip([nomes, especies, datas], input().split(" "))]

animais = {}

datas = [int(data[3] + data[4]) for data in datas]

for i in range(len(nomes)):
    animais[nomes[i]] = (especies[i], datas[i])

mes= int(input())

#Preciso ordenar os nomes em ordem alfabetica.
nomes = sorted(nomes)


for i in nomes:
  if animais[i][1] == mes:
    aniversariantes.append(i)
    aniversariantes.append(animais[i][0])
    
if aniversariantes != []:
  print("E os donos da festa do mes sao:")
  for i in range (0, len(aniversariantes), 2):
    print(f"{aniversariantes[i]} - {aniversariantes[i+1]}")


else:
  print("Sem festa esse mes. :(")