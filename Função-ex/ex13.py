def eh_par(numero):
    if numero % 2 == 0:
        return True
    return False

numero = int(input("Digite um numero para saber se ele é par: "))

print(eh_par(numero))
