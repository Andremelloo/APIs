import tkinter as tk  ## importar a biblioteca toda e colocando um apelido para ela com o nome tk
from twilio.rest import Client
from secrets import account_sid, auth_token

##________________________________________________________________
# SID da sua conta em twilio.com/console
account = account_sid
# Seu token de autenticação de twilio.com/console
token = auth_token
client = Client(account, token)
##______________________________________________________________

def enviar_sms():
    nome_remetente_preenchido = caixa_input_remetente.get()  ## pegando o que o usuario colocou no campo nome_remetente e colocando em uma variavel.
    numero_preechido = caixa_input_numero_destino.get()  ## pegando o que o usuario colocou no campo numero_distino e colocando em uma variavel.
    texto_sms_preechido = caixa_input_sms.get("1.0",
                                       tk.END)  ## pegando o que o usuario colocou no campo text_sms e colocando em uma variavel.

    try:
        message = client.messages.create(
            to="+" + numero_preechido,
            from_="+12677109979",
            body="Enviado por: " + nome_remetente_preenchido + "\n" + texto_sms_preechido)
        print("SMS Enviado com sucesso")
        text_OK = tk.Label(text="SMS Enviado com sucesso!!")  ## Escrevendo um text na janela
        text_OK.grid(row=5, column=1, sticky="NSEW")  ## colocando na jenela o texto / row=linha e colum=coluna

    except:
        print("error, número errado!")
        text_NOK = tk.Label(text="Número errado!!", fg='red')  ## Escrevendo um text na janela
        text_NOK.grid(row=5, column=1, sticky="NSEW")  ## colocando na jenela o texto / row=linha e colum=coluna

##--------------------------------------------------------------------------------------------------------------------------------------------

janela = tk.Tk()  ## Abrindo uma janela no Tkinter
janela.title("Enviar SMS gratis !!")  ## colocando titulo na sua janela.

janela.rowconfigure(0, weight=1)  ## ajustando automaticamente conforme voce abra a janela.
janela.columnconfigure([0, 1], weight=1)  ## ajustando automaticamente conforme voce abra a janela.

label_mensagem0 = tk.Label(text="Nome Remetente :", padx=10, anchor='w')  ## Escrevendo um text na janela / padx, dar space para os lados/ anchor alinhar o texto para qual lado  NSEW
label_mensagem1 = tk.Label(text="Número Destinatário :", padx=10)  ## Escrevendo um text na janela
label_mensagem2 = tk.Label(text="Escreva seu SMS aqui :", padx=10)  ## Escrevendo text na janela

label_mensagem0.grid(row=0, column=0, sticky="NSEW")  ## colocando na jenela o texto / row=linha e colum=coluna
label_mensagem1.grid(row=1, column=0,  sticky="NSEW")  ## colocando na jenela o texto / row=linha e colum=coluna
label_mensagem2.grid(row=4, column=0, sticky="NSEW")  ## colocando na jenela o texto / row=linha e colum=coluna


caixa_input_remetente = tk.Entry(borderwidth=2, relief='solid')  ## colocando um campo de input / borderwidth=2, colocar borda na caixa / relief='solid'
caixa_input_numero_destino = tk.Entry(borderwidth=2, relief='solid')  ## colocando um campo de input
caixa_input_sms = tk.Text(width=50, height=10, borderwidth=2, relief='solid')  ## colocando um campo de input

caixa_input_remetente.grid(row=0, column=1, sticky="NSEW", padx=20, pady=10)  ## / padx, dar space para o lado / pady, dar space para baixo e cima
caixa_input_numero_destino.grid(row=1, column=1, sticky="NSEW", padx=20, pady=10)
caixa_input_sms.grid(row=4, column=1, columnspan=4, sticky="NSEW", padx=20)

space = tk.Label(text="                                                         ")
space.grid(row=1, column=3, sticky="NSEW", padx=20, pady=10)


botao_enviar = tk.Button(text="Enviar SMS",
                  command=enviar_sms, borderwidth=2, relief='solid')  ## tk.Button criar um botão / command= enviar_sms, é o nome da função que vai ser executad, quando clicar no botão.
botao_enviar.grid(row=6, column=1, columnspan=4, padx=10, pady=20)


janela.mainloop()  ## criando janela em um loob infinito.
