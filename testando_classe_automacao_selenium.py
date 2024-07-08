from website_automator import WebsiteAutomator

navegador = WebsiteAutomator()
navegador.pagina("https://portalvirtual.unisc.br/moodle/login_unisc/")
navegador.clicar('//*[@id="logar"]/strong')
navegador.enviar_escrita('//*[@id="loginform-username"]', "m134231")
navegador.enviar_escrita('//*[@id="loginform-password"]', "")
navegador.atraso(5)
navegador.clicar('//*[@id="login-form"]/div[5]/div[2]/button')