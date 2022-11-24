import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
option = Options()
option.headless = False
option.add_extension('C:\extension_22_11_2_0.crx')

driver = webdriver.Chrome(options=option)

@pytest.fixture()
def initiate_driver():
    driver.get("https://empclaims.my.idaptive.app/my#/MyApps")
    driver.maximize_window()
    yield driver

    driver.close()
