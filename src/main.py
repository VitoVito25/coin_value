# Importa as funções
from functions import start_browser, fetch_coin_data

# Lista de URLs das moedas
urls = [
    "https://coinmarketcap.com/currencies/bitcoin/",
    "https://coinmarketcap.com/currencies/ethereum/",
]

# Inicia o navegador
browser = start_browser()

# Dicionário para armazenar os resultados
coin_mapping = {}

# Busca os dados para cada URL
for url in urls:
    name, value = fetch_coin_data(browser, url)
    if name and value:
        coin_mapping[name] = value

# Fecha o navegador
browser.quit()

# Exibe o resultado
print(coin_mapping)
