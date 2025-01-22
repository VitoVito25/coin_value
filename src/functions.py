from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time  # Importação correta para time.sleep()

# Variável global para armazenar a instância do navegador
browser = None

def start_browser():
    """
    Função para iniciar o navegador.
    :return: Instância do navegador.
    """
    global browser  # Utiliza a variável global 'browser'
    
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)  # Inicia o ChromeDriver sem opções headless por padrão
    return browser

def fetch_coin_data(browser, url):
    """
    Função para buscar dados de uma moeda em uma URL específica.
    :param browser: Instância do navegador.
    :param url: URL da página da moeda.
    :return: Nome e valor da moeda.
    """
    try:
        browser.get(url)
        time.sleep(3)  # Aguarda o carregamento da página
        
        # Localizar elementos na página
        name_element = browser.find_element(By.XPATH, '//*[@id="section-coin-overview"]/div[1]/h1/div[1]/span')
        value_element = browser.find_element(By.XPATH, '//*[@id="section-coin-overview"]/div[2]/span')
        
        name = name_element.text.strip()
        value = value_element.text.strip()
        
        return name, value
    except NoSuchElementException as e:
        print(f"Erro ao processar {url}: Elemento não encontrado - {e}")
        return None, None
