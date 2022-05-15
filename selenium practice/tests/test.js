const {By,Key,Builder} = require("selenium-webdriver");
require("chromedriver");

// async function myFirstTest(){
//     var searchString = "Automation testing with selenium and javascript";

//     const driver = await new Builder().forBrowser("chrome").build();

//     await driver.get("http://google.com");

//     await driver.findElement(By.name("q")).sendKeys(searchString,Key.RETURN);

//     var title = await driver.getTitle();
//     console.log("Title is",title);

//     await driver.quit();
// }

// myFirstTest()

(async function example() {
    let driver = await new Builder().forBrowser('chrome').build();
  
    try {
      // Navigate to Url
      await driver.get('https://www.google.com');
  
      // Enter text "webdriver" and perform keyboard action "Enter"
      await driver.findElement(By.name('q')).sendKeys('webdriver', Key.ENTER);
  
      // Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
      await driver.actions().keyDown(Key.CONTROL).sendKeys('a').perform();
    }
    finally {
      await driver.quit();
    }
  })();
    