from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get("https://www.google.com")
# Para manter o navegador aberto, use:
input("Pressione Enter para fechar o navegador...")
navegador.quit()