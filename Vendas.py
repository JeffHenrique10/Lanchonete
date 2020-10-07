from refrigerantes import Refrigerante
from salgados import Salgados
from sucos import Sucos
from doces import Doces
from agua import Agua

class Vendas:
    def __init__(self, NomeCliente,Data, Horario):
        self.__nomeCliente= NomeCliente
        self.__data= Data
        self.__horario= Horario
        self.__lista= []
        self._valorConta= 0
        self.__valordesconto= 0

    def getNome(self):
        return self.__nomeCliente

    def getHorario(self):
        return self.__horario

    def getData(self):
        return self.__data

    def getListaDaVenda(self):
        return self.__lista

    def getValorConta(self):
        return self._valorConta

    def setNome(self,nome):
        self.__nomeCliente = nome

    def setHorario(self,horario):
        self.__horario = horario

    def setData(self,date):
        self.__data=date

    def setListaDaVenda(self,produto):
        self.__lista=produto

    def ValorConta(self,conta):
        self._valorConta=conta

    def addProdutoVenda(self,produto):
        self.__lista.append(produto)

    def mostrarListaVenda(self):
        print('Produtos no "Carrinho" do cliente:', self.__nomeCliente)
        for p in self.__lista:
            print(p.getNome())

    def Vender(self):
        for j in self.__lista:
            quantiAtual = 0
            preco = 0
            quanti=int(input('Digite a quantidade de {} que você irá querer: '.format(j.getNome())))
            print(('-='*23))
            if j.getQuantidade() > quanti:
                preco= preco+(j.getPreco()*quanti)
                quantiAtual = quantiAtual + (j.getQuantidade() - quanti)
                print('O Cliente pediu {} {}. Preço Total:{}'.format(quanti, j.getNome(), preco))
                print('Quantidade de {} da lanchonete foi atualizada de {} para {}'.format(j.getNome(),
                j.getQuantidade(), quantiAtual))
                print(('-=' * 23))
                self._valorConta+=(preco)


    def EmitirConta(self):
        print('Conta do(a) Cliente(a) ', self.getNome())
        print('{:.2f} R$'.format(self._valorConta))

    def AplicarDesconto(self):
        if self._valorConta > 50:
            desconto=self._valorConta*0.05
            self._valorConta-=desconto
            self.__valordesconto+=desconto

        if self._valorConta > 50:
            print('{:.2f} R$ foi Aplicado desconto no valor de: {:.2f} R$'.format(self._valorConta,
            self.__valordesconto))
        else:
            print('{:.2f}R$ não foi Aplicado desconto no valor da conta'.format(self._valorConta))