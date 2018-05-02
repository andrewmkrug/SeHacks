import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait(locator):
    wait = WebDriverWait(driver, 900)
    element = wait.until(EC.element_to_be_clickable((By.ID, locator)))


def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(1)
    apply_style(original_style)

driver = webdriver.Firefox()
driver.get("http://locahost:9000")

wait("forgotPassword")

wait("highlight")

highlight(driver.find_element_by_class_name("highlight(driver.find_element)"))
driver.close()