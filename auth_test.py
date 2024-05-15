import time
from selenium.webdriver.common.by import By

def test_auth_page(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(5)


    enter_email = driver.find_element(By.XPATH,'//*[@id="username"]')
    enter_email.send_keys('asya_yepifanova@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')


def test_forgotten_your_password(driver):
    driver.find_element(By.XPATH, '//*[@id="forgot_password"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(3)
    enter_email = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_email.send_keys('asya_yepifanova@mail.ru')
    time.sleep(25)

    auth = driver.find_element(By.XPATH, '//*[@id="reset"]')
    auth.click()
    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]')
