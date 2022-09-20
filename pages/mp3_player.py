from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from logging import Logger


class Mp3Players(BasePage):

    PAGE_HEADER = ".//*[@id='content']/h2"
    IPOD_CLASSIC = ".//*/a[text()='iPod Classic']"
    PRODUCT_HEADER = ".//*[@id='content']//h1"
    ADD_TO_CART = "button-cart"

    def __init__(self, driver, logger: Logger):
        self.logger = logger
        super(Mp3Players, self).__init__(driver)

    # elements:
    def page_header(self):
        self.wait_until_located((By.XPATH, self.PAGE_HEADER))
        return self.find_element_by_xpath(self.PAGE_HEADER)

    def ipod_classic(self):
        return self.find_element_by_xpath(self.IPOD_CLASSIC)

    def product_header(self):
        self.wait_until_located((By.XPATH, self.PRODUCT_HEADER))
        return self.find_element_by_xpath(self.PRODUCT_HEADER)

    def add_to_cart_btn(self):
        return self.find_element_by_id(self.ADD_TO_CART)

    # actions:
    def page_header_text(self):
        txt = self.page_header().text
        self.logger.info('Text from page header: {}'.format(txt))
        return txt

    def product_header_text(self):
        txt = self.product_header().text
        self.logger.info('Text from product header: {}'.format(txt))
        return txt

    def ipod_classic_click(self):
        self.ipod_classic().click()
        self.logger.info('Ipod Classic hyperlink text was clicked')

    def add_to_cart_btn_click(self):
        self.add_to_cart_btn().click()
        self.logger.info('Add to cart button was clicked')
