from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o WebDriver (por exemplo, para o Chrome)
driver = webdriver.Chrome()

# --- ABRIR O TEAMS ---
driver.get("https://teams.microsoft.com")
# Aguarda o carregamento e/ou login manual
time.sleep(20)  # Ajuste esse tempo conforme necessário

# --- ABRIR O CHATGPT EM UMA NOVA ABA ---
driver.execute_script("window.open('');")
# Acessa a nova aba (índice 1)
driver.switch_to.window(driver.window_handles[1])
driver.get("https://chat.openai.com/")
# Aguarda o login ou carregamento
time.sleep(20)  # Ajuste conforme necessário

def monitorar_mensagens_teams():
    """
    Função que verifica se há novas mensagens no Teams.
    OBS: Os seletores abaixo são fictícios. Será necessário inspecionar a página do Teams
         e identificar os elementos que representam novas mensagens.
    """
    # Volta para a aba do Teams
    driver.switch_to.window(driver.window_handles[0])
    try:
        # Exemplo: encontra elementos que representem mensagens não respondidas
        novas_msgs = driver.find_elements(By.CLASS_NAME, "classe-da-mensagem-nova")
        for msg in novas_msgs:
            texto_msg = msg.text
            print("Mensagem recebida:", texto_msg)
            resposta = obter_resposta_chatgpt(texto_msg)
            resposta_formatada = formatar_resposta(resposta)
            enviar_resposta_teams(resposta_formatada)
            # Aqui você pode implementar lógica para marcar a mensagem como já processada
    except Exception as e:
        print("Erro ao monitorar mensagens:", e)

def obter_resposta_chatgpt(mensagem):
    """
    Envia a mensagem para o ChatGPT e aguarda a resposta.
    """
    # Troca para a aba do ChatGPT
    driver.switch_to.window(driver.window_handles[1])
    try:
        # Localiza a caixa de entrada (o seletor exato deve ser verificado)
        textarea = driver.find_element(By.TAG_NAME, "textarea")
        textarea.clear()
        textarea.send_keys(mensagem)
        textarea.send_keys(Keys.ENTER)
        
        # Aguarda o ChatGPT gerar a resposta (tempo pode variar)
        time.sleep(10)
        
        # Captura a resposta. É necessário inspecionar a estrutura da resposta do ChatGPT.
        resposta_elemento = driver.find_element(By.CSS_SELECTOR, "div.resposta-classe")
        resposta_texto = resposta_elemento.text
        print("Resposta do ChatGPT:", resposta_texto)
        return resposta_texto
    except Exception as e:
        print("Erro ao obter resposta do ChatGPT:", e)
        return ""

def formatar_resposta(resposta):
    """
    Processa a resposta para extrair apenas a parte direcionada à pessoa,
    removendo eventuais informações padrão que possam indicar automatismo.
    Essa lógica dependerá do formato da resposta gerada.
    """
    # Exemplo simples: remove linhas que comecem com um padrão específico
    linhas = resposta.split("\n")
    linhas_filtradas = [linha for linha in linhas if not linha.startswith("Como assistente")]
    resposta_formatada = "\n".join(linhas_filtradas)
    return resposta_formatada

def enviar_resposta_teams(resposta):
    """
    Envia a resposta formatada de volta para o chat do Teams.
    """
    # Volta para a aba do Teams
    driver.switch_to.window(driver.window_handles[0])
    try:
        # Encontra a caixa de mensagem do Teams (o seletor exato deve ser ajustado)
        chat_input = driver.find_element(By.XPATH, "//input[@type='text']")
        chat_input.clear()
        chat_input.send_keys(resposta)
        chat_input.send_keys(Keys.ENTER)
        print("Resposta enviada ao Teams.")
    except Exception as e:
        print("Erro ao enviar resposta para o Teams:", e)

# Loop principal para monitorar mensagens periodicamente
while True:
    monitorar_mensagens_teams()
    time.sleep(5)  # Verifica a cada 5 segundos (ajuste conforme necessário)

