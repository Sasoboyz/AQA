import time
import os
import allure
from .base_page import BasePage
from .locators import *
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):

    def random_click(self):
        actions = ActionChains(self.browser)
        actions.move_by_offset(100, 100).click().perform()

    def picture_input(self):
        with allure.step("Вставка изображения"):
            current_dir = os.path.abspath(os.path.dirname(__file__))
            file_name = "pic_1.jpg"
            file_path = os.path.join(current_dir, file_name)

            element = self.browser.find_element(*SideBarr.PHOTO_LOAD)
            time.sleep(10)
            element.send_keys(file_path)

    # Авторизация

    def authing(self, log, pas,name):
        with allure.step("Авторизация"):
            logging_id = self.browser.find_element(*AdminLocators.ADMIN_LOG)
            logging_id.clear()
            logging_id.send_keys(log)
            logging_pass = self.browser.find_element(*AdminLocators.ADMIN_PASS)
            logging_pass.clear()
            logging_pass.send_keys(pas)
            button = self.browser.find_element(*AdminLocators.SAVING_BUTTON)
            button.click()
            naming = self.browser.find_element(*AdminLocators.ADMIN_NAME).text
            assert name == naming

        # Выход из авторизации

    def unauthing(self):
        with allure.step("Выход из учетной записи"):
            button = self.browser.find_element(*AdminLocators.BUTTON_UNAUTH)
            button.click()
            assert self.browser.find_element(*AdminLocators.ADMIN_LOG)

    def bad_auth(self, log, pas,name):
        with allure.step("Некорректная авторизация"):
            logging_id = self.browser.find_element(*AdminLocators.ADMIN_LOG)
            logging_id.send_keys(log)
            logging_pass = self.browser.find_element(*AdminLocators.ADMIN_PASS)
            logging_pass.send_keys(log)
            button = self.browser.find_element(*AdminLocators.SAVING_BUTTON)
            button.click()
            time.sleep(1)
            assert self.browser.find_element(*AdminLocators.ERROR)
            # Выход из окна дропбокса

    def taking_letter(self,warning):
        button_1 = self.browser.find_element(*SideBarr.ABITUR_1)
        button_1.click()
        button_2 = self.browser.find_element(*SideBarr.ABITUR_2)
        button_2.click()
        warn = self.browser.find_element(*SideBarr.WARNING_ID).text
        assert warning in warn


    def checkboxes_actual(self):
        with allure.step("Выбор чекбоксов"):
            profile = self.browser.find_element(*SideBarr.PROFILE)
            profile.click()
            profile = self.browser.find_element(*SideBarr.FAST_MENU)
            profile.click()
            profile = self.browser.find_element(*SideBarr.CHECKBOX_1)
            profile.click()
            profile = self.browser.find_element(*SideBarr.CHECKBOX_2)
            profile.click()
            profile = self.browser.find_element(*SideBarr.CHECKBOX_3)
            profile.click()
            profile = self.browser.find_element(*SideBarr.CHECKBOX_4)
            profile.click()
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            button = self.browser.find_element(*SideBarr.SAVE)
            button.click()
            button = self.browser.find_element(*AdminLocators.MAIN_PAGE)
            button.click()
            time.sleep(2)
            assert self.browser.find_elements(*SideBarr.CHECKING_SID)


    def checkboxes_back(self):
        with allure.step("Отмена чекбоксов"):
            profile = self.browser.find_element(*SideBarr.PROFILE)
            profile.click()
            profile = self.browser.find_element(*SideBarr.FAST_MENU)
            profile.click()
            profile = self.browser.find_element(*SideBarr.CHECKBOX_1)
            profile.click()
            profile = self.browser.find_element(*SideBarr.CHECKBOX_2)
            profile.click()
            profile = self.browser.find_element(*SideBarr.CHECKBOX_3)
            profile.click()
            profile = self.browser.find_element(*SideBarr.CHECKBOX_4)
            profile.click()
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            button = self.browser.find_element(*SideBarr.SAVE)
            button.click()
            time.sleep(1)
            button = self.browser.find_element(*AdminLocators.MAIN_PAGE)
            button.click()

