#raio do circulo
def raio_circulo():
    area = int(input("Digite o valor da area do circulo: "))

    divisao = area / 3.14
    raio = divisao ** (1/2)

    return raio 

raio = raio_circulo()
print(f"O raio do circulo é", {raio})