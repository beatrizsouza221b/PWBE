<<<<<<< HEAD
#binario para decimal

def binario_para_decimal(binario):
    numero = binario[::-1]
    potencia = 0
    soma = 0
    for i in numero:
        soma += int(i) * (2**potencia)
        potencia += 1
    
    return soma

binario = input("Digite um número binário: ")
print(binario_para_decimal(binario))
=======
import random

numero = random.randint(1, 100)

while True:
    tentativa = int(input("Tente advinhar o número secreto (escolha um número inteiro de 1 a 100): "))

    if tentativa == numero:
        print("Você advinhou!!")
        break

    elif tentativa > numero:
        print("O número que você escolheu é maior que o número secreto")

    else:
        print("O número que você escolheu é menor que o número secreto")

>>>>>>> 356f9c7db0d01f814c9ef6c49e9c330222580ab6
