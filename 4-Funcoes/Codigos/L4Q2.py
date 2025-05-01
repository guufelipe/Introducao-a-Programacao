probabilidades = []
nomes = []
probabilidade_ok = False
count_amor = 0
count_morte = 0

def conferindo_probabilidade(probabilidade):
    if probabilidade <= 50:
        return True
    else: 
        return False

def conferir_chances(count_amor, count_morte):
    if count_amor > count_morte:
        return True
    else:
        return False

nome = input()
while nome != "cabo":
    if len(nome) <= 7:
        nomes.append(nome)
        probabilidade = int(input())
        probabilidades.append(str(probabilidade))
    
        if nome == "Makima":
            print("Woof Woof")
        
        if ((len(nome) <= 7) and (conferindo_probabilidade(probabilidade)) or nome == "Makima"):
            count_amor +=1
            print(f"Beleza {nome}!! Essa é uma boa pretendente!")
        else:
            count_morte += 1
            print(f"{nome}, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?")
        
    
    else: 
        print(f"Er {nome[:2]}.. errr... nao consigo lembrar, melhor deixar para la")
    nome = input()
   

else:
    
    if conferir_chances(count_amor, count_morte):
        print("Epa ai sim! E hoje pochita!!")
    else:
        print("Desculpa pochita acho que nao vai ser hoje que voce vai poder ver meus sonhos")
    
    if count_morte == 0:
        for i in range(len(nomes)):
            print(f"nome: {nomes[i]} - chances de morrer: {probabilidades[i]}%")


