
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


def test_reg_page(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Анастасия')
    time.sleep(4)


    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Нагаева')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)
    choose_region_Mari_El = driver.find_element(By.XPATH,"//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)


    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('asya_yepifanova@mail.ru')
    time.sleep(4)


    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH,'//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)


    driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"



def test_reg_page_two_letters(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Яo') #Проверяем возможность заполнения поля двумя символами
    time.sleep(4)


    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Тала')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH,"//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)


    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga@gmail.com')
    time.sleep(4)


    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('043813FzZsWMy')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH,'//*[@id="password-confirm"]')
    confirm_password.send_keys('043813FzZsWMy')

    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(9)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


def test_reg_page_thirty_letters(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Зоязоязоязоязоязоязоязоязоязоя')  # Проверяем возможность заполнения поля тридцатью символами
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Тала')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taiga@gmail.com')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('043813FzZsWMy')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('043813FzZsWMy')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(9)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"



def test_reg_page_hyphen(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Яна')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Чио-Сан') #Проверяем возможность заполнения поля с использованием дефиса
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taiga@yandex.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('043813FzZsWMy')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('043813FzZsWMy')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(9)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"
