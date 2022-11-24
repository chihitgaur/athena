import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from Locators import *


class Cyberdone():
    def cyber_arc(self):
        driver.find_element(by=By.XPATH,value=cy_email).send_keys('cgaur@empclaims.com')

        time.sleep(2)

        driver.find_element(by=By.XPATH, value=cy_button).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, cy_pass)))
        driver.find_element(by=By.XPATH,value=cy_pass).send_keys("Vibha@321")
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,cy_butpas)))

        driver.find_element(by=By.XPATH, value=cy_butpas).click()
        time.sleep(4)
        driver.find_element(by=By.XPATH,value=cy_yes).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cy_signinbut)))
        driver.find_element(by=By.XPATH,value=cy_signinbut).click()
        time.sleep(2)

        driver.find_element(by=By.XPATH,value=cy_search).send_keys("Meridian Complete")
        time.sleep(2)
        driver.find_element(by=By.XPATH,value=cy_cmpltmeri).click()