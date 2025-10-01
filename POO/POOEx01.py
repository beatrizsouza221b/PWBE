class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f"Esses são os detalhes desse carro: \n marca: {self.marca}\nModelo: {self.modelo}\n Ano: {self.ano}")

Adicionando_carro_1 = Carro("Fiat", "Stilo", 2020)
Adicionando_carro_1.detalhes()
