from Produto import Produtos
class Doces(Produtos):
    def __init__(self,Nome, Preco, Quantidade,Sodio,Sabor):
        super().__init__(Nome, Preco, Quantidade,Sodio)
        self.__sabor= Sabor

    def getNome(self):
        return self._nome

    def getPreco(self):
        return self._preco

    def getQuantidade(self):
        return self._quant

    def getSodio(self):
        return self._sodio

    def getSabor(self):
        return self.__sabor

    def setNome(self, nom):
        self._nome=nom

    def setPreco(self, pre):
        self._preco= pre

    def setQuantidade(self,quanti):
        self._quant= quanti

    def setSodio(self,sod):
        self._sodio=sod

    def setSabor(self, sabores):
        self.__sabor=sabores

    def mostraProduto(self):
        print('DOCES')
        super().mostraProduto()
        print('Sabor: ', self.__sabor)