from BasePage import BasePage


class SignupPage(BasePage):
    username = "//input[@ng-model='$ctrl.formData.username']"
    email = "//input[@ng-model='$ctrl.formData.email']"
    password = "//input[@ng-model='$ctrl.formData.password']"
    signup_button = "//button[@class='btn btn-lg btn-primary pull-xs-right ng-binding']"
    signed = "//a[@class='nav-link ng-binding']"

    def set_user(self, user):
        self._driver.find_element_by_xpath(SignupPage.username).send_keys(user)

    def set_email(self, mail):
        self._driver.find_element_by_xpath(SignupPage.email).send_keys(mail)

    def set_pass(self, passw):
        self._driver.find_element_by_xpath(SignupPage.password).send_keys(passw)

    def signup(self):
        return self._driver.find_element_by_xpath(SignupPage.signup_button).click()
