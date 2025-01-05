from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
import time


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1500,800")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options = chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()