caes = {}
n = int(input())
pets = {}

nome = ""
raca = ""
notas = []
aulunos = []
media_aulunos = []
racas = []
situacao = []

caes_aprovados = []
caes_reprovados = []
caes_recuperacao = []


for i in range (n):
    nome, raca, *notas = input().split(", ")
    caes[nome] = raca, notas
    
for i in caes.keys():
  aulunos.append(i)


for i in aulunos:
  
  #Definindo as medias
  media = float(caes[i][1][0])
  media += float(caes[i][1][1])
  media += float(caes[i][1][2])
  media /= 3
  
  media_aulunos.append(media)
  

  #Separando as Raças
  racas.append(caes[i][0])
  
#Calculando as situações:
for i in range (len(aulunos)):
  if media_aulunos[i] >= 3:
    situacao.append("Aprovado")
  
  elif media_aulunos[i] < 2:
    situacao.append("Reprovado")
  
  elif media_aulunos[i] >= 2 and media_aulunos[i] < 3:
    situacao.append("Recuperação")
  
#Criando o novo dicionario com os nomes, medias e raças organizadas:  

for i in range(len(aulunos)):
  pets[aulunos[i]] = (racas[i], media_aulunos[i], situacao[i])
  
  
for i in aulunos:
  if pets[i][2] == "Aprovado":
    caes_aprovados.append(i)

  elif pets[i][2] == "Reprovado":
    caes_reprovados.append(i)
  
  elif pets[i][2] == "Recuperação":
    caes_recuperacao.append(i)
  

if caes_aprovados != []:
  print("Estao aprovados e de parabens os seguintes coleguinhas:")
  for i in caes_aprovados:
    nome_pet = i 
    raca_pet = pets[i][0]
    media_pet = pets[i][1]
    
    print(f"{nome_pet} - {raca_pet} - media: {media_pet:.2f}")

if caes_reprovados != []:
  print("Os colegas a seguir nao se comportaram bem e precisam de ajuda profissional (entrar em contato urgente):")
  for i in caes_reprovados:
    nome_pet = i 
    raca_pet = pets[i][0]
    media_pet = pets[i][1]
  
    print(f"{nome_pet} - {raca_pet} - media: {media_pet:.2f}")

if caes_recuperacao != []:
  print("Esses queridos terao uma nova chance e prometem melhorar:")
  for i in caes_recuperacao:
    nome_pet = i 
    raca_pet = pets[i][0]
    media_pet = pets[i][1]
    
    print(f"{nome_pet} - {raca_pet} - media: {media_pet:.2f}")