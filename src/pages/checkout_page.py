from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils import logger, string_util
from src.utils.element import click, find_elements, find_element, send_keys


class CheckOutPage(BasePage):
    # Elements
    # --------
    __BUTTON_ADD_TO_CARD_BACKPACK_INPUT = (By.ID, "add-to-cart-sauce-labs-backpack")
    __BUTTON_ADD_TO_CARD_BOLT_T_SHIRT_INPUT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    __ICON_SHOPPING_CARD = (By.ID, "shopping_cart_container")
    __TEXT_ON_SHOPPING_CARD = (By.CSS_SELECTOR, ".header_secondary_container span")
    # __ITEM_NAME = (By.XPATH, "//div[contains(text(),\"Sauce Labs Backpack\")]")

    __ITEM_NAME = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    __ITEM_PRICE_BY_TITLE = (
        By.XPATH, "//*[contains(text(),\"Sauce Labs Backpack\")]//../../div[contains(@class,\"item_pricebar\")]/div")

    __BUTTON_CHECK_OUT = (By.ID, "checkout")
    __HEADER_CHECKOUT_PAGE = (By.CSS_SELECTOR, ".header_secondary_container span")

    __FIRST_NAME_INPUT = (By.ID, "first-name")
    __LAST_NAME_INPUT = (By.ID, "last-name")
    __POSTCODE_INPUT = (By.ID, "postal-code")
    __CONTINUE_BUTTON = (By.ID, "continue")

    # Actions
    # -------
    def click_button_backpack(self):
        click(self.__BUTTON_ADD_TO_CARD_BACKPACK_INPUT)
        logger.info(f"Click 'Add to Card' backpack")

    def click_button_bolt_t_shirt(self):
        click(self.__BUTTON_ADD_TO_CARD_BOLT_T_SHIRT_INPUT)
        logger.info(f"Click 'Add to Card' Bolt T shirt")

    def click_icon_shopping_card(self):
        click(self.__ICON_SHOPPING_CARD)
        logger.info(f"Click icon shopping card")

    def click_on_button_checkout(self):
        click(self.__ICON_SHOPPING_CARD)
        logger.info(f"Click on button checkout")

    def get_list_title(self):
        elements = find_elements(self.__ITEM_NAME)
        list_title = []
        number = len(elements)
        print(number)
        for i in elements:
            print(i.text)
            list_title.append(i.text)
        return list_title

    def get_price_by_title(self, title):
        new_xpath = string_util.cook_element(self.__ITEM_PRICE_BY_TITLE, title)
        return find_element(new_xpath).text

    def click_on_button_checkout(self):
        click(self.__BUTTON_CHECK_OUT)
        logger.info(f"Click on check out button on your card")

    def enter_first_name(self, text):
        send_keys(self.__FIRST_NAME_INPUT, text)

    def enter_last_name(self, text):
        send_keys(self.__LAST_NAME_INPUT, text)

    def enter_post_code(self, text):
        send_keys(self.__POSTCODE_INPUT, text)

    def click_on_button_continue(self):
        click(self.__CONTINUE_BUTTON)

    def get_header_checkout_page(self):
        pass


checkout_page = CheckOutPage()
