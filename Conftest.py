import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language=request.config.getoption("language")
    options = Options()
    options.add_argument(f"--lang={language}")
    browser = webdriver.Chrome(options=options)
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    yield browser
    browser.quit()

class TestLogin:
    def test_guest_should_see_login_link(self, browser):
        browser.find_element(By.CSS_SELECTOR, "#login_link")
