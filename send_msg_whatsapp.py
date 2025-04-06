from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o navegador e abre o WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

# Pausa para escanear o código QR manualmente
time.sleep(15)

def send_message(contact, message):
    # Procura o campo de busca e procura o contato
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(contact)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)
    time.sleep(1)
    
    # Envia a mensagem
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

# Exemplo de uso
contact_name = "Nome do Contato"
auto_reply_message = "Olá, esta é uma mensagem automática."
send_message(contact_name, auto_reply_message)

# Fecha o navegador após 10 segundos
time.sleep(10)
driver.quit()
