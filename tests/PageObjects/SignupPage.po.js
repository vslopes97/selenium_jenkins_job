var SignupPage = function(){

    this.title = 'Sign up — Conduit';
    this.dirNgBind = element(by.linkText('ngBind'));
    this.username = element(by.model('$ctrl.formData.username'));
    this.email = element(by.model('$ctrl.formData.email'));
    this.password = element(by.model('$ctrl.formData.password'));
    this.signupButton = element(by.xpath("//button[@class='btn btn-lg btn-primary pull-xs-right ng-binding']"));
    var text = "username has already been taken";
    this.duplicaterusername = element(by.cssContainingText('li.ng-binding.ng-scope', text));

};

SignupPage.prototype.visit = function(){
    browser.get('http://localhost:4000/#!/register');
};

module.exports = SignupPage;