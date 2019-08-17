var SignupPage = require('../PageObjects/SignupPage.po');
var HomePage = require('../PageObjects/HomePage.po');
var NewArticlePage = require('../PageObjects/NewArticle.po');
var ArticlePage = require('../PageObjects/ArticlePage.po');

describe('Sign Up Test', function() {
  var signupPage = new SignupPage();
  var homePage = new HomePage();
  var newArticlePage = new NewArticlePage();
  var articlePage = new ArticlePage();

  beforeEach(function() {
    signupPage.visit();
    browser.driver.manage().window().maximize();
  });

  it('it should have a title', function() {
    expect(browser.getTitle()).toEqual(signupPage.title);
  });

  it('it should sign up new user', function(){
    let user = Math.random().toString(36).substring(2, 5)
    let email = user + "@gmail.com"
    signupPage.username.sendKeys(user);
    signupPage.email.sendKeys(email);
    signupPage.password.sendKeys('1234567890');
    signupPage.signupButton.click().then(function() {
        expect(homePage.signed.getText()).toEqual(user);
      });
  });

  it('it should create a new article', function(){
    homePage.launch_new_article();

    newArticlePage.input_title("Valid Title");
    newArticlePage.input_description("Valid Description");
    newArticlePage.input_article_text("Valid Article text");
    newArticlePage.input_tags("Valid Tags");
    newArticlePage.publish();
    expect(articlePage.is_in_page()).toBe(true);
  });
});