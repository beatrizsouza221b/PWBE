def area_circulo():
    raio = float(input("Digite o valor do raio do círculo: "))

    soma = (raio ** 2) * 3.14
    return soma

resultado = area_circulo()
print(f"A area do círculo é", resultado)