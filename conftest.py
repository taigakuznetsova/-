import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=0bed2c04-ae5f-49f4-9e7e-d6b5a80ebcb0&theme&auth_type')
    driver.maximize_window()
    yield driver

    driver.quit()
