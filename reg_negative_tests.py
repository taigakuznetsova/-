import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


def test_unsuccessful_email_already_used(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Асия')
    time.sleep(4)


    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('asya_yepifanova@mail.ru') #Повторно регистрируемся с тем же email
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


def test_unsuccessful_enter_your_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('') #Проверяем пустое поле
    time.sleep(4)


    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taiga@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"



def test_unsuccessful_enter_your_second_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Елена')
    time.sleep(4)


    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Brown') #Проверяем латинский алфавит
    time.sleep(4)


    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taiga@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"



def test_unsuccessful_name_one_letter(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('А') #Проверяем невозможность заполнения поля одним символом
    time.sleep(4)


    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taiga@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"



def test_unsuccessful_name_thirty_one_letter(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Зоязоязоязоязоязоязоязоязоязояя') #Проверяем невозможность заполнения поля тридцати одним символом
    time.sleep(4)


    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taiga@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"



def test_unsuccessful_name_numbers(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Зоя1') #Проверяем невозможность заполнения поля цифрами
    time.sleep(4)


    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taiga@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"



def test_unsuccessful_no_email(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Асия')
    time.sleep(4)


    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('') #Проверяем пустой email
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


def test_unsuccessful_email_no_at(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Асия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taigagmail.com')  # Проверяем email без знака @
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"



def test_unsuccessful_email_quotation_marks(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Асия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taiga"gmail.com')  # Проверяем email с кавычками вместо знака @
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


def test_unsuccessful_email_at_the_beginning(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Асия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('@taiga.taigagmail.com')  # Проверяем email со знаком @ в начале
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"




def test_unsuccessful_email_comma(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Асия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga,taiga@gmail.com')  # Проверяем email с запятой вместо точки
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWM')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"




def test_unsuccessful_no_password_confirm(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Асия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taiga@gmail.com')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('') #Нет подтверждения пароля

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"



def test_unsuccessful_different_passwords(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Асия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taiga@gmail.com')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('0438513FzZsWM')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('0438513FzZsWO') #Пароли не совпадают

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


def test_unsuccessful_password_less_than_eight(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Асия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Епифанова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('taiga.taiga@gmail.com')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('04383sW')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('04383sW')  # Пароль из семи символов

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"
