<<<<<<< HEAD
def area_retangulo():
    base = float(input("Digite o valor da base do retangulo: "))
    altura = float(input("Digite o valor do altura do retangulo: "))

    soma = base * altura
    return soma

resultado = area_retangulo()
print(f"A area do retangulo é", resultado)
=======
senha = 1234

nome = input("Digite seu nome: ")

senha_tentativa = int(input(f"Bem vindo {nome}!\nDigite sua senha: "))

while True:
    if senha_tentativa != senha:
        senha_tentativa = int(input("Senha incorreta!\nTente novamente, digite sua senha:\n-> "))

    else:
        print("Login realizado!")
        break
>>>>>>> 356f9c7db0d01f814c9ef6c49e9c330222580ab6
