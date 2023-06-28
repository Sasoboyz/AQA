from selenium.webdriver.common.by import By

class AdminLocators():
    ADMIN_LOG = (By.ID, "loginform-username")
    ADMIN_PASS = (By.ID, "loginform-password")
    SAVING_BUTTON = (By.CLASS_NAME, "styled-button.styled-button--red.styled-button--solid.styled-button--w100")
    BUTTON_UNAUTH = (By.CLASS_NAME, 'logout__text')
    MAIN_PAGE = (By.CLASS_NAME, 'toggle-menu')
    ADMIN_NAME = (By.CLASS_NAME, 'current-user__name')
    ERROR = (By.CLASS_NAME, 'help-block.help-block-error')

class SideBarr():
    PROFILE = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]')
    PHOTO_LOAD = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/div[1]/form/div[1]/div[1]/div[2]/input')
    ABITUR_1 = (By.CLASS_NAME, 'main-menu__item-name')
    ABITUR_2 = (By.CLASS_NAME, 'main-menu-dropdown__link')
    WARNING_ID = (By.ID, 'w0-warning-0')
    # SCIENCE = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[11]/a/span')
    FAST_MENU = (By.ID, 'fast-menu-tab')
    CHECKBOX_1 = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/div[3]/form/div[1]/div/table/tbody/tr[1]/td[1]/input[4]')
    CHECKBOX_2 = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/div[3]/form/div[1]/div/table/tbody/tr[6]/td[1]/input[4]')
    CHECKBOX_3 = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/div[3]/form/div[1]/div/table/tbody/tr[16]/td[1]/input[4]')
    CHECKBOX_4 = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/div[3]/form/div[1]/div/table/tbody/tr[22]/td[1]/input[4]')
    CHECKING_SIDE = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[19]/a/span')
    SAVE = (By.CSS_SELECTOR, '#w3 > div.form-sumb > button')

