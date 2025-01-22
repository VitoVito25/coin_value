# Importa as funções necessárias
from functions import start_browser, fetch_coin_data, append_to_excel

# Dicionário com nomes das moedas e suas URLs
coin_mapping = {
    "BTC": "https://coinmarketcap.com/currencies/bitcoin/",
    "ETH": "https://coinmarketcap.com/currencies/ethereum/",
    "SOL": "https://coinmarketcap.com/currencies/solana/",
    "LINK": "https://coinmarketcap.com/currencies/chainlink/",
    "RAY": "https://coinmarketcap.com/currencies/raydium/",
    "RNDR": "https://coinmarketcap.com/currencies/render/",
    "NEAR": "https://coinmarketcap.com/currencies/near-protocol/",
    "HNT": "https://coinmarketcap.com/currencies/helium/",
    "PENDLE": "https://coinmarketcap.com/currencies/pendle/",
    "LDO": "https://coinmarketcap.com/currencies/lido-dao/",
    "OP": "https://coinmarketcap.com/currencies/optimism/",
    "RON": "https://coinmarketcap.com/currencies/ronin/",
    "STX": "https://coinmarketcap.com/currencies/stacks/",
    "WIF": "https://coinmarketcap.com/currencies/dogwifhat/",
    "IMX": "https://coinmarketcap.com/currencies/immutablex/",
    "DRIFT": "https://coinmarketcap.com/currencies/drift/",
    "ENA": "https://coinmarketcap.com/currencies/ethena/",
    "JUP": "https://coinmarketcap.com/currencies/jupiter/",
    "ARB": "https://coinmarketcap.com/currencies/arbitrum/",
    "MATIC": "https://coinmarketcap.com/currencies/polygon/",
    "DOGE": "https://coinmarketcap.com/currencies/dogecoin/",
    "PYTH": "https://coinmarketcap.com/currencies/pyth-network/",
    "GALA": "https://coinmarketcap.com/currencies/gala/",
    "SUWI": "https://coinmarketcap.com/currencies/suwi/",
    "SHIBA": "https://coinmarketcap.com/currencies/shiba-inu/",
    "PEPE": "https://coinmarketcap.com/currencies/pepe/"
}

print('Iniciando busca...')

# Inicia o navegador
browser = start_browser()

# Busca os dados
results = fetch_coin_data(browser, coin_mapping)
print('Compilando dados...')

# Fecha o navegador
browser.quit()

# Adiciona os dados na planilha "data" do arquivo "coin_data.xlsx"
append_to_excel(results, file_path="coin_data.xlsx", sheet_name="data")

# Exibe os resultados
print(results)
