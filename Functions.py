import PySimpleGUI as sg
import Layouts
from datetime import date


def menu():
    pedidos = Layouts.menu()
    window, event, values = sg.read_all_windows()

    while True:

        if window == pedidos and event == sg.WIN_CLOSED:
            break

        if window == pedidos and event == 'Pedido':
            pedidos.hide()
            fazerPedido()

        if window == pedidos and event == 'Sair':
            break


def fazerPedido():
    # criando as janelas
    pedidos, confirmaDados = Layouts.Pedidos(), None
    # loops
    dados = {}

    while True:
        window, event, values = sg.read_all_windows()
        # print(values['numeroPedido'])

        # quando a janela for fechada
        if window == pedidos and event == sg.WIN_CLOSED:
            break

        if window == pedidos and event == 'Limpar dados':
            window.FindElement('nome').Update('')
            window.FindElement('pedido').Update('')
            window.FindElement('endereco').Update('')
            window.FindElement('valor').Update('')
            window.FindElement('cartao').Update('')
            window.FindElement('dinheiro').Update('')
            window.FindElement('entregador').Update('')
            window.FindElement('naocobrar').Update('')
            window.FindElement('adicinardata').Update('')

        if window == pedidos and event == 'Voltar':
            pedidos.hide()
            menu()

        # quando queremos ir para a proxima janela
        if window == pedidos and event == 'Continuar':

            if values['adicinardata']:
                escreverDoc(inserirData())

            if values['cartao']:
                pedidos.hide()
                confirmaDados = Layouts.Dados(values['nome'], values['pedido'], values['endereco'],
                                              values['valor'], 'Cartao', values['entregador'])

                dados = {'nome': values['nome'], 'pedido': values['pedido'], 'endereco': values['endereco'],
                         'entregador': values['entregador'], 'valor': values['valor'], 'pagamento': 'Cartao'}

            elif values['dinheiro']:
                pedidos.hide()
                confirmaDados = Layouts.Dados(values['nome'], values['pedido'], values['endereco'],
                                              values['valor'], 'Dinheiro', values['entregador'])

                dados = {'nome': values['nome'], 'pedido': values['pedido'], 'endereco': values['endereco'],
                         'entregador': values['entregador'],  'valor': values['valor'], 'pagamento': 'Dinheiro'}

            elif values['naocobrar']:
                pedidos.hide()
                confirmaDados = Layouts.Dados(values['nome'], values['pedido'], values['endereco'],
                                              values['valor'], 'NÃO COBRAR', values['entregador'])

                dados = {'nome': values['nome'], 'pedido': values['pedido'], 'endereco': values['endereco'],
                         'entregador': values['entregador'], 'valor': 'NÃO COBRAR', 'pagamento': 'NÃO COBRAR'}

            else:
                sg.popup("Selecione opcão de pagamento meu amor")

        # quando queremos voltar para janela anterior
        if window == confirmaDados and event == 'Voltar':
            confirmaDados.hide()
            pedidos.un_hide()

        # aqui começa a parte onde armazenamos os dados

        if window == confirmaDados and event == 'Enviar pedido':
            # print('dados {}'.format(dados))
            enviarPedido(dados)
            confirmaDados.hide()
            pedidos.un_hide()


def enviarPedido(dados):
    nome = dados['nome']
    pedido = dados['pedido']
    endereco = dados['endereco']
    valor = dados['valor']
    pagamento = dados['pagamento']
    entregador = dados['entregador']

    if valor == 'NÃO COBRAR':
        Dados = f'Nome: {nome}\n' \
                f'Pedido: {pedido}\n' \
                f'Endereço: {endereco}\n' \
                f'Pagamento: {pagamento}\n\n' \
                f'Entregador:{entregador}\n\n\n' \
                f'-----------------------------\n\n\n'

    else:
        Dados = f'Nome: {nome}\n' \
                f'Pedido: {pedido}\n' \
                f'Endereço: {endereco}\n' \
                f'Cobrar: R${valor}\n' \
                f'Pagamento: {pagamento}\n\n' \
                f'Entregador:{entregador}\n\n\n' \
                f'-----------------------------\n\n\n'

    if pagamento == 'Dinheiro' and valor == '' or pagamento == 'Cartao' and valor == '':
        sg.popup('Acho que você esqueceu o valor gatinha')
    elif nome == '' or pedido == '' or endereco == '':
        sg.popup('Alguma coisa faltando nos dados amor')
    else:
        print(Dados)
        escreverDoc(Dados)


def escreverDoc(Dados):
    with open("Pedidos.txt", "a") as arquivo:
        arquivo.write(Dados)
        arquivo.close()

        # dados = f'Nome: Joao\n' \
        # f'Pedido: #0982\n' \
        # f'Endereço: Rua Aricanduva 343\n' \
        # f'Cobrar: NÃO COBRAR \n\n\n' \
        # f'-----------------------------\n\n\n'


def inserirData():
    DIAS = [
        'Domingo',
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-Feira',
        'Sexta-feira',
        'Sábado'
    ]

    data_atual = date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')

    indice_da_semana = data_atual.isoweekday()
    dia_da_semana = DIAS[indice_da_semana]

    data = f'\n\n---------------------------\n' \
           f'{dia_da_semana.upper()} - {data_em_texto}\n' \
           f'---------------------------\n\n\n'

    return data
