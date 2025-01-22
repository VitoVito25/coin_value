from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Variável global para armazenar a instância do navegador
browser = None

def start_browser():
    """
    Função para iniciar o navegador.
    :return: Instância do navegador.
    """
    global browser  # Utiliza a variável global 'browser'

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    return browser

def fetch_coin_data(browser, coin_mapping):
    """
    Função para buscar dados de moedas a partir de um mapeamento de URLs.
    :param browser: Instância do navegador.
    :param coin_mapping: Dicionário com nomes das moedas como chaves e URLs como valores.
    :return: Dicionário com nomes das moedas como chaves e seus valores como valores.
    """
    results = {}
    search_index = 1  
    search_length = len(coin_mapping)

    for name, url in coin_mapping.items():
        try:
            print(f"Pesquisando {name}... ({search_index}/{search_length})")
            search_index += 1

            browser.get(url)
            
            # Aguarda até que o valor esteja visível na página (Timeout em 10 segundos)
            wait = WebDriverWait(browser, 10)
            value_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-coin-overview"]/div[2]/span')))
            
            # Obtém o valor da moeda
            coin_value = value_element.text.strip()
            
            # Armazena o resultado no dicionário
            results[name] = coin_value
        
        except TimeoutException as e:
            print(f"Erro ao processar {name}: Tempo de carregamento excedido - {e}")
        except NoSuchElementException as e:
            print(f"Erro ao processar {name}: Elemento não encontrado - {e}")
    
    return results

