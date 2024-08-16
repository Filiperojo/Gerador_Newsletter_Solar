
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def coleta_resumo(flag):
  OpenAI.api_key = 'API_KEY'
  chrome_options = Options()
  chrome_options.add_argument("--headless")  
  chrome_options.add_argument("--disable-gpu")  
  client = OpenAI()
  navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
  navegador.get("https://canalsolar.com.br/")
  time.sleep(2)

  action = ActionChains(navegador)
  for i in range(flag):
      action.key_down(Keys.TAB).perform()
  action.key_down(Keys.ENTER).perform()
  time.sleep(1)
  current_url = navegador.current_url

  response = requests.get(current_url)
  soup = BeautifulSoup(response.content, "html.parser")
  text = soup.get_text()
  time.sleep(1)


  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Resuma o seguinte texto para uma newsletter "},
      {"role": "user", "content": text}
    ]
  )

  
  completion = completion.choices[0].message.content
  texto_formatado = completion.encode('utf-8').decode('utf-8')

  titulo = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Dê um titulo obrigatoriamente limitado a 50 caracteres para a seguinte Newsletter "},
      {"role": "user", "content": texto_formatado}
    ]
  )

  titulo = titulo.choices[0].message.content
  titulo_formatado = titulo.encode('utf-8').decode('utf-8')



  print(titulo_formatado)
  print(texto_formatado)

  return(titulo_formatado, texto_formatado, current_url)


