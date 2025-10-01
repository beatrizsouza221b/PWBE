
def hipotenusa():
    cateto1 = float(input("Digite o valor do cateto1: "))
    cateto2 = float(input("Digite o valor do cateto2: "))

    soma = (cateto1 ** 2) + (cateto2 ** 2)
    raiz = soma ** (1/2)
    return raiz

resultado = hipotenusa()
print(f"O valor da hipotenusa é", resultado)