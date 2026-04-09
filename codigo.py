# Pyautogui -> fazer automações com python
    # Clicar em algum lugar -> pyautogui.click
    # Pressionar uma tecla -> pyautogui.press
    # Escrever um texto -> pyautogui.write
    # Combinação de tecla -> pyautogui.hotkey 
import pyautogui as py


# Entrar no sistema da empresa -> https://dlp.hashtagtreinamentos.com/python/intensivao/login
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    # Abrir o navegador
py.press("win")
py.write("chrome")
py.press("enter")
    # Delay
import time
time.sleep(0.5)
    # Maximizar
py.hotkey("win", "up")
time.sleep(0.1)
    # Digitar o site
py.write(site)
py.press("enter")
    # Delay
time.sleep(3)


# Fazer login
    # Digitar email
py.click(x=575, y=407)
py.write("Yang")
    # Digitar senha
py.click(x=551, y=506)
py.write("123")
    # Entrar
py.click(x=816, y=577)
    # Delay de 3seg
time.sleep(3)


# Importar a base de dados
import pandas as pd
dados = pd.read_csv("produtos.csv")
print(dados)


# Cadastrar um produto
    # Repetir para todos os produtos
for linha in dados.index:

    py.click(x=582, y=295)

    codigo = dados.loc[linha, "codigo"]
    py.write(codigo)
    py.press("tab")

    marca = dados.loc[linha, "marca"]
    py.write(marca)
    py.press("tab")

    tipo = dados.loc[linha, "tipo"]
    py.write(tipo)
    py.press("tab")

    categoria = str(dados.loc[linha, "categoria"])
    py.write(categoria)
    py.press("tab")

    preco_unitario = str(dados.loc[linha, "preco_unitario"])
    py.write(preco_unitario)
    py.press("tab")

    custo = str(dados.loc[linha, "custo"])
    py.write(custo)
    py.press("tab")

    obs = (dados.loc[linha, "obs"])
    if pd.notna(obs):
        py.write(str(obs))

    py.press("enter")
    py.scroll(1000)
    py.click(x=582, y=295)
