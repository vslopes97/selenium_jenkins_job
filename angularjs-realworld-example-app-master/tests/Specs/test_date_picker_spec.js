describe('Protractor Demo', function() {
    browser.ignoreSynchronization = true; 
    
	it('choose date', function() {
        browser.get("http://www.mattkruse.com/javascript/calendarpopup/");
        browser.ignoreSynchronization =true;
        element(by.xpath("//a[@id='anchor1x']")).click().then(function(){
            element(by.xpath("//a[contains(text(),'16')]")).click();
            browser.sleep(1000);
        });
        
    });
    
});