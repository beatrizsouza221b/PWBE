list = []

for i in range(10):
    numeros = int(input(f"Digite um número {i + 1}: "))
    list.append(numeros)

for numeros in list:
    if numeros > 0:
        print("esses são os número positivos dessa lista", {numeros})