from Produto import Produtos

class Salgados(Produtos):
    def __init__(self, Nome, Preco, Quantidade,Sodio,Tipo, Recheio):
        super().__init__(Nome, Preco, Quantidade,Sodio)
        self.__tipo= Tipo
        self.__recheio= Recheio

    def getNome(self):
        return self._nome

    def getPreco(self):
        return self._preco

    def getQuantidade(self):
        return self._quant

    def getSodio(self):
        return self._sodio

    def getTipo(self):
        return self.__tipo

    def getRecheio(self):
        return self.__recheio

    def setNome(self, nom):
        self._nome = nom

    def setPreco(self, pre):
        self._preco = pre

    def setQuantidade(self, quanti):
        self._quant = quanti

    def setSodio(self, sod):
        self._sodio = sod

    def setTipo(self, salga):
        self.__tipo= salga

    def setRecheio(self, sabores):
        self.__recheio=sabores

    def mostraProduto(self):
        print('SALGADOS')
        super().mostraProduto()
        print('Tipo:', self.__tipo)
        print('Sabor: ', self.__recheio)