# КЛАСС СТРАНИЦЫ

from selenium.common.exceptions import NoSuchElementException # Импортируем исключение NoSuchElementException
from pages.base_page import BasePage # Импортируем класс BasePage

class SwagLabs(BasePage): # Создаём класс SwagLabs, наследуемый от класса BasePage

    def exist_icon(self): # вызывает метод find_element родительского класса и передает в него локатор
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException: # Исключение ошибки NoSuchElementException (когда элемент не найден)
            return False # Возвращаем False, в случае её появления
        return True # иначе возвращаем True

    def exist_name(self):
        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True

    def exist_pass(self):
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True