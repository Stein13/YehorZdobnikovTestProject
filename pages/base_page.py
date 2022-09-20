from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element_by_id(self, *args):
        return self.driver.find_element(By.ID, *args)

    def find_element_by_xpath(self, *args):
        return self.driver.find_element(By.XPATH, *args)

    def wait_until_located(self, *args):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(*args))

    def wait_until_clickable(self, *args):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(*args))

    def typing_text(self, text, element):
        value = element.get_attribute('text')
        if value:
            element.clear()
        element.send_keys(text)

    def hover_to_element(self, element):
        h = ActionChains(self.driver).move_to_element(element)
        h.perform()
