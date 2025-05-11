from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest
from utility import ReadConfigurationFile

@pytest.fixture()
def setup_and_teardown(request):

        browser=  ReadConfigurationFile.read_configuration("basic info","browser")
        if browser.__eq__("chrome"):
                driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser.__eq__("firefox"):
                driver = webdriver.Firefox()
        elif browser.__eq__("edge"):
                driver = webdriver.Edge()
        else:
                print("provide a valid browser name from this list chrome/firefox/edge")

        driver.maximize_window()
        url= ReadConfigurationFile.read_configuration("basic info","url")
        driver.get(url)
        request.cls.driver = driver
        time.sleep(5)   
        yield
        driver.quit()