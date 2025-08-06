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

