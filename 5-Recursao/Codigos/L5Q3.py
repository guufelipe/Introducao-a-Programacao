numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#FUNÇÕES:
#Mensagem usuario
def converter_texto_usuario(mensagem, posicao, letras, letra_da_vez):
    if len(mensagem) == posicao:
        return letras 
       
    else:
        letra = mensagem[posicao]
        if posicao == 0:
          letra_da_vez = letra
          letras.append([letra, 1])
        
        else:
          if letra == letra_da_vez:
            letras[-1][1] += 1
          
          else:
            letras.append([letra,1])
            letra_da_vez = letra

        return converter_texto_usuario(mensagem, posicao + 1, letras,letra_da_vez)
#Mensagem GPT
def converter_texto_gpt(soma):
    if 0 < soma <= 5:
        return "1t3a1 1f1a1c3i1n1h1o1 1n3e"
    
    elif 6 < soma <= 20:
        return "1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o"

    elif 21 < soma <= 30:
        return "1s6o1 1n1a1 1v1i1d2a1 1m4a1n1s3a"
    
    elif 31 < soma <= 40:
        return "1v5a1 1e2s1t4u3d3a3r1 1r1a1p3a3z"
    
    elif 40 < soma:
        return "3e1s1t5u1d1a1 1n2a1o1 1p1r3a1 1t2u1 1v4e1r"
    
#Descomprimir (Mensagem GPT)
resultado = ""
def descomprimir_texto_gpt(texto_descomprimir, resultado):
    lista_texto = list(texto_descomprimir)
    if len(lista_texto) == 0:
        return resultado
    
    else:
        multiplicador = int(lista_texto[0])
        letra = lista_texto[1]
        for i in range(multiplicador):
            resultado += letra
        return descomprimir_texto_gpt(texto_descomprimir[2:], resultado)    


codigo = ""
texto_p_traduzir = ""
ultima_palavra = ""

while codigo != "Preciso parar de usar o ChatGPT":
    codigo = input()
    continuar = True
    if codigo == "Vou pedir ajuda pro meu amigo ChatGPT":
        while continuar:          
            texto_p_traduzir = input()
            
            if texto_p_traduzir != "Não tô entendendo nada":
                texto_p_traduzir = texto_p_traduzir.split(" ")
                qtd = len(texto_p_traduzir)
                palavra = ""
                soma = 0
                letras = []
                numeros_mensagem = []
                mensagem_gpt = []
                for i in range(qtd):
                    converter_texto_usuario(texto_p_traduzir[i], 0, letras, letra_da_vez = texto_p_traduzir[i][0])
                    if i < qtd - 1:
                        letras.append([" ", 1])
                #Formando a palavra do usuario  
                for b in range (len(letras)) :
                    palavra += str(letras[b][1])+ letras[b][0]
                #calculando a soma das repetições
                for j in (palavra):
                    if j in numeros:
                        soma += int(j)


                print(f"usuário:{palavra}")
                print(f"ChatGPT:{converter_texto_gpt(soma)}")
                ultima_palavra = converter_texto_gpt(soma)

                soma = 0
                palavra = ""
            else: 
                continuar = False
    elif codigo == "Qual era a tradução?":
        if ultima_palavra != "":
            ultima_traducao = descomprimir_texto_gpt(ultima_palavra, resultado)
            print(f'Descobri! É: {ultima_traducao}, tá de brincadeira né?')
        else:
            print("Não tem nada pra traduzir")

    
# a = 'abc'
# a.isnumber()