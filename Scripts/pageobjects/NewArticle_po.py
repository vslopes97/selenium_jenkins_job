from BasePage import BasePage


class NewArticle(BasePage):
    et_title = "//input[@placeholder='Article Title']"
    et_description = '//input[@placeholder="What\'s this article about?"]'
    et_article_text = "//textarea[@placeholder='Write your article (in markdown)']"
    et_tags = "//input[@placeholder='Enter tags']"
    bt_publish = "//button[@class='btn btn-lg pull-xs-right btn-primary']"

    def input_title(self, title):
        self._driver.find_elements_by_xpath(self.et_title)[0].send_keys(title)

    def input_description(self, description):
        self._driver.find_elements_by_xpath(self.et_description)[0].send_keys(description)

    def input_article_text(self, text):
        self._driver.find_elements_by_xpath(self.et_article_text)[0].send_keys(text)

    def input_tags(self, tags):
        self._driver.find_elements_by_xpath(self.et_tags)[0].send_keys(tags)

    def publish(self):
        self._driver.find_elements_by_xpath(self.bt_publish)[0].click()
