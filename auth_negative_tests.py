import time
from selenium.webdriver.common.by import By

def test_unsuccessful_auth_page_no_email(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(5)


    enter_email = driver.find_element(By.XPATH,'//*[@id="username"]')
    enter_email.send_keys('') #Проверяем пустой email
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')


def test_unsuccessful_auth_page_invalid_email(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(5)


    enter_email = driver.find_element(By.XPATH,'//*[@id="username"]')
    enter_email.send_keys('taiga_taiga@gmail.com') #Проверяем неверный email
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')


def test_unsuccessful_auth_page_invalid_pasword(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(5)


    enter_email = driver.find_element(By.XPATH,'//*[@id="username"]')
    enter_email.send_keys('asya_yepifanova@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('04356513FPsM')
    time.sleep(6)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')
