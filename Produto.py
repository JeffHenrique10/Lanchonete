class Produtos:
    def __init__(self,Nome, Preco, Quantidade, Sodio):
        self._nome = Nome
        self._preco = Preco
        self._quant = Quantidade
        self._sodio=Sodio

    def getNome(self):
        return self._nome

    def getPreco(self):
        return self._preco

    def getQuantidade(self):
        return self._quant

    def getSodio(self):
        return self._sodio

    def setNome(self, nom):
        self._nome=nom

    def setPreco(self, pre):
        self._preco= pre

    def setQuantidade(self,quanti):
        self._quant= quanti

    def setSodio(self,sod):
        self._sodio=sod

    def mostraProduto(self):
        print('Nome: ', self._nome)
        print('Preço: ', self._preco)
        print('Quantidade: ', self._quant)
        print('Sodio: ',self._sodio)