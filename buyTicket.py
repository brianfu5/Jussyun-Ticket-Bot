from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config

MY_EMAIL = config.MY_EMAIL
MY_PASSWORD = config.MY_PASSWORD

def login(driver):
    """
    This function uses the above MY_EMAIL and MY_PASSWORD fields to log in to your account.
    """
    clickButton("//*[@id='app']/div[1]/div/div[2]/div", driver)
    fillField("//*[@id='app']/div[1]/div/div[1]/div/div/div[1]/div/div[1]/input", MY_EMAIL, driver)
    fillField("//*[@id='app']/div[1]/div/div[1]/div/div/div[2]/div/div[1]/input", MY_PASSWORD, driver)
    clickButton("//*[@id='app']/div[1]/div/div[1]/div/div/div[5]/div/div[1]/div[1]/div/span", driver)
    clickButton("//*[@id='app']/div[1]/div/div[1]/div/div/div[3]", driver)

def clickButton(xpath, driver):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    button.click()

def fillField(xpath, input, driver):
    field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath)))
    field.send_keys(input)

def buyTicket():
    """
    This function combines all the steps to instantly get you in the seat selection phase.
    Here, you can select your own seat, submit the order, 
    complete the CAPTCHA(I couldn't figure out how to automate this) and pay. 
    """

    chromedriver_path = config.chromedriver_path
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

    driver.get(config.event)
    time.sleep(1)

    try:
        login(driver)
        print("Finished Login")
        time.sleep(1)

        clickButton("//*[@id='app']/section/div/div[2]/div[1]/div[2]/div[5]/div/div[1]", driver)
        clickButton("//*[@id='app']/section/div/div[2]/div[1]/div[2]/div[8]/span", driver)
        clickButton("//*[@id='app']/section/div[2]/div/div[2]/div[2]/div/div/span", driver)
        #clickButton("//*[@id='app']/section/div[2]/div/div[8]/div[2]", driver)
    finally:
        print("User should complete from here")
        

if __name__ == "__main__":
    print("Loading")