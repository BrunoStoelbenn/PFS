import time
from selenium import webdriver  #  importar a biblioteca webdrive do selenium
from webdriver_manager.chrome import ChromeDriverManager #   importar o gerenciador automático do google chrome ChromeDriverManager do webdriver_manager.chrome
from selenium.webdriver.chrome.service import Service  #  Vai executar o ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class WebsiteAutomator:
    def __init__(self):
        self.setup_browser()
    
    def setup_browser(self):
        #  Configura o navegador chrome com as opções necessárias
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service, options=chrome_options)

    def pagina(self, url):
        self.browser.get(url)

    def clicar(self, xpathId):
        self.browser.find_element('xpath', xpathId).click()

    def enviar_escrita(self, xpathId, texto):
        self.browser.find_element('xpath', xpathId).send_keys(texto)

    def atraso(self, tempo):  #  Função para gerar um atraso passando um tempo em segundos como parâmetro para dar tempo de carregar algum elemento html para depois clicar ou enviar um texto.
        time.sleep(tempo)