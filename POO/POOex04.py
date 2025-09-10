class Produto:
    def __init__(self, nome_produto, preco_uni, qtd_disponivel):
        self.nome_produto = nome_produto
        self.preco_uni = preco_uni
        self.qtd_disponivel = qtd_disponivel

    def mostrar_estoque(self):
        print(f"Produto: {self.nome_produto},\nPreço: R${self.preco_uni}\nQuantidade em estoque:{self.qtd_disponivel}")

produto_1 = Produto("Celular", "R$2000,00", "200")
produto_1.mostrar_estoque()
