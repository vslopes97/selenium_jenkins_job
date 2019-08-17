var HomePage = function(){
    this.title = 'Home — Conduit';
    this.signed = element.all(by.xpath("//a[@class='nav-link ng-binding']")).first();
    this.new_article = element.all(by.xpath("//a[@href='#!/editor/']")).first()
};

HomePage.prototype.signup_check = function() {
    return this.signed.text;
};

HomePage.prototype.launch_new_article = function() {
    return this.new_article.click();
};

module.exports = HomePage;