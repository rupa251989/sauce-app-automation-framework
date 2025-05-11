from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    username_field_name = "user-name"
    password_field_name = "password"
    submit_login_button_locator = "login-button"
   

    def enter_username(self,username):
        element= self.driver.find_element(By.ID,self.username_field_name)
        element.send_keys(username)

    def enter_password(self,password):
        element = self.driver.find_element(By.ID,self.password_field_name)
        element.send_keys(password)

    def click_on_submit_button(self):
        element = self.driver.find_element(By.ID,self.submit_login_button_locator)
        element.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_submit_button()

    def wait_for_inventory_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/v1/inventory.html")
        )

    def wait_for_login_error(self):
         error_element = WebDriverWait(self.driver, 10).until(
         EC.url_to_be("https://www.saucedemo.com/v1/")
        )

  