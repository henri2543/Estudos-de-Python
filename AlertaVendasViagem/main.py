import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACeade5162105bea2e6f79419e4b5c46d3"
# Your Auth Token from twilio.com/console
auth_token = "0db608a16071f31d5499e4e442a43d7c"

client = Client(account_sid, auth_token)


# Passo a passo de solução

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    # Para cada arquivo:
    # Verificar se algum valor na coluna de vendas do arquivo analisado é maior que 55.000

    if (tabela_vendas['Vendas'] > 55000).any():

        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]

        valor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        print(f'No mês de {mes}  o vendedor {vendedor} com R${valor},00 de vendas')

        # Se for maior do que 55.000 -> Envia um SMS com o nome / mês / valor

        message = client.messages.create(
            to="+5511975354644",
            from_="+12055092229",
            body=f'No mês de {mes}  o vendedor {vendedor} com R${valor},00 de vendas')

        print(message.sid)

# Caso não seja maior que 55.000, fazer nada