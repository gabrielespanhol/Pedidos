import PySimpleGUI as sg


def menu():
    sg.theme('Reddit')
    layout = [
       [sg.Button('Pedido')],
       [sg.Button('Novo entregador')],
       [sg.Button('Dia novo')]

    ]
    return sg.Window('Menu', layout=layout, finalize=True)


def Pedidos():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome'), sg.Input(key='nome',)],
        [sg.Text('Pedido'), sg.Input(key='pedido')],
        [sg.Text('Endereço'), sg.Input(key='endereco')],
        [sg.Text('Valor R$'), sg.Input(key='valor')],
        [sg.Text('Entregador'), sg.Input(key='entregador')],
        [sg.Checkbox('Cartão', key='cartao'),
         sg.Checkbox('Dinheiro', key='dinheiro'),
         sg.Checkbox('NÃO COBRAR', key='naocobrar', text_color='red',)],

        [sg.Button('Limpar dados'), sg.Button('Continuar'), sg.Checkbox('Adicionar Data', key='adicinardata')]

    ]
    return sg.Window('Tela Pedidos', layout=layout, finalize=True)


def Dados(nome, pedido, endereco, valor, cobrar, entregador):
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome'), sg.Text(nome)],
        [sg.Text('Pedido'), sg.Text(pedido)],
        [sg.Text('Endereço'), sg.Text(endereco)],
        [sg.Text('Valor'), sg.Text('R$ '+valor)],
        [sg.Text('Pagamento'), sg.Text(cobrar)],
        [sg.Text('Entregador'), sg.Text(entregador)],
        [sg.Button('Voltar'), sg.Button('Enviar pedido')]
    ]

    return sg.Window('Confirmar dados do pedido', layout=layout, finalize=True)
