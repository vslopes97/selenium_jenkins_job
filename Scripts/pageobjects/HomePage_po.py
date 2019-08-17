from BasePage import BasePage


class HomePage(BasePage):
    signed = "//a[@class='nav-link ng-binding']"
    tv_new_article = "//a[@href='#!/editor/']"

    def signup_check(self):
        return self._driver.find_elements_by_xpath(self.signed)[0].text

    def launch_new_article(self):
        self._driver.find_elements_by_xpath(self.tv_new_article)[0].click()
