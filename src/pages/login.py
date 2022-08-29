import allure
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils import logger
from src.utils.element_util import find_elements, send_keys, click, find_element


class LoginPage(BasePage):
    # Elements
    # --------
    __USER_INPUT = (By.ID, "user-name")
    __PASSWORD_INPUT = (By.ID, "password")
    __SIGN_ME_IN_BUTTON = (By.ID, "login-button")
    __LOGO = (By.CSS_SELECTOR, ".app_logo")
    __MESSAGE_LOGIN_FAILED = (By.CSS_SELECTOR, ".error-message-container h3")

    # Actions
    # -------

    def type_user(self, username):
        send_keys(self.__USER_INPUT, username)
        logger.info("Type user: " + username)

    def type_password(self, password):
        send_keys(self.__PASSWORD_INPUT, password)
        logger.info(f"Type password: {password}")

    def click_sign_me_in_button(self):
        click(self.__SIGN_ME_IN_BUTTON)
        logger.info("Click 'Sign me in' button")


    def verify_avatar(self):
        element = find_elements(self.__LOGO)
        logger.info(" avatar is displayed")
        return element.is_displayed()

    def verify_message_login_fail(self, message):
        ele_message = find_elements(self.__MESSAGE_LOGIN_FAILED)
        logger.info(f"message failed:{ele_message.text} and {message}")
        if message == ele_message.text:
            print(f'message failed:{ele_message.text} are equal {message}"')
            return True

        else:
            print(f'message :{ele_message.text} not {message}"')
            return False

    def login(self, username, password):
        self.type_user(username)
        self.type_password(password)
        self.click_sign_me_in_button()

    def wait_for_product_list_loaded(self):
        element = find_element(self.__LOGO)
        return element.is_displayed()


login_page = LoginPage()
