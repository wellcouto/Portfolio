import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
# Your Auth Token from twilio.com/console
auth_token  = "#############################"
client = Client(account_sid, auth_token)

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc [tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} o vendedor {vendedor} vendeu R${vendas}!!!")
        message = client.messages.create(
            to="+15558675309",
            from_="+15017250604",
            body=f"No mês {mes} o vendedor {vendedor} vendeu R${vendas}!!!")
        print(message.sid)
