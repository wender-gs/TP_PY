import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

print("Iniciando serviços...")

table = pd.read_excel('tp_data.xlsx', sheet_name=0)

df = pd.DataFrame(table)

v = df['v']

with open('./db/dados.txt') as file:
    try:
        d = int(file.read())
    except Exception as e:
        d = int(0)
        print(e)

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

print("instanciando o browser...")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

print("Inserindo registros se disponiveis...")

for i in v:  # variavel i retorna os valores contidos na coluna v

    while i > d:
        with open("dados.txt", "r") as arquivo:
            ac: str = arquivo.read()

        # entrando na página de cadastro
        driver.get("http://localhost:8000/usuarios/create")

        # recuperando o input do username e adicionando o valor a ele
        username = driver.find_element('xpath', '//*[@id="name"]')
        username.send_keys(df.loc[d]['username'])

        # recuperando o input do email e adicionando o valor a ele
        email = driver.find_element('xpath', '//*[@id="email"]')
        email.send_keys(df.loc[d]['email'])

        # recuperando o input do password e adicionando o valor a ele
        password = driver.find_element('xpath', '//*[@id="pass"]')
        password.send_keys(str(df.loc[d]['password']))

        # clicando no botão de cadastro
        driver.find_element('xpath', '/html/body/section/div[2]/form/button').click()

        with open("dados.txt", 'w') as arquivo:
            arquivo.write(str(i))

        d += 1

driver.quit()

print("atualização concluida!")
