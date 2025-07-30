list = []
while True:
    numero = int(input("Digite um número positivo: "))
    list.append(numero)

    if numero >= 0:
        numero = int(input("Digite um número positivo: "))
        list.append(numero)

    else:
        print("Número inválido")
        print(f"O maior número digitado foi: {max(list)}")
        exit()