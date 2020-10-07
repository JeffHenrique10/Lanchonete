from lanchonete import Lanchonete
from refrigerantes import Refrigerante
from salgados import Salgados
from sucos import Sucos
from doces import Doces
from agua import Agua
from Vendas import Vendas

lan= Lanchonete('Bom Lanche', 'Timon' ,'10 as 22 horas', 32128597)
refri= Refrigerante('Sprite Green', 2.00, 50,'32 mg', 'Sprite', 1, 'Limão')
sal= Salgados('Coxinha', 3.50, 100,'89 mg','Salgados', 'Frango')
suc= Sucos('Suco',1.70, 120,'17 mg','Natural', 'Laranja')
doce= Doces('Brownie', 2.00, 60,'89 mg','Chocolate')
ag= Agua('Agua Mineral',2.00, 100,'23 mg','Ouro da Mina', 1)
refri2=Refrigerante('Fanta Uva',4.00,45,'57 mg','Fanta',2,'Laranja')
sal2= Salgados('Pastel', 3.50, 75, '86 mg', 'Salgado', 'Carne')
doce2= Doces('Brigadeiro',2.50,50,'100 mg','Chocolate')

#Lanchonete
lan.adicionarProdutos(refri)
lan.adicionarProdutos(ag)
lan.adicionarProdutos(suc)
lan.adicionarProdutos(doce)
lan.adicionarProdutos(sal)
lan.adicionarProdutos(refri2)
lan.adicionarProdutos(sal2)
lan.adicionarProdutos(doce2)
lan.mostraDados()


print('--'*10,'Informações dos produtos',('--'*10))
refri.mostraProduto()
print('--'*45)
sal.mostraProduto()
print('--'*45)
suc.mostraProduto()
print('--'*45)
doce.mostraProduto()
print('--'*45)
ag.mostraProduto()
print('--'*45)
refri2.mostraProduto()
print('--'*45)
sal2.mostraProduto()
print('--'*45)
doce2.mostraProduto()
print('--'*45)


#Cliente1
v1=Vendas('Fabricio','05/12/2018','15:30')

#Cliente2
v2=Vendas('Julia','05/12/2018','16:30')

#VendaCliente1
print(('-='*7),v1.getNome(),('-='*7))
v1.addProdutoVenda(refri)
v1.addProdutoVenda(sal)
v1.addProdutoVenda(doce)
v1.mostrarListaVenda()
lan.AdicionarVendas(v1)
print(('-='*23))
v1.Vender()
v1.EmitirConta()
v1.AplicarDesconto()

#VendaCliente2
print(('-='*7),v2.getNome(),('-='*7))
v2.addProdutoVenda(doce2)
v2.addProdutoVenda(suc)
v2.addProdutoVenda(sal2)
v2.mostrarListaVenda()
lan.AdicionarVendas(v2)
print(('-='*23))
v2.Vender()
v2.EmitirConta()
v2.AplicarDesconto()
lan.LucroDia('05/12/2018')

