# БАЗОВЫЙ КЛАСС

from selenium.webdriver.common.by import By # Импортируем метод By

class BasePage: # Создаём класс

    def __init__(self, driver): # инициализируем с атрибутом driver, принимающим аргументы
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/' # аргумент выставлен по умолчанию

    def visit(self):  # метод посещения страницы
        return self.driver.get(self.base_url)  # возвращает переход на страницу по принятому URL


    def find_element(self, locator): # Метод поиска элемента. Принимает локатор
        return self.driver.find_element(By.CSS_SELECTOR, locator) # Возвращает результат обращение к поиску локатора через драйвер.