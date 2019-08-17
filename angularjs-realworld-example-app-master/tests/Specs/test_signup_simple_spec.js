describe('Signup test', function() {
    var username = element(by.model('$ctrl.formData.username'));
    var email = element(by.model('$ctrl.formData.email'));
    var password = element(by.model('$ctrl.formData.password'));
    var signupButton = element(by.xpath("//button[@class='btn btn-lg btn-primary pull-xs-right ng-binding']"));
    var signed = element.all(by.xpath("//a[@class='nav-link ng-binding']")).first();
    var text = "username has already been taken";
    var duplicaterusername = element(by.cssContainingText('li.ng-binding.ng-scope', text));

    var test_user = "DevSerTester";
    var test_email = "devsertester@gmail.com";
    var test_pwd = "cardume-coworking";
    
    var new_test_user = "maldkmfsl";
    var new_test_email = "sdflknmsdk@gmail.com";
    var new_test_pwd = "1092830911";

    function random_user() {
        var characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz';
        var user, email = '';
        for (var i = 0; i < 5; i++) {
            var rnum = Math.floor(Math.random() * characters.length);
            user += characters.substring(rnum, rnum + 1);
        }

        email = user + '@gmail.com';
        console.log(user, email);
        return user, email;
    }
   
    beforeEach(function() {
      browser.get('http://localhost:4000/#!/register');
    });
  
    it('it should have a title', function() {
      expect(browser.getTitle()).toEqual('Sign up — Conduit');
    });

    it(' it should display error when username is duplicated', function() {
      username.sendKeys(test_user);
      email.sendKeys(test_email);
      password.sendKeys(test_pwd);

      //clica no botão e depois faz o assert
      signupButton.click().then(function () {
        expect(duplicaterusername.getText()).toEqual(text);
      }); 

     });
  
    it('it should sign up new user', function() {
      username.sendKeys(new_test_user);
      email.sendKeys(new_test_email);
      password.sendKeys(new_test_pwd);

      //clica no botão e depois faz o assert
      signupButton.click().then(function() {
        expect(signed.getText()).toEqual(new_test_user);
      }); 

    }); 
});