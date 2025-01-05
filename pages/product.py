from selenium.webdriver.common.by import By

class ProductPage:
    TITLE = (By.XPATH, "//h2")
    PRODUCTS = (By.XPATH, "//div[@class='card-block']")


    def __init__(self, driver):
        self.driver = driver        

    def check_title_is(self, title):
        page_title = self.driver.find_element(*self.TITLE)
        assert page_title.text == title, f"{page_title.text} != {title}"

    def check_products_count(self, count):
        products = self.driver.find_elements(*self.PRODUCTS)
        assert len(products) == count

