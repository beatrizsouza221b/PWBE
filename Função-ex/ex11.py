<<<<<<< HEAD
def hipotenusa():
    cateto1 = float(input("Digite o valor do cateto1: "))
    cateto2 = float(input("Digite o valor do cateto2: "))

    soma = (cateto1 ** 2) + (cateto2 ** 2)
    raiz = soma ** (1/2)
    return raiz

resultado = hipotenusa()
print(f"O valor da hipotenusa é", resultado)
=======
numero = int(input("Digite um número de 1 a 100: "))

resultado = 1

for i in range(1, numero + 1):
    resultado *= i

print(f"O fatorial de {numero} é {resultado}")
>>>>>>> 356f9c7db0d01f814c9ef6c49e9c330222580ab6
