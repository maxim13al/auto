from selenium.webdriver.common.by import By

class HomePage:
    URL = "https://www.demoblaze.com/"
    SAMSUNG = (By.XPATH, "//a[text()='Samsung galaxy s6']")   
    MONITOR = (By.XPATH, "//a[text()='Monitors']")

    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get(self.URL)

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(*self.SAMSUNG)
        galaxy_s6.click()

    def click_monitor(self):
        monitor = self.driver.find_element(*self.MONITOR)
        monitor.click()


