from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
from parsel import Selector

import csv

#Arquivo CSV
writer = csv.writer(open('output.csv','w'))
writer.writerow(['Nome', 'Headline', 'URL'])

#Opcoes para pagina
#options = Options()
#options.add_argument("start-maximized")

#Carregar Driver
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Chrome('./chromedriver')

#Acessar a pagina
driver.get('https://linkedin.com/')
sleep(1)

#Acessar Login
driver.find_element_by_css_selector('a.nav__button-secondary').click()
sleep(3)

#Preencher usuario
usuario_input = driver.find_element_by_name('session_key')
usuario_input.send_keys('rodrigo.reis12@gmail.com')

#Preencher senha (####### seu senha)
senha_input = driver.find_element_by_name('session_password')
senha_input.send_keys('########')

#Enter para o Login
senha_input.send_keys(Keys.RETURN)
sleep(3)

#Acessar o Google
driver.get("https://www.google.com")
sleep(1)


#Preencher busca
busca_input = driver.find_element_by_name('q')
busca_input.send_keys('site:linkedin.com/in AND "Data Science" AND "Sāo Paulo"')
busca_input.send_keys(Keys.RETURN)
sleep(2)

#Busca todos os links
lista_perfil = driver.find_elements_by_xpath('//div[@class="yuRUbf"]/a')
lista_perfil = [perfil.get_attribute('href') for perfil in lista_perfil]

#Extrair informacoes individuais
for perfil in lista_perfil:
    driver.get(perfil)
    sleep(4)

    response = Selector(text=driver.page_source)
    nome = response.xpath('//title/text()').extract_first().split(" | ")[0]
    headline = response.xpath('//h2/text()')[1].extract().split()[0]
    url_perfil = driver.current_url

    #Gravar no CSV
    writer.writerow([nome, headline, url_perfil])

driver.quit()







