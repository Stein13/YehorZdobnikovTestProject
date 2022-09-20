from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from logging import Logger


class Registration(BasePage):

    PAGE_HEADER = ".//*[@id='content']/h1"
    FIRST_NAME_INPUT = "input-firstname"
    LAST_NAME_INPUT = "input-lastname"
    EMAIL_INPUT = "input-email"
    PHONE_INPUT = "input-telephone"
    PASS_INPUT = "input-password"
    CONFIRM_PASS_INPUT = "input-confirm"
    POLICY_CHECK_BOX = ".//*[@name='agree']"
    SUBMIT_BTN = ".//*[@type='submit']"
    CONTINUE_BTN = ".//*[text()='Continue']"

    def __init__(self, driver, logger: Logger):
        self.logger = logger
        super(Registration, self).__init__(driver)

    # elements:
    def page_header(self):
        self.wait_until_located((By.XPATH, self.PAGE_HEADER))
        return self.find_element_by_xpath(self.PAGE_HEADER)

    def first_name_txt_field(self):
        return self.find_element_by_id(self.FIRST_NAME_INPUT)

    def last_name_txt_field(self):
        return self.find_element_by_id(self.LAST_NAME_INPUT)

    def email_txt_field(self):
        return self.find_element_by_id(self.EMAIL_INPUT)

    def phone_txt_field(self):
        return self.find_element_by_id(self.PHONE_INPUT)

    def pass_txt_field(self):
        return self.find_element_by_id(self.PASS_INPUT)

    def confirm_pass_txt_field(self):
        return self.find_element_by_id(self.CONFIRM_PASS_INPUT)

    def privacy_policy_checkbox(self):
        return self.find_element_by_xpath(self.POLICY_CHECK_BOX)

    def submit_btn(self):
        return self.find_element_by_xpath(self.SUBMIT_BTN)

    def continue_btn(self):
        return self.find_element_by_xpath(self.CONTINUE_BTN)

    # actions:
    def page_header_text(self):
        txt = self.page_header().text
        self.logger.info('Text from page header: {}'.format(txt))
        return txt

    def first_name_input(self, text):
        self.typing_text(text, self.first_name_txt_field())
        self.logger.info('Input {} into first name text field'.format(text))

    def last_name_input(self, text):
        self.typing_text(text, self.last_name_txt_field())
        self.logger.info('Input {} into last name text field'.format(text))

    def email_input(self, text):
        self.typing_text(text, self.email_txt_field())
        self.logger.info('Input {} into email text field'.format(text))

    def phone_input(self, text):
        self.typing_text(text, self.phone_txt_field())
        self.logger.info('Input {} into telephone text field'.format(text))

    def password_input(self, text):
        self.typing_text(text, self.pass_txt_field())
        self.logger.info('Input {} into password text field'.format(text))

    def confirm_password_input(self, text):
        self.typing_text(text, self.confirm_pass_txt_field())
        self.logger.info('Input {} into confirm password text field'.format(text))

    def privacy_policy_checkbox_click(self):
        self.privacy_policy_checkbox().click()
        self.logger.info('Set privacy policy checkbox')

    def submit_btn_click(self):
        self.submit_btn().click()
        self.logger.info('Submit button was clicked')

    def continue_btn_click(self):
        self.continue_btn().click()
        self.logger.info('Continue button was clicked')
