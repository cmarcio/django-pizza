pedidos = [
    {
        'nome': 'mario',
        'sabor': 'portuguesa'
    },
    {
        'nome': 'marco',
        'sabor': 'presunto'
    }
]
for pedido in pedidos:
    print('Nome: {} \nSabor:{}'.format(pedido['nome'], pedido['sabor']))
