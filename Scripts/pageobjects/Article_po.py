import time
from BasePage import BasePage


class Article(BasePage):
    et_write_comment = "//textarea[@placeholder='Write a comment...']"
    bt_post_comment = "//button[@class='btn btn-sm btn-primary']"

    def is_in_page(self):
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        return self._driver.find_elements_by_xpath(self.et_write_comment) and \
               self._driver.find_elements_by_xpath(self.bt_post_comment)
