var Jasmine2HtmlReporter = require('protractor-jasmine2-html-reporter');

exports.config = {
    framework: 'jasmine',
    seleniumAddress: 'http://localhost:4444/wd/hub',
    capabilities: {
        browserName: 'chrome'
      },
    specs: ['./Specs/test_date_picker_spec.js', 
            './Specs/test_alert_spec.js',
            './Specs/test_protractor_demo_spec.js',
            './Specs/test_protractor_spec.js'],

    onPrepare: function(){
        jasmine.getEnv().addReporter(new Jasmine2HtmlReporter({
            savePath: './tests/Reports/'
        }))
    }
}