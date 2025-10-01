class Voador:
    def voar(self):
        return "O pato voa"

class Aquatico:
    def nadar(self):
        return "O pato nada"

class Pato(Voador, Aquatico):
    def habilidades(self):
        print(f"{self.voar()}, {self.nadar()}")

pato1= Pato()
pato1.habilidades()