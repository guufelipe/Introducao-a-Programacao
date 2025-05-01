n = int(input())
pets = {}
nome = ""
estado = ""
amigos = []
desordeiros = []



for i in range (n):
    nome, estado, *amigos = input().split(", ")
    pets[nome] = (estado, amigos)

for i in pets.keys():
    if len(pets[i][1]) == 1:
        if not i in desordeiros:
          desordeiros.append(i)
    
    if pets[i][0] == "agitado" and len(pets[i][1]) <= 3:
        if not i in desordeiros:
          desordeiros.append(i)

if len(desordeiros) == 0:
  print("Todos estão se divertindo tranquilamente! Os queridos cuidadores podem relaxar!")

elif len(desordeiros) == 1:
  print(f"Apenas {desordeiros[0]} está querendo bagunçar, deem carinho e atenção imediatamente!")

else:
    string_desordeiros = ", ".join(desordeiros[:-1])
    string_desordeiros += (f' e {desordeiros[-1]}')
    print(f'Vai ser um trabalho difícil, mas {string_desordeiros} podem acabar atrapalhando os alunos do CIn!')
