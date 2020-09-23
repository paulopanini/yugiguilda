from behave import given, when, then
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
from dotenv import load_dotenv

load_dotenv()

@given(u'o navegador "{navegador}"')
def step_impl(context, navegador):
    if navegador == "Chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.headless = False
        context.webdriver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    if navegador == "Firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        options.headless = False
        context.webdriver = webdriver.Firefox(GeckoDriverManager().install())

@given(u'a tela de login do vhsys')
def step_impl(context):
    context.webdriver.get("https://app.vhsys.com.br")

@when(u'clicado no botão entrar')
def step_impl(context):
    element = context.webdriver.find_element(By.ID, "btnLogar")
    element.click()
    time.sleep(3)

@then(u'deve apresentar a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    element = context.webdriver.find_element(By.ID, "resultadoLogar")
    assert(element.text == mensagem)

@given(u'o campo "{campo}" é preenchido com o valor "{valor_campo}"')
def step_impl(context, campo, valor_campo):
    element = context.webdriver.find_element(By.ID, campo)
    element.send_keys(valor_campo)

@then(u'deve apresentar o elemento "{elemento}" com o atributo "{atributo}" contendo o valor "{valor}"')
def step_impl(context, elemento, atributo, valor):
    element = context.webdriver.find_element(By.ID, elemento)
    assert(element.get_attribute(atributo) == valor)

@given(u'o usuário está logado no sistema')
def step_impl(context):
    context.webdriver.get(os.getenv('url'))
    element = context.webdriver.find_element(By.ID, 'login')
    element.send_keys(os.getenv('user'))
    element = context.webdriver.find_element(By.ID, 'senha')
    element.send_keys(os.getenv('password'))
    element = context.webdriver.find_element(By.ID, os.getenv('btn_logar'))
    element.click()
    time.sleep(5)