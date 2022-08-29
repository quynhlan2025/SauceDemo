from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils import logger
from src.utils.element import click, find_elements, find_element


class CardPage(BasePage):
    # Elements
    # --------
    __ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    __ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    __SUB_TOTAL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    __TAX = (By.CSS_SELECTOR, ".summary_tax_label")
    __TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

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

    def get_list_price(self):
        elements = find_elements(self.__ITEM_PRICE)
        list_price = []
        number = len(elements)
        print(number)
        for i in elements:
            print(i.text)
            list_price.append(i.text)
        return list_price

    def get_sub_total(self):
        return find_element(self.__SUB_TOTAL).text

    def get_total(self):
        return find_element(self.__TOTAL_LABEL).text

    def get_tax(self):
        return find_element(self.__TAX).text

    def get_header_checkout_page(self):
        pass


card_page = CardPage()
