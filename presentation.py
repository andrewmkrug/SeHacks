import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from subprocess import call



def wait(driver, locator):
    found = False
    while found == False:
        try:
            element = driver.find_element_by_css_selector(".slides section.present")
            if locator in element.text:
                found = True
            else:
                print(element.text)
                time.sleep(1)
        except:
            pass
    return element


def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(3)
    apply_style(original_style)

def release_me(driver, handle):
    driver.find_element_by_css_selector("body").send_keys(Keys.COMMAND + "t")

    driver.get("https://github.com/andrewmkrug/SeHacks/settings")


driver = webdriver.Chrome()
driver.get("http://localhost:9000/gitpitch/desktop#/")
#driver.get("http://localhost:9000/gitpitch/desktop#/18")
handle = driver.window_handles

driver.find_element_by_css_selector("body").send_keys("s")
time.sleep(10)
driver.find_element_by_css_selector("body").send_keys("f")
time.sleep(5)
driver.find_element_by_css_selector("body").send_keys(Keys.ARROW_DOWN)


#wait("button.navigate-down").click()
# wait("#forgotPassword")

wait(driver, "WAIT DO YOU WANT TO SEE IT?")
time.sleep(1)
highlight(driver.find_element_by_css_selector("#wait-do-you-want-to-see-it-"))

wait(driver, "AWESOMENESS AHEAD")
# driver.find_element_by_css_selector("body").send_keys("")


wait(driver, "QUESTIONS")
time.sleep(3)
release_me(driver, handle)