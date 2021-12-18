def atualizar_cotacoes():
    # ler a dataframe de moedas (arquivo excel)
    df = pd.read_excel(var_caminhararquivo.get())
    print(df)
    moedas = df.iloc[:,
             1]  ## pegando todas as linhas, iniciando do index 0 da COLUNAS (arquivo excel) / .iloc[LINHAS, COLUNAS]
    # pegar a data de inicio e data de fim das cotacoes
    data_inicial = calendario_datainicial.get()  ## pegando o que está preenchido na caixa e colocando na variavel
    data_final = calendario_datafinal.get()  ## pegando o que está preenchido na caixa e colocando na variavel

    ano_inicia = data_inicial[-4:]
    mes_inicia = data_inicial[3:5]
    dia_inicia = data_inicial[:2]

    ano_final = data_final[-4:]
    mes_final = data_final[3:5]
    dia_final = data_final[:2]
    print(f"{ano_inicia}{mes_inicia}{dia_inicia} a {ano_final}{mes_final}{dia_final} ")
    # para cada moedas que esta PREENCHIDA no excel
    for moeda in moedas:
        link = f"https://economia.awesomeapi.com.br/{moeda}-BRL/10?start_date={ano_inicia}{mes_inicia}{dia_inicia}&end_date={ano_final}{mes_final}{dia_final}"
        requisicao_moeda = requests.get(link)
        cotacoes = requisicao_moeda.json()
        print(cotacoes)
        print("test")
        print(link)
        # pegar todas as coracoes daquela moeda
        # criar uma coluna
        for cotacao in cotacoes:
            timestamp = int(cotacao[
                                'timestamp'])  ## vem a data em formato de numero, precisa import o datetime para transformar a data
            bid = float(cotacao['bid'])
            data = datetime.fromtimestamp(timestamp)
            print(bid)
            print(data)

    df.loc[df.iloc[:, 0] == moeda, data] = bid  ## Localizar na primeira linha e uma coluna == a moeda, vai ser o BID
df.to_excel("test.xlsx")
label_atualizarcotacoes['text'] = "Arquivo Atualizado com Sucesso"