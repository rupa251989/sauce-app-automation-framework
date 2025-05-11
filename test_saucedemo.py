
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()

        
    def test_login_positive(self):
        driver = self.driver
        
        driver.get("https://www.saucedemo.com/v1/")
        
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")

        password = driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")

        login = driver.find_element(By.ID,"login-button")
        login.click()

        assert driver.current_url == "https://www.saucedemo.com/v1/inventory.html",f"it should have been login but it is failing"


    def test_login_negative(self):
        driver = self.driver
        
        driver.get("https://www.saucedemo.com/v1/")
        
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")

        password = driver.find_element(By.ID,"password")
        password.send_keys("negative")

        login = driver.find_element(By.ID,"login-button")
        login.click()

        assert driver.current_url != "https://www.saucedemo.com/v1/inventory.html",f"it should have been failed but login"

    def teardown_method(self):
        self.driver.quit()





