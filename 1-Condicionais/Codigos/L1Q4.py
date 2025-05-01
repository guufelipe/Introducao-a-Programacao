# narrador 1
nome_narrador_1 = input()
bordao_narrador_1 = input()
e_carismatico_narrador_1 = input()
emocao_narrador_1 = int(input())

pontuacao_1 = 0

# narrador 2 

nome_narrador_2 = input()
bordao_narrador_2 = input()
e_carismatico_narrador_2 = input()
emocao_narrador_2 = int(input())
pontuacao_2 = 0

# teste bordao 1

if bordao_narrador_1 == "PROOOO FUNDO DO GOOOL":
    pontuacao_1 += 15
elif bordao_narrador_1 == "EU QUERO É GRITAR GOL":
    pontuacao_1 -= 10
elif bordao_narrador_1 == "VOCÊ. É. RIDÍCULO":
    pontuacao_1 += 18
elif bordao_narrador_1 == "QUEM SABE NA BOLA PARADA":
    pontuacao_1 -= 5
else:
    pontuacao_1 += 10

# teste bordao 2

if bordao_narrador_2 == "PROOOO FUNDO DO GOOOL":
    pontuacao_2 += 15
elif bordao_narrador_2 == "EU QUERO É GRITAR GOL":
    pontuacao_2 -= 10
elif bordao_narrador_2 == "VOCÊ. É. RIDÍCULO":
    pontuacao_2 += 18
elif bordao_narrador_2 == "QUEM SABE NA BOLA PARADA":
    pontuacao_2 -= 5
else:
    pontuacao_2 += 10

#carisma narrador 1

if e_carismatico_narrador_1 == "sim" :
    pontuacao_1 += 10

pontuacao_1 += emocao_narrador_1

#carisma narrador 2

if e_carismatico_narrador_2 == "sim":
    pontuacao_2 += 10

pontuacao_2 += emocao_narrador_2

#disputa

if pontuacao_1 > pontuacao_2:
  print(f'O(a) narrador(a) escolhido(a) é {nome_narrador_1}! Ele(a) será um(a) sucessor(a) digno(a) para o grande Galvão.')
else:
  print(f'O(a) narrador(a) escolhido(a) é {nome_narrador_2}! Ele(a) será um(a) sucessor(a) digno(a) para o grande Galvão.')
