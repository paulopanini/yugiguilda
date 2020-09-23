from selenium import webdriver


def after_scenario(context, tag):
    context.webdriver.quit()
