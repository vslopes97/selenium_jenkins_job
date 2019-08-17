describe('Protractor Demo', function() {

    beforeEach(function() {
        browser.ignoreSynchronization = true; 
    });

	it('Alerts operation', function() {
        browser.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver");
		element(by.name("alert")).click();
		let ale = browser.switchTo().alert();
        ale.accept();        
        browser.sleep(20);
    });    
});