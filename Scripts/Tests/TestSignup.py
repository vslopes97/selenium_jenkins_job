import time
from Scripts.pageobjects.HomePage_po import HomePage
from Scripts.pageobjects.SignupPage_po import SignupPage
from Scripts.pageobjects.TestTemplate import TestTemplate
from Scripts.pageobjects.Data import User


class TestSignup(TestTemplate):
    def test_signup_success(self):
        signup_page = SignupPage(self.driver)
        signup_page.set_user(User.username)
        signup_page.set_email(User.email)
        signup_page.set_pass(User.password)
        signup_page.signup()
        time.sleep(10)
        home_page = HomePage(self.driver)
        self.assertEqual(User.username, home_page.signup_check())
