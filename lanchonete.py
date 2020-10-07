class Lanchonete:
    def __init__(self, Nome, Local,hFuncionamento, Tel):
        self.__nome= Nome
        self.__local= Local
        self.__funcionamento= hFuncionamento
        self.__telefone= Tel
        self.__listaProduto=[]
        self.__venda=[]

    def getNome(self):
        return self.__nome

    def getLocal(self):
        return self.__local

    def getFuncionamento(self):
        return self.__funcionamento

    def getTelefone(self):
        return self.__telefone

    def getProdutos(self):
        return self.__listaProduto

    def setNome(self,nom):
        self.__nome= nom

    def setLocal(self,endereco):
        self.__local(endereco)

    def setTelefone(self, tel):
        self.__telefone= tel

    def setFuncionamento(self,hfunc):
        self.__funcionamento= hfunc

    def adicionarProdutos(self,produto):
        self.__listaProduto.append(produto)

    def AdicionarVendas(self,vendas):
        self.__venda.append(vendas)

    def LucroDia(self,data):
        LucroNoDia = 0
        for v in self.__venda:
            if v.getData() == data:
                LucroNoDia+=v.getValorConta()

        print('Fatura no dia {} : {:.2f}'.format(data,LucroNoDia))

    def mostraDados(self):
        print('Nome: ', self.__nome)
        print('Local: ', self.__local)
        print('Horario de Funcionamento: ', self.__funcionamento)
        print('Telefones: ',self.__telefone)
        print('Produtos: ')
        print('N°',('--'*3),'Produto',('--' * 15), 'Preço')
        for i, n in enumerate(self.__listaProduto):
            print(i+1,('--'*3),n.getNome(),('--'*20),n.getPreco())






