n = int(input())
n_primo = False


def conferir_numero_primo(n):
    if n == 1:
        return False
    for count in range (2, n):
        if n % count == 0:
            return False
    return True
            
def numeros_primos_anteriores(n):
    numeros_primos = []
    for numero in range (2, n):
        if conferir_numero_primo(numero):
            numeros_primos.append(numero)
    return numeros_primos
        

n_primo = conferir_numero_primo(n)



if n_primo:
    print(f"O número {n} é primo.")

if not n_primo:
    print(f"O número {n} não é primo.")
    lista = numeros_primos_anteriores(n)
    if lista != []:
        print(f"Entretanto, temos primos no intervalo de 1 à {n}. Estes são:")
        print(*lista, sep = ", ")

    elif lista == []:
        print(f"Além disso, não temos primos no intervalo de 1 à {n}.")

print("AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!")