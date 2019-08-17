import time
from Scripts.pageobjects.SignupPage_po import SignupPage
from Scripts.pageobjects.Data import User
from Scripts.pageobjects.HomePage_po import HomePage
from Scripts.pageobjects.TestTemplate import TestTemplate
from Scripts.pageobjects.NewArticle_po import NewArticle
from Scripts.pageobjects.Article_po import Article
from Scripts.pageobjects.Data import ArticleFilling


class TestCreateArticle(TestTemplate):
    def test_create_article(self):
        home_page = HomePage(self.driver)
        new_article_page = NewArticle(self.driver)
        article_page = Article(self.driver)

        signup_page = SignupPage(self.driver)
        signup_page.set_user(User.username)
        signup_page.set_email(User.email)
        signup_page.set_pass(User.password)
        signup_page.signup()

        time.sleep(5)
        home_page.launch_new_article()
        time.sleep(5)

        new_article_page.input_title(ArticleFilling.title)
        new_article_page.input_description(ArticleFilling.description)
        new_article_page.input_article_text(ArticleFilling.text)
        new_article_page.input_tags(ArticleFilling.tags)
        new_article_page.publish()
        time.sleep(5)

        assert article_page.is_in_page(), 'Article page should have been reached'
