import random

print("Jogo dos dados\nO objetivo é tirar 7 somando dois dados.")
tentativas = []

while True:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    tentativas.append(dado1)

    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"Soma: {dado1 + dado2}")

    if dado1 + dado2 == 7:
        print("Você tirou 7! Você ganhou!") 
        break  


print(f"Foram necessárias {len(tentativas)} tentativas para tirar 7.")

     

