n = int(input())
_ = input()
msg_pre_traduzida = ""
caracteres_especiais = "! @ $ % & #"
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
seq_letras = ""
msg_traduzida = []
palavras_decodificadoras = []
palavras_codificadas = []
string_final = ""
possibilidade = False

# For pra rodar as quantas entradas eu terei
for i in range(n-1):
    
    decodificadora = input()
    _ = input()
    codificada = input()
    _ = input()

    palavras_decodificadoras.append(decodificadora)
    palavras_codificadas.append(codificada)


decodificadora = input()
_ = input()
codificada = input()
palavras_decodificadoras.append(decodificadora)
palavras_codificadas.append(codificada)


for i in range(n):
    if palavras_decodificadoras[i] == "Portal":
        for j in range(len(caracteres_especiais)):
            a = palavras_codificadas[i]
            a = a.replace(caracteres_especiais[j], "")
            msg_pre_traduzida = a
            
        
        for k in range(len(msg_pre_traduzida)):
            a = msg_pre_traduzida[k]
            if a in alfabeto:
                indice = alfabeto.index(a)
                a = alfabeto[(indice + 1) % len(alfabeto)]
                seq_letras += a
        if seq_letras != "":        
            msg_traduzida.append(seq_letras)
        if msg_traduzida != []:
            possibilidade = True
        seq_letras = ""

    if palavras_decodificadoras[i] == "Experimento":
        #For que vai rodar pela entrada codificada quando a palavra decodificadora for Experimento
        soma_numeros = 0
        for j in ((palavras_codificadas[i])):
            numeros = []
            if j.isdigit():
                if (int(j) % 2 == 0):
                    numeros.append(int(j))
            for l in range (len(numeros)):
                    soma_numeros += numeros[l]
        msg_traduzida.append(str(soma_numeros))
        possibilidade = True        

    if palavras_decodificadoras[i] == "Realidade":
        #For que vai rodar pela entrada codificada quando a palavra decodificadora for Realidade
        numeros = []
        soma_numeros = 0
        for j in (palavras_codificadas[i]):
                if j.isdigit():
                    numeros.append(int(j))
        for l in range (len(numeros)):
            if (numeros[l] % 2 != 0):
                soma_numeros += numeros[l] 
        msg_traduzida.append(str(soma_numeros)) 
        possibilidade = True 
    
    if palavras_decodificadoras[i] == "Schembulock":
        #For que vai rodar pela entrada codificada quando a palavra decodificadora for Schembulock
        multiplicacao = 1
        numeros = []

        for j in palavras_codificadas[i]:
            if j.isdigit():
                numeros.append(int(j))

        for l in (numeros):
            multiplicacao *= l

        msg_traduzida.append(str(multiplicacao))
        possibilidade = True

for i in range (len(msg_traduzida)):
    if i < (len(msg_traduzida) - 1):
        string_final += (f"{msg_traduzida[i]} ")
    elif i == (len(msg_traduzida) -1):
        string_final += msg_traduzida[i]

if possibilidade:
    print(f"Consegui! A mensagem decodificada de Bill Cipher é: {string_final}")

elif (possibilidade == False):
    print(f"Esse formato de mensagem nem Bill Cipher entenderia!")