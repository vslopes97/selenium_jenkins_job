import unittest
from selenium import webdriver


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'/home/indtusuario/Documents/Selenium/Drivers/chrome_driver/chromedriver')
        self.driver.get("http://localhost:4000/#!/register")

    def tearDown(self):
        self.driver.quit()
