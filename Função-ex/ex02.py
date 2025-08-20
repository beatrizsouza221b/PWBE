#calculo de IMC

def calcular_IMC():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    IMC = peso / (altura ** 2)
    print("Seu IMC é ", IMC)
    return IMC
   
print("Bem vindo!\n Este programa soma seu IMC")
calcular_IMC()