#Importar as Bibliotecas
from selenium import webdriver
    #WebDriver serve para simular o uso do Navegador, atráves da Navegação WEB.
import time
from webdriver_manager.chrome import ChromeDriverManager
    #Simular o Uso do Navegador.
from selenium.webdriver.common.keys import Keys
from webdriver_manager.driver import ChromeDriver


#Navegar até o WhatsApp Web
driver = webdriver.Chrome((ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com/')
time.sleep(10)

#Definir Contatos e Grupos e Mensagems.
contatos = ['CEG 61 Quinta-Feira 22h']
mensagem = 'BID OPEN - CEG QUINTA-FEIRA 22:'
mensagem1 = '1. Ruan'
mensagem2 = '2. '
mensagem3 = '3. '
mensagem4 = '4. '
mensagem5 = '5. '
mensagem6 = '6. '
mensagem7 = '7. '
mensagem8 = '8. '
mensagem9 = '9. '
mensagem10 = '10. '
mensagem11 = '11. '
mensagem12 = '12. '


#Buscar Contatos/Grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem,mensagem1,mensagem2,mensagem3,mensagem4,mensagem5,mensagem6,mensagem7,mensagem8,mensagem9,mensagem10,mensagem11,mensagem12):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem1)
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem2)
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem3)   
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem4)   
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem5)   
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem6)   
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem7)   
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem8)   
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem9)   
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem10)   
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem11)   
    campo_mensagem[1].send_keys(Keys.CONTROL, Keys.ENTER)
    campo_mensagem[1].send_keys(mensagem12)       
    campo_mensagem[1].send_keys(Keys.ENTER)


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem,mensagem1,mensagem2,mensagem3,mensagem4,mensagem5,mensagem6,mensagem7,mensagem8,mensagem9,mensagem10,mensagem11,mensagem12)
