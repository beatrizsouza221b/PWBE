senha = 1234

nome = input("Digite seu nome: ")

senha_tentativa = int(input(f"Bem vindo {nome}!\nDigite sua senha: "))

while True:
    if senha_tentativa != senha:
        senha_tentativa = int(input("Senha incorreta!\nTente novamente, digite sua senha:\n-> "))

    else:
        print("Login realizado!")
        break