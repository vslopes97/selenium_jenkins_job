var NewArticle = function(){
    this.title = element.all(by.xpath("//input[@placeholder='Article Title']")).first();
    this.description = element.all(by.xpath('//input[@placeholder="What\'s this article about?"]')).first();
    this.article_text = element.all(by.xpath("//textarea[@placeholder='Write your article (in markdown)']")).first();
    this.tags = element.all(by.xpath("//input[@placeholder='Enter tags']")).first();
    this.publish = element(by.xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']")).first();
};

NewArticle.prototype.input_title = function(title) {
    return this.title.sendKeys(title);
};

NewArticle.prototype.input_description = function(description) {
    return this.description.sendKeys(description);
};

NewArticle.prototype.input_article_text = function(article_text) {
    return this.article_text.sendKeys(article_text);
};

NewArticle.prototype.input_tags = function(tags) {
    return this.tags.sendKeys(tags);
};

NewArticle.prototype.publish = function() {
    this.publish.click();
};

module.exports = NewArticle;