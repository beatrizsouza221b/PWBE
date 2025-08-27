class SuperHeroi:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder
        self.capa = True

    def salvar(self):
        print(f"{self.nome} salvou o mundo! Parabéns")

    def comer(self, comida):
        print(f"{self.nome} comeu {comida}")
        
    def destruir_carros(self, quantos_carros):
        for i in range(quantos_carros):
            print(F"{self.nome} destruiu um carro com o poder de {self.poder}") 

    def derrotar_vilao(self, nome_vilao):
        print(f"O herói {self.nome} derrotou seu arquinimigo {nome_vilao}")


Super_Heroi_1 = SuperHeroi("Spider-Man", "Soltar veias");
Super_Heroi_1.salvar()
Super_Heroi_1.destruir_carros(2)
Super_Heroi_1.derrotar_vilao("Doende verde")
Super_Heroi_1.poder = "dormir"
Super_Heroi_1.destruir_carros(5)

super_heroi_2 = SuperHeroi("Homem de ferro", "Inteligencia")
super_heroi_2.salvar()
Super_Heroi_1.salvar()
