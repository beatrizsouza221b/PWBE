<<<<<<< HEAD
#calculo de distancia

def distancia_pontos(x1, y1, x2, y2):
    x2_menos_x1 =  x2 - x1
    y2_menos_y1 =  y2 - y1

    x_quadrado = x2_menos_x1 ** 2
    y_quadrado = y2_menos_y1 ** 2

    soma = x_quadrado + y_quadrado

    distancia = soma ** (1/2)
    
    return distancia

x1 = float(input("Digite o valor do ponto x1: "))
x2 = float(input("Digite o valor do ponto x2: "))

y1 = float(input("Digite o valor do ponto y1: "))
y2 = float(input("Digite o valor do ponto y2: "))

resultado = distancia_pontos(x1, x2, y1, y2)
print(resultado)
=======
numero = int(input("Digite um número e obtenha a tabuada dele de 1 a 10: "))

for i in range(1, 11):
    print(f"{i} x {numero} = ", i * numero)
>>>>>>> 356f9c7db0d01f814c9ef6c49e9c330222580ab6
