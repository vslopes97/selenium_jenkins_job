var ArticlePage = function(){
    this.write_comment = element.all(by.xpath("//textarea[@placeholder='Write a comment...']")).first();
    this.post_comment = element.all(by.xpath("//button[@class='btn btn-sm btn-primary']")).first();
};

ArticlePage.prototype.is_in_page = function() {
    browser.executeScript('window.scrollTo(0,0);').then(function () {
        return Boolean(this.write_comment, this.post_comment);
    })
};

module.exports = ArticlePage;