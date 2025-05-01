vida_denji = 1000
porcentagem_denji = 100
vida_zombie = 1000
porcentagem_zombie = 100
fim_game = False

def calcular_porcentagem(a):
    if a == vida_denji:
            return int(vida_denji * 0.1)
    if a == vida_zombie:
            return int(vida_zombie * 0.1)



print("Denji fez pacto com Pochita. Que comece a luta.")
while vida_denji > 0 and vida_zombie > 0:
    personagem = input()
    golpe = input()
    dano = int(input())
    if personagem != "Denji" and personagem != "ZombieDevil":
        print("Esse personagem não está lutando, escolha entre Denji ou Zombie Devil.")
    if golpe != "ataque" and golpe != "defesa":
        print("Esse golpe não existe, escolha entre ataque ou defesa.")

    #Calculando ataques e porcentagens
    if golpe == "ataque" and not fim_game:
        if personagem == "Denji":
            vida_zombie -= dano
            if vida_zombie > 0:
                print(f"Uhu, Denji atacou! A porcentagem de vida atual do Zombie Devil é de {calcular_porcentagem(vida_zombie)}%.")
                #Conferindo se Zombie devil morreu
            if vida_zombie <= 0:
                print("O Chainsaw Man conseguiu sua vingança, o Zombie Devil está morto!")
                fim_game = True
        elif personagem == "ZombieDevil":
            vida_denji -= dano
            if vida_denji > 0:
                print(f"Ah não, Denji foi atacado pelo Zombie Devil! A porcentagem de vida atual de Denji é de {calcular_porcentagem(vida_denji)}%.")    
            #Conferindo se Denji morreu
            if vida_denji <= 0:
                print("Infelizmente o Chainsaw Man está morto e não há ninguém para puxar sua corrente e revive-lo.")
                fim_game = True
    #Calculando defesa 
    elif golpe == "defesa" and not fim_game:
        if personagem == "Denji":
            print("Isso aê! O feitiço virou contra o feiticeiro. Denji defendeu o golpe do Zombie Devil e ganhou um bônus de vida.")
            vida_denji += dano
            if vida_denji > 1000:
                vida_denji = 1000
            vida_zombie -= dano
            #Conferindo se Zombie devil morreu
            if vida_zombie <= 0:
                print("O Chainsaw Man conseguiu sua vingança, o Zombie Devil está morto!")
                fim_game = True
        
        elif personagem == "ZombieDevil":
            print("Ops! O Zombie Devil defendeu o ataque de Denji e ganhou um bônus de vida.")
            vida_zombie += dano
            if vida_zombie > 1000:
                vida_zombie = 1000
            vida_denji -= dano
            #Conferindo se Denji morreu
            if vida_denji <= 0:
                print("Infelizmente o Chainsaw Man está morto e não há ninguém para puxar sua corrente e revive-lo.")
                fim_game = True

        if (vida_denji > 0 and vida_zombie > 0) and (personagem == "Denji" or personagem == "ZombieDevil"):
            print(f"A porcentagem de vida atual de Denji é de {calcular_porcentagem(vida_denji)}% e do Zombie Devil é de {calcular_porcentagem(vida_zombie)}%.")

