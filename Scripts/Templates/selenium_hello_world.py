# coding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from Screenshot import Screenshot_Clipping
from Scripts.pageobjects.Data import User


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'/home/indtusuario/Documents/Selenium/Drivers/chrome_driver/chromedriver')

    def test_new_user(self):
        driver = self.driver
        driver.get("https://hvacnhurry.com")
        elem_login = driver.find_element_by_xpath("//a[contains(text(),'Log In')]")
        elem_login.click()
        driver.implicitly_wait(5)
        register = driver.find_element_by_xpath("//*[@id='register-link']")
        register.click()
        elem_email = driver.find_element_by_xpath("//input[@id='register_email']")
        elem_email.click()
        elem_email.send_keys("qwertyu@abcdef.com")
        elem_pwd = driver.find_element_by_xpath("//input[@id='register_pwd']")
        elem_pwd.click()
        elem_pwd.send_keys("22233385")
        elem_re_pwd = driver.find_element_by_xpath("//input[@id='register_re_pwd']")
        elem_re_pwd.click()
        elem_re_pwd.send_keys("22233385")
        register_btn = driver.find_element_by_xpath("//form[@id='register-form']/button")
        register_btn.click()
        driver.implicitly_wait(10)
        elem_logout = driver.find_element_by_xpath("//a[contains(text(),'Log Out')]")
        self.assertIn("LOG OUT", elem_logout.text)

    def test_email_badly_formatted(self):
        driver = self.driver
        driver.get("https://hvacnhurry.com")
        elem_login = driver.find_element_by_xpath("//a[contains(text(),'Log In')]")
        elem_login.click()
        driver.implicitly_wait(5)
        register = driver.find_element_by_xpath("//*[@id='register-link']")
        register.click()
        elem_email = driver.find_element_by_xpath("//input[@id='register_email']")
        elem_email.click()
        elem_email.send_keys("qwertyu")
        elem_pwd = driver.find_element_by_xpath("//input[@id='register_pwd']")
        elem_pwd.click()
        elem_pwd.send_keys("22233385")
        elem_re_pwd = driver.find_element_by_xpath("//input[@id='register_re_pwd']")
        elem_re_pwd.click()
        elem_re_pwd.send_keys("22233385")
        register_btn = driver.find_element_by_xpath("//form[@id='register-form']/button")
        register_btn.click()
        driver.implicitly_wait(10)
        elem_email_badly_formatted = driver.find_element_by_xpath("//*[@id='reg-error-response']")
        time.sleep(4)
        ob = Screenshot_Clipping.Screenshot()
        img_url = ob.full_Screenshot(driver=driver, save_path=r'.', image_name='Myimage.png')
        print(img_url)
        self.assertIn("The email address is badly formatted.", elem_email_badly_formatted.text)

    def test_different_passwords(self):
        driver = self.driver
        driver.get("https://hvacnhurry.com")
        elem_login = driver.find_element_by_xpath("//a[contains(text(),'Log In')]")
        elem_login.click()
        driver.implicitly_wait(5)
        register = driver.find_element_by_xpath("//*[@id='register-link']")
        register.click()
        elem_email = driver.find_element_by_xpath("//input[@id='register_email']")
        elem_email.click()
        elem_email.send_keys("qwertyu@a.com")
        elem_pwd = driver.find_element_by_xpath("//input[@id='register_pwd']")
        elem_pwd.click()
        elem_pwd.send_keys("22233385")
        elem_re_pwd = driver.find_element_by_xpath("//input[@id='register_re_pwd']")
        elem_re_pwd.click()
        elem_re_pwd.send_keys("22233386")
        register_btn = driver.find_element_by_xpath("//form[@id='register-form']/button")
        register_btn.click()
        driver.implicitly_wait(10)
        elem_login_error = driver.find_element_by_xpath("//*[@id='reg-error-response']")
        self.assertIn("Error: passwords do not match.", elem_login_error.text)

    def test_6_digit_less_password(self):
        driver = self.driver
        driver.get("https://hvacnhurry.com")
        elem_login = driver.find_element_by_xpath("//a[contains(text(),'Log In')]")
        elem_login.click()
        driver.implicitly_wait(5)
        register = driver.find_element_by_xpath("//*[@id='register-link']")
        register.click()
        elem_email = driver.find_element_by_xpath("//input[@id='register_email']")
        elem_email.click()
        elem_email.send_keys("qwertyu@a.com")
        elem_pwd = driver.find_element_by_xpath("//input[@id='register_pwd']")
        elem_pwd.click()
        elem_pwd.send_keys("2")
        elem_re_pwd = driver.find_element_by_xpath("//input[@id='register_re_pwd']")
        elem_re_pwd.click()
        elem_re_pwd.send_keys("2")
        register_btn = driver.find_element_by_xpath("//form[@id='register-form']/button")
        register_btn.click()
        driver.implicitly_wait(10)
        elem_pwd_error = driver.find_element_by_xpath("//*[@id='reg-error-response']")
        time.sleep(4)
        self.assertIn("Password should be at least 6 characters", elem_pwd_error.text)

    def test_combos(self):
        driver = self.driver
        driver.get("https://hvacnhurry.com")
        elem1 = driver.find_element_by_xpath("//select[@id='dd-mfr']")
        all_options = elem1.find_elements_by_tag_name("option")
        for option in all_options:
            if option.text == 'Acme':
                option.click()
        search = driver.find_element_by_xpath("//button[@id='search-btn']")
        search.click()

    def test_drag_and_drop(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://jqueryui.com/draggable/')
        driver.switch_to.frame(0)

        source1 = driver.find_element_by_id('draggable')
        action = ActionChains(driver)

        # move element by x,y coordinates on the screen
        action.drag_and_drop_by_offset(source1, 100, 100).perform()
        driver.implicitly_wait(15)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Test")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Results", driver.find_element_by_tag_name('h3').text)
        time.sleep(2)
        ob = Screenshot_Clipping.Screenshot()
        element = driver.find_element_by_xpath('//*[@id="content"]/div/section/form/ul/li[1]/h3/a')
        img_url = ob.get_element(driver, element, r'.')
        print(img_url)

    def test_signup_sucess(self):
        driver = self.driver
        driver.get("http://localhost:4000/#!/register")
        user = User()
        self.assertIn("Sign up", driver.title)
        username = driver.find_element_by_xpath("//input[@ng-model='$ctrl.formData.username']")
        username.send_keys(user.username)
        email = driver.find_element_by_xpath("//input[@ng-model='$ctrl.formData.email']")
        email.send_keys(user.email)
        password = driver.find_element_by_xpath("//input[@ng-model='$ctrl.formData.password']")
        password.send_keys(user.password)
        signup = driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right ng-binding']")
        signup.click()
        time.sleep(10)
        self.assertIn(user.username, driver.find_elements_by_xpath("//a[@class='nav-link ng-binding']")[0].text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
