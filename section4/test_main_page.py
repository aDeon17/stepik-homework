from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators
from selenium import webdriver
import time


def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.URL_SITE
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина


def test_guest_should_see_login_link(browser):
    link = MainPageLocators.URL_SITE
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def main():
    try:
        driver = webdriver.Chrome()
        test_guest_can_go_to_login_page(driver)
        # test_guest_should_see_login_link(driver)

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        driver.quit()


if __name__ == "__main__":
    main()
