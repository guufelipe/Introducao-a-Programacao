texto = input()
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
cont = len(texto)

#alan turing

#inverter a palavra:

def inverter(palavra, tamanho):
    if tamanho == 1:
        return palavra[0]
    else:
        return texto[tamanho -1] + inverter(palavra, tamanho -1)

palavra_invertida = inverter(texto, len(texto))
print(palavra_invertida)