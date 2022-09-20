from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from logging import Logger


class TopBar(BasePage):

    MY_ACCOUNT_BTN = ".//*[@title='My Account']"
    LOGIN = ".//ul[@class='dropdown-menu dropdown-menu-right']/*/a[text()='Login']"
    REGISTRATION = ".//ul[@class='dropdown-menu dropdown-menu-right']/*/a[text()='Register']"
    MP3_PLAYERS = ".//*/a[text()='MP3 Players']"
    SHOW_ALL_MP3_PLAYERS = ".//*/a[text()='Show All MP3 Players']"
    CART = "cart"
    PRODUCT_HEADER_IN_CART = ".//*[@class='dropdown-menu pull-right']//td[@class='text-left']/a"
    MY_ACCOUNT_CELL_IN_DROPDOWN = ".//*[@class='dropdown-menu dropdown-menu-right']//a[text()='My Account']"

    def __init__(self, driver, logger: Logger):
        self.logger = logger
        super(TopBar, self).__init__(driver)

    # elements:
    def my_account_btn(self):
        return self.find_element_by_xpath(self.MY_ACCOUNT_BTN)

    def log_in(self):
        self.wait_until_located((By.XPATH, self.LOGIN))
        return self.find_element_by_xpath(self.LOGIN)

    def registration(self):
        self.wait_until_located((By.XPATH, self.REGISTRATION))
        return self.find_element_by_xpath(self.REGISTRATION)

    def my_account_cell_in_dropdown(self):
        self.wait_until_located((By.XPATH, self.MY_ACCOUNT_CELL_IN_DROPDOWN))
        return self.find_element_by_xpath(self.MY_ACCOUNT_CELL_IN_DROPDOWN)

    def mp3_players(self):
        return self.find_element_by_xpath(self.MP3_PLAYERS)

    def show_all_mp3_players(self):
        self.wait_until_located((By.XPATH, self.SHOW_ALL_MP3_PLAYERS))
        return self.find_element_by_xpath(self.SHOW_ALL_MP3_PLAYERS)

    def cart_btn(self):
        return self.find_element_by_id(self.CART)

    def product_header_in_cart(self):
        self.wait_until_located((By.XPATH, self.PRODUCT_HEADER_IN_CART))
        return self.find_element_by_xpath(self.PRODUCT_HEADER_IN_CART)

    # actions:
    def my_account_click(self):
        self.my_account_btn().click()
        self.logger.info('My account button was clicked')

    def log_in_click(self):
        self.log_in().click()
        self.logger.info('Login button was clicked')

    def registration_click(self):
        self.registration().click()
        self.logger.info('Registration button was clicked')

    def hover_to_mp3_players(self):
        self.hover_to_element(self.mp3_players())
        self.logger.info('Cursor hovered to mp3 players dropdown')

    def show_all_mp3_player_click(self):
        self.show_all_mp3_players().click()
        self.logger.info('Show all button was clicked')

    def cart_btn_click(self):
        self.cart_btn().click()
        self.logger.info('Cart button was clicked')

    def product_in_cart_text(self):
        txt = self.product_header_in_cart().text
        self.logger.info('Text from page header: {}'.format(txt))
        return txt
