from Produto import Produtos
class Agua(Produtos):
    def __init__(self,Nome, Preco, Quantidade,Sodio, Marca, Litros,):
        super().__init__(Nome,Preco, Quantidade,Sodio)
        self.__marca= Marca
        self.__litros= Litros

    def getNome(self):
        return self._nome

    def getPreco(self):
        return self._preco

    def getQuantidade(self):
        return self._quant

    def getSodio(self):
        return self._sodio

    def getMarca(self):
        return self.__marca

    def getLitros(self):
        return self.__litros

    def setNome(self, nom):
        self._nome = nom

    def setPreco(self, pre):
        self._preco = pre

    def setQuantidade(self, quanti):
        self._quant = quanti

    def setSodio(self, sod):
        self._sodio = sod

    def setMarca(self, mar):
        self.__marca= mar

    def setLitros(self, L):
        self.__litros= L

    def mostraProduto(self):
        print('AGUA')
        super().mostraProduto()
        print("Marca: ", self.__marca)
        print('Litros:', self.__litros)