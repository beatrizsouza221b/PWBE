def eh_par(numero):
    return numero % 2 == 0 
#foi feito uma verificação, e a resposta devolvida é true or false

nuumero = int(input("Digite um número: "))
resultado = eh_par(nuumero)
print("O numero é", resultado)