from conftest import driver

class switching():
    def switching_tabs(self, num):
        tabs = driver.window_handles
        driver.switch_to.window(tabs[num])

