import time
from selenium import webdriver  #  importar a biblioteca webdrive do selenium
from webdriver_manager.chrome import ChromeDriverManager #   importar o gerenciador automático do google chrome ChromeDriverManager do webdriver_manager.chrome
from selenium.webdriver.chrome.service import Service  #  Vai executar o ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())  #  Identificar a versão atual do google chrome e instalar o chromedriver correspondente à essa versão

navegador = webdriver.Chrome(service=service, options=chrome_options)  #  Passo o servico como parâmetro para a minha variável navegador porque assim vai ser acessado o chromedriver correspondente a versão do meu navegador

navegador.get("https://portalvirtual.unisc.br/moodle/login_unisc/")

navegador.find_element('xpath', '//*[@id="logar"]/strong').click()

navegador.find_element('xpath', '//*[@id="loginform-username"]').send_keys("sua_matrícula_virtual_unisc")

navegador.find_element('xpath', '//*[@id="loginform-password"]').send_keys("sua_senha_virtual_unisc")

time.sleep(5) # Pausa a execução por 5 segundos

navegador.find_element('xpath', '//*[@id="login-form"]/div[5]/div[2]/button').click()



