def area_retangulo():
    base = float(input("Digite o valor da base do retangulo: "))
    altura = float(input("Digite o valor do altura do retangulo: "))

    soma = base * altura
    return soma

resultado = area_retangulo()
print(f"A area do retangulo é", resultado)