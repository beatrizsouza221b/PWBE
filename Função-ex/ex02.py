#calculo de IMC

def calcular_IMC():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    IMC = peso / (altura ** 2)
    print("Seu IMC é ", IMC)
    return IMC
   
print("Bem vindo!\n Este programa soma seu IMC")
calcular_IMC()

print("Tabela de IMC\nAbaixo de 18.5: Abaixo do peso\n18,5 - 24.9: Peso normal\n25 - 29.9: Execsso de peso\nAcima de 30: Obesidade")