from selenium import webdriver
from selenium.webdriver.common.by import By

#instanciando o navegador
navegador = webdriver.Chrome()
#usando o método get para acessar a página 
navegador.get("https://pt-br.facebook.com/login/device-based/regular/login/")

#localizando o campo de email pelo name
campo_nome = navegador.find_element(By.NAME, "email")
#preenchendo o campo de email
campo_nome.send_keys("email@email.com")

#localizando o campo de senha pelo name
campo_email = navegador.find_element(By.NAME, "pass")
#preenchendo o campo senha
campo_email.send_keys("123456")

#localizando o botão de login pelo name
botao_login = navegador.find_element(By.NAME, "login")
#clique no botão de login
botao_login.click()

#para manter o navegador aberto
input("Pressione Enter para fechar o navegador...")
navegador.quit()






