import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as Ops

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                 help="Choose language:ru,en...etc.")


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(10)
    print("\nstarting test..")
    yield browser
    print("\nquit browser..")
    browser.quit()







# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     user_language = request.config.getoption("language")
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         webdriver.Chrome()
#         options = Options()
#         options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#         browser = webdriver.Chrome(options=options)
#         browser.set_window_size(1920, 1080)
#         browser.implicitly_wait(10)
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#         options = Ops()
#         options.set_preference("intl.accept_languages", user_language)
#         webdriver.Firefox(options=options)
#         browser.set_window_size(1920, 1080)
#         browser.implicitly_wait(10)
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()