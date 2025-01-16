from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.homepage import HomePage
from pages.product import ProductPage
import time


def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is("Samsung galaxy s6")




def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    product = ProductPage(driver)
    time.sleep(2)
    product.check_products_count(2)

def test_tst():
    assert 1 == 2
