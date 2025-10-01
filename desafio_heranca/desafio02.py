class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10
    
class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20
    
funcionario_1 = Funcionario("Dorival", 3000)
gerente_1 = Gerente("Clarisse", 5000)
print(f"Funcionário: {funcionario_1.nome} | Salário: {funcionario_1.salario} | Bônus: 10%")

print(f"Gerente: {gerente_1.nome} | Salário: {gerente_1.salario} | Bônus: 20%")