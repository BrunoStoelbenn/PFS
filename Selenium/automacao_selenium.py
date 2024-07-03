from selenium import webdriver  #  importar a biblioteca webdrive do selenium
from webdriver_manager.chrome import ChromeDriverManager #   importar o gerenciador automático do google chrome ChromeDriverManager do webdriver_manager.chrome
from selenium.webdriver.chrome.service import Service  #  Vai executar o ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())  #  Identificar a versão atual do google chrome e instalar o chromedriver correspondente à essa versão

navegador = webdriver.Chrome(service=service, options=chrome_options)  #  Passo o servico como parâmetro para a minha variável navegador porque assim vai ser acessado o chromedriver correspondente a versão do meu navegador

# Passo 1: Entrar no link da página
navegador.get("https://lp.hashtagtreinamentos.com/esperapythonimpressionador?origemurl=hashtag_yt_org_listaesperapython_8AMNaVt0z_M")  #  navegador.get vai direcionar você para o link da página passada como parâmetro

# Passo 2: Preencher nome, preencher e-mail
navegador.find_element('xpath', '//*[@id="botaoPopup1"]/div[1]').click();  #  Comando para encontrar um elemento por meio do seu xpath. Entre as outras aspas simples eu passo qual é o elemento que eu quero encontrar por meio do xpath. O .click() diz para eu clicar no elemento. O .send_keys("") vai passar o texto que você digitar dentro das aspas.

# Passo 3: Clicar no botão para enviar o formulário

navegador.find_element('xpath', '//*[@id="firstname"]').send_keys("Bruno")
navegador.find_element('xpath', '//*[@id="email"]').send_keys("brunostoelbenn@gmail.com")
navegador.find_element('xpath', '//*[@id="phone"]').send_keys("51 995050424")
navegador.find_element('xpath', '//*[@id="_form_2475_submit"]').click()



