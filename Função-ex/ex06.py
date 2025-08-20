<<<<<<< HEAD
def numero_digitos():
    numero = str(input("Digite um numero: "))
    digito = len(numero)

    return digito

resultado = numero_digitos()
print(resultado)
=======
list = []

for i in range(10):
    numeros = int(input(f"Digite um número {i + 1}: "))
    list.append(numeros)

for numeros in list:
    if numeros > 0:
        print("esses são os número positivos dessa lista", {numeros})
>>>>>>> 356f9c7db0d01f814c9ef6c49e9c330222580ab6
