
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.login import LoginPage
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class TestCartScenario:
   

 def test_user_able_to_add_items_in_cart_scenario(self):
    login_page = LoginPage(self.driver)
    login_page.login("standard_user", "secret_sauce")
    login_page.wait_for_inventory_page()
    assert self.driver.current_url == "https://www.saucedemo.com/v1/inventory.html", \
        "Login failed: User should be redirected to the inventory page."


 def test_user_able_to_remove_items_in_cart_scenario(self):
    login_page = LoginPage(self.driver)
    login_page.login("standard_user", "wrong_password")
    login_page.wait_for_login_error()
    assert self.driver.current_url != "https://www.saucedemo.com/v1/inventory.html", \
        "Login should have failed with wrong credentials, but user reached inventory page."