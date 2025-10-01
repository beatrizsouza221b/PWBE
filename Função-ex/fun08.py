def area_quadrado():
    lado = float(input("Digite o valor do lado do quadrado: "))

    soma = lado ** 2
    return soma

resultado = area_quadrado()
print(f"A area do quadardo é", resultado)
