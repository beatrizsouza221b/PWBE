def eh_impar(numero):
    if numero % 2 != 0:
        return True
    return False
numero = int(input("Digite um numero para saber se ele é ímpar: "))

print(eh_impar(numero))