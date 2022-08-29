from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils import logger
from src.utils.element import click, find_element


class OrderPage(BasePage):
    # Elements
    # --------
    __BUTTON_ADD_TO_CARD_BACKPACK_INPUT = (By.ID, "add-to-cart-sauce-labs-backpack")
    __BUTTON_ADD_TO_CARD_BOLT_T_SHIRT_INPUT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    __ICON_SHOPPING_CARD = (By.ID, "shopping_cart_container")
    __TEXT_ON_SHOPPING_CARD = (By.CSS_SELECTOR, ".header_secondary_container span")
    __TITLE_CARD_BOLT_T_SHIRT = (By.XPATH, "//*[@id='remove-sauce-labs-bolt-t-shirt']/../../div/a/div")
    __TITLE_CARD_BACKPACK_INPUT = (By.XPATH, "//*[@id='remove-sauce-labs-backpack']/../../div/a/div")
    __PRICE_BACKPACK = (
        By.XPATH, "//*[@id='remove-sauce-labs-bolt-t-shirt']/../../div/div[@class=\"inventory_item_price\"]")
    #MENU
    __ICON_MENU=(By.ID,"react-burger-menu-btn")
    __ICON_LOGOUT=(By.ID,"logout_sidebar_link")

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

    def get_title_card_back_input(self):
        title = find_element(self.__TITLE_CARD_BACKPACK_INPUT).text
        logger.info(f"Title of BACKPACK_INPUT {title} ")
        return title

    def get_title_t_shirt(self):
        title = find_element(self.__TITLE_CARD_BOLT_T_SHIRT).text
        logger.info(f"Title of T-SHIRT_INPUT {title} ")
        return title

    def get_price_card_back_input(self):
        price = find_element(self.__PRICE_BACKPACK).text
        logger.info(f"Title of BACKPACK_INPUT {price} ")
        return price

    def click_menu_icon(self):
        click(self.__ICON_MENU)
        logger.info(f" click on icon menu ")

    def click_logout(self):
        click(self.__ICON_LOGOUT)
        logger.info(f" click on icon log out ")



order_page = OrderPage()
