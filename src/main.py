# Importa as funções necessárias
from functions import start_browser, fetch_coin_data

# Dicionário com nomes das moedas e suas URLs
coin_mapping = {
    "BTC": "https://coinmarketcap.com/currencies/bitcoin/",
    "ETH": "https://coinmarketcap.com/currencies/ethereum/",
}

# Inicia o navegador
browser = start_browser()

# Busca os dados
results = fetch_coin_data(browser, coin_mapping)
print('Compilando dados...')

# Fecha o navegador
browser.quit()

# Exibe os resultados
print(results)
