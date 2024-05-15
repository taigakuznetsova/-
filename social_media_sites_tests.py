import time
from selenium.webdriver.common.by import By

def test_vk_page(driver):
    driver.find_element(By.XPATH, '//*[@id="oidc_vk"]').click()
    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]') #Проверяем переход по ссылке на быстрый вход в vk по  qr-коду


def test_mail_page(driver):
    driver.find_element(By.XPATH, '//*[@id="oidc_mail"]').click()
    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="wrp"]') #Проверяем переход по ссылке на вход в @мой мир
