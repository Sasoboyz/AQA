import allure
from .pages.main_page import MainPage
from .pages.links import LINKS,DATAPASS



allure.description("Корректная авторизация")
def test_correct_cuth(browser):  # Проверка авторизации всех пользователей
    link = LINKS.ADMIN_LINK
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.authing(DATAPASS.ADMIN_LOG, DATAPASS.ADMIN_PASS,DATAPASS.ADMIN_NAME)

def test_bad_auth(browser):
    link = LINKS.ADMIN_LINK
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.bad_auth(DATAPASS.ADMIN_LOG, DATAPASS.ADMIN_PASS, DATAPASS.ADMIN_NAME)

def test_unauth(browser):
    link = LINKS.ADMIN_LINK
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.authing(DATAPASS.ADMIN_LOG, DATAPASS.ADMIN_PASS,DATAPASS.ADMIN_NAME)
    page.unauthing()

def test_correct_auth_after_bad(browser):
    link = LINKS.ADMIN_LINK
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.bad_auth(DATAPASS.ADMIN_LOG, DATAPASS.ADMIN_PASS, DATAPASS.ADMIN_NAME)
    page.authing(DATAPASS.ADMIN_LOG, DATAPASS.ADMIN_PASS,DATAPASS.ADMIN_NAME)
    page.unauthing()

def test_letter_checking(browser):
    link = LINKS.ADMIN_LINK
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.authing(DATAPASS.ADMIN_LOG, DATAPASS.ADMIN_PASS,DATAPASS.ADMIN_NAME)
    page.taking_letter(DATAPASS.WARNING)

def test_checkbox(browser):
    link = LINKS.ADMIN_LINK
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.authing(DATAPASS.ADMIN_LOG, DATAPASS.ADMIN_PASS,DATAPASS.ADMIN_NAME)
    page.checkboxes_actual()
    page.checkboxes_back()

def test_all_functions(browser):
    link = LINKS.ADMIN_LINK
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.bad_auth(DATAPASS.ADMIN_LOG, DATAPASS.ADMIN_PASS, DATAPASS.ADMIN_NAME)
    page.authing(DATAPASS.ADMIN_LOG, DATAPASS.ADMIN_PASS,DATAPASS.ADMIN_NAME)
    page.taking_letter(DATAPASS.WARNING)
    page.checkboxes_actual()
    page.checkboxes_back()
    page.unauthing()