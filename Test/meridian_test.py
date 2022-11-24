import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
from Cyberark.cyberark import Cyberdone
from Locators import *
from Switching import switching
from Writing.Excel_part import picking_data


class Testmeridian():

    @pytest.mark.usefixtures("initiate_driver")
    def test_end_to_end(self, initiate_driver):
        data3 = pd.read_excel(r"C:\\Users\\chihi\\Desktop\\Claim status meridian\\ARclaim.xlsx")


        driver= initiate_driver
        Cyberdone().cyber_arc()

        switching().switching_tabs(1)
        time.sleep(3)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, tin_field)))
        driver.find_element(by=By.XPATH,value=tin_field).click()


        try:
            el1=813174547
            if el1==201644291:
                driver.find_element(by=By.XPATH,value=tin_option1_medicaid).click().click()

            elif el1==273698244:
                driver.find_element(by=By.XPATH,value=tin_option2_medicaid).click()
            elif el1==382896881:
                driver.find_element(by=By.XPATH,value=tin_option3_medicaid).click()
            elif el1==383544427:
                driver.find_element(by=By.XPATH,value=tin_option4_medicaid).click()
            elif el1==412153406:
                driver.find_element(by=By.XPATH,value=tin_option5_medicaid).click()
            else:
                driver.find_element(by=By.XPATH,value=tin_option6_medicaid).click()
        except:
            pass
        #WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, plan_type_medicaid)))
        # driver.find_element(by=By.XPATH,value=plan_type).click()
        time.sleep(3)
        driver.find_element(by=By.XPATH,value=plan_type_medicaid).click()
        time.sleep(4)
        driver.find_element(by=By.XPATH,value=go_button).click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, claims)))
        driver.find_element(by=By.XPATH,value=claims).click()
        time.sleep(5)
        for i in range(data3.shape[0]):
        #for i in range(0,1):
            date1 = str(data3.at[i, "DOS"])

            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, change_date)))
            driver.find_element(by=By.XPATH,value=change_date).click()

            time.sleep(2)
            driver.find_element(By.XPATH,from_date).click()

            driver.find_element(by=By.XPATH,value=from_date).send_keys(date1)
            time.sleep(10)

            driver.find_element(By.XPATH,to_date).click()
            driver.find_element(by=By.XPATH,value=to_date).send_keys(date1)
            time.sleep(10)

            driver.find_element(by=By.XPATH,value=search).click()
            try:
                for z in range(0,50):
                    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,claim_NO)))

                    driver.find_elements(by=By.XPATH,value=claim_NO)[z].click()


                    time.sleep(2)
                    try:
                        element_error= driver.find_element(By.XPATH,error)
                        if element_error.is_displayed():
                            driver.back()

                        if not driver.find_element(By.XPATH,reload).is_displayed():
                            driver.refresh()


                    except:
                        pass
                    picking_data().picking_process()

                    time.sleep(3)
                    driver.find_element(By.XPATH, back_claim).click()
            except:
                pass

            continue
