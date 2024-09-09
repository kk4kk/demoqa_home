# ТЕСТ

from pages.swag_labs import SwagLabs # Импортируем класс

def test_check_icon(browser):
    saucedemo = SwagLabs(browser)  # Создаем объект класса SwagLabs, передаём в него драйвер (browser)
    saucedemo.visit()  # посещаем страницу
    assert saucedemo.exist_icon()  # проверка наличия элемента на странице

def test_check_name(browser):
    saucedemo = SwagLabs(browser)
    saucedemo.visit()
    assert saucedemo.exist_name()

def test_check_pass(browser):
    saucedemo = SwagLabs(browser)
    saucedemo.visit()
    assert saucedemo.exist_pass()