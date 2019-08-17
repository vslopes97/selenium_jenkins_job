// spec.js
describe('Protractor Demo', function() {
    browser.ignoreSynchronization = true; 
    
	it('choose selects', function() {
		browser.get("https://chercher.tech/practice/dropdowns")
		element(by.tagName("select#first")).click();
		browser.sleep(1000);
		element(by.css("#first [value='Yahoo']")).click();
    });
    
});