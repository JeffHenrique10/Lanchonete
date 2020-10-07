from Produto import Produtos

class Sucos(Produtos):
    def __init__(self,Nome,Preco, Quantidade,Sodio,Tipo, Sabor):
        super().__init__(Nome,Preco, Quantidade, Sodio)
        self.__tipo= Tipo
        self.__sabor= Sabor

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

    def setTipo(self, suc):
        self.__tipo=suc

    def setSabor(self, sabores):
        self.__sabor=sabores


    def mostraProduto(self):
        print('SUCOS')
        super().mostraProduto()
        print('Tipo:', self.__tipo)
        print('Sabor: ', self.__sabor)