from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from password import *

driver = webdriver.Chrome("C:\Chromedriver\chromedriver")

URL = "https://tinder.com/"

driver.get(URL)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a").click()

main_page = driver.current_window_handle
print(main_page)
print(driver.title)

time.sleep(1)
driver.find_element_by_xpath("//button[@aria-label='Zaloguj się przez Facebooka']").click()
time.sleep(5)

# changing the handles to access login page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

# change the control to signin page
driver.switch_to.window(login_page)

driver.find_element_by_xpath("//button[@title='Akceptuj wszystkie']").click()
time.sleep(1)

driver.find_element_by_xpath("//input[@type='text']").send_keys(FACEBOOK_EMAIL)
driver.find_element_by_xpath("//input[@type='password']").send_keys(FACEBOOK_PASSWORD, Keys.ENTER)

driver.switch_to.window(main_page)
time.sleep(6)
driver.find_element_by_xpath("//button[@data-testid='allow']").click()
time.sleep(1)
driver.find_element_by_xpath("//button[@data-testid='allow']").click()

page = driver.find_element_by_tag_name('body')
for _ in range(100):

    page.send_keys(Keys.ARROW_RIGHT)
    time.sleep(3)

    try:
        driver.find_element_by_xpath("//button[@title='Wróć do Tindera']").click()
    except NoSuchElementException:
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/button[2]").click()
        except NoSuchElementException:
            continue



