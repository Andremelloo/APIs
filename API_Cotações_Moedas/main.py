import tkinter as tk
from tkinter import ttk

import numpy as np
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import pandas as pd
from datetime import datetime
import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()


lista_moedas = list(dicionario_moedas.keys()) ### ele me da as chaves do dicionario

def pegar_cotacao():
    moeda = combobox_selecionarmoeda.get()
    data_cotacao = calendario_moeda.get()
    print(moeda)
    print(data_cotacao)
        ## como a data vez em formato diferente, tem que arrumar a formataçao delas dessa maneira. para poder usar no link do requests
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f"https://economia.awesomeapi.com.br/{moeda}-BRL/10?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}"
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid'] ## estou pegando no index 0 o "BID" da variavel que é um dicionario "cotacao"
    label_textocotacao['text'] = f"A cotação da {moeda} no dia {data_cotacao} foi de: R$ {valor_moeda}" ## substituir o texto no lavel_textocotacao

    print(link)
    print(valor_moeda)

def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title="Selecione o Arquivo de Moeda")
    var_caminhararquivo.set(caminho_arquivo)  ## variavel exclusiva do tkinter para conseguir acessar em outra funçao
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f"Arquivo Selecionado: {caminho_arquivo}"



def atualizar_cotacoes():
    df = pd.read_excel(var_caminhararquivo.get())
    moedas = ['EUR','USD','BTC']
    data_inicial = calendario_datainicial.get()
    data_final = calendario_datafinal.get()
    novo_df = pd.DataFrame()

    ano_inicia = data_inicial[-4:]
    mes_inicia = data_inicial[3:5]
    dia_inicia = data_inicial[:2]

    ano_final = data_final[-4:]
    mes_final = data_final[3:5]
    dia_final = data_final[:2]
    print(novo_df)
    for moeda in moedas:
        link = f"https://economia.awesomeapi.com.br/{moeda}-BRL/?start_date={ano_inicia}{mes_inicia}{dia_inicia}&end_date={ano_final}{mes_final}{dia_final}"
        print(link)
        requisicao_moeda = requests.get(link)
        cotacoes = requisicao_moeda.json()
        print(cotacoes)
        for cotacao in cotacoes:
            timestamp = int(cotacao['timestamp'])
            bid = float(cotacao['bid'])
            data = datetime.fromtimestamp(timestamp)
            novo_df.loc[data, moeda] = bid
            print("test")
    novo_df.insert(0, column='Data', value=novo_df.index)
    novo_df.index = pd.to_datetime(novo_df.index, dayfirst=True)
    novo_df.sort_index(inplace=True)
    novo_df.to_excel('test.xlsx', index=False)
    label_atualizarcotacoes['text'] = 'Arquivo atualizado com sucesso'

def fechar():
    pass




janela = tk.Tk()

janela.title("Cotação de Moedas")


label_cotacaomoeda = tk.Label(text="Cotação de 1 moeda especifica", borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

label_selecionarmoeda = tk.Label(text="Selecionar Moeda", anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

label_selecionardata = tk.Label(text="Selecionar o dia que deseja a cotação", anchor='e')
label_selecionardata.grid(row=2, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)





calendario_moeda = DateEntry(year=2021, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

label_textocotacao = tk.Label(text="")
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

botao_pegarcotacao = tk.Button(text="Pegar Cotação", command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

label_cotacamultipas = tk.Label(text="Cotação de Múltiplas moedas", borderwidth=2, relief='solid')
label_cotacamultipas.grid(row=4, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)


label_selecionararquivo = tk.Label(text="Selecionar um arquivo em Execel com as Moedas na culuna A")
label_selecionararquivo .grid(row=5, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)

var_caminhararquivo = tk.StringVar()

botao_selecionararquivo = tk.Button(text="Clique para Selecionar", command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')


label_arquivoselecionado = tk.Label(text="Nenhum Arquivo Selecionado", anchor='e') ### anchor='e' centralizar o texto para o lado esquerdo ENSW
label_arquivoselecionado.grid(row=6, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)


label_datainicial = tk.Label(text="Data Inicial", anchor='e')
label_datafinal = tk.Label(text="Data Final", anchor='e')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky='nsew')
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')


calendario_datainicial = DateEntry(year=2021, locale='pt_br')
calendario_datafinal = DateEntry(year=2021, locale='pt_br')
calendario_datainicial.grid(row=7, column=1, padx=10, pady=10, sticky='nsew')
calendario_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='nsew')

botao_atualizarcotacoes = tk.Button(text="Atualizar Cotacoes", command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nsew')

label_atualizarcotacoes = tk.Label(text="")
label_atualizarcotacoes.grid(row=9, column=1, padx=10, pady=10, sticky='nsew', columnspan=2)


botao_fechar = tk.Button(text="Fechar", command=fechar)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nsew')


janela.mainloop()