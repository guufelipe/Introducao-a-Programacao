contador = 0
frase = input()
while (frase != "O relógio descarregou!" and frase != "Por hoje já deu"):
    contador += 1
    frase = input()
else: 
    if frase == "O relógio descarregou!":
        print(f'Corra Ben! Você já derrotou {contador} aliens')
    elif frase == "Por hoje já deu":
        print (f'Muito Ben Ben! hehe você derrotou {contador} aliens hoje')