import allure

from src.consts import consts
from src.pages.login import login_page
from src.pages.order_page import order_page
from src.utils import json_util, common, logger
from tests import MasterTest


class LoginTest(MasterTest):

    @allure.title("Verify test_login_successful")
    def test_login_successful(self):
        # Test data
        try:
            print("-----test login")
            file_path = consts.PROJECT_ROOT + "/data/login.json"
            json_data = json_util.load(file_path)
            pr_data = json_data["tc01"]
            # Test steps
            with allure.step("First fullfill user name/Password "):
                login_page.type_user(pr_data["username"])
                login_page.type_password(pr_data["password"])
                login_page.click_sign_me_in_button()

            assert login_page.verify_avatar() == True

        except Exception as ex:
            logger.error(ex)
            self.failures.append(ex)
        finally:
            self.screenshot_binary_data.append(self.save_screenshot())

    @allure.title("Verify test_login_invalid_password")
    def test_login_invalid_password(self):
        # Test data
        try:
            print("-----test login")
            file_path = consts.PROJECT_ROOT + "/data/login.json"
            json_data = json_util.load(file_path)
            pr_data = json_data["tc02"]
            # Test steps

            login_page.type_user(pr_data["username"])
            login_page.type_password(pr_data["password"])
            login_page.click_sign_me_in_button()

            assert login_page.verify_message_login_fail(pr_data["message"]) == True
            # logger.info(" avatar is displayed")
            common.sleep(1)
        except Exception as ex:
            logger.error(ex)
            self.failures.append(ex)
        finally:
            self.screenshot_binary_data.append(self.save_screenshot())
        # Test cleanup

    @classmethod
    def setup_class(cls):
        print("---- BEFORE  CLASS")
        pass

    @classmethod
    def teardown_class(cls):
        order_page.click_menu_icon()
        order_page.click_logout()
        print("---- AFTER CLASS----")
        pass
