import allure
import pytest

from src.pages.cart_page import card_page
from src.pages.checkout_page import checkout_page
from src.pages.order_page import order_page
from src.utils import common
from tests import MasterTest


@pytest.mark.usefixtures("before_test_order")
class OrderTest(MasterTest):

    @allure.title("Verify order successfull")
    def test_order_successful(self):
        order_page.click_button_backpack()
        order_page.click_button_bolt_t_shirt()

        with allure.step("First fullfill user name/Password "):
            title_backpack = order_page.get_title_card_back_input()
            price_backpack = order_page.get_title_t_shirt()
            order_page.click_icon_shopping_card()
            order_page.click_on_button_checkout()

        list_title = checkout_page.get_list_title()

        # Verify title as what user selected
        assert title_backpack in list_title
        assert price_backpack in list_title

        # number_in_checkout_page =
        print("-------------------")
        print(list_title)
        checkout_page.click_on_button_checkout()

        common.sleep(2)
        with allure.step("First fullfill first name /last name/ passcode "):
            checkout_page.enter_first_name("Lan")
            checkout_page.enter_last_name("nguyen")
            checkout_page.enter_post_code("8000")
            checkout_page.click_on_button_continue()

        # Verify product name in Card View
        list_title_in_card_view = card_page.get_list_title()
        with allure.step(" Verify title of product "):
            assert title_backpack in list_title_in_card_view
            assert price_backpack in list_title_in_card_view

        # verify price  in  Card View
        list_price = card_page.get_list_price()
        total_price = 0
        for price in list_price:
            print("each price")
            print(price)
            price_after = price.replace("$", "")
            print(price_after)
            total_price += float(price_after)

        print(f"------ TOTAL PRICE  --------{total_price}")

        total_price_in_cardview = card_page.get_sub_total().replace("Item total: $", "")
        print(f"------ TOTAL PRICE IN CARD VIEW  --------{total_price_in_cardview}")
        total_price_string = str(total_price)
        with allure.step(" Verify  price of price in Card View  "):
            assert total_price_string == total_price_in_cardview
        print(list_price)
        common.sleep(2)
        pass
