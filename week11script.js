const { Builder, By } = require("selenium-webdriver");

async function testSum() {
  // Open Chrome
  let driver = await new Builder().forBrowser("chrome").build();

  try {
    // Load local HTML file
    await driver.get(
      "file:///C:/users/ruthv/OneDrive/Attachments/Desktop/New folder/index.html"
    );
    // 👉 Change this path to your file location!

    // Enter values
    await driver.findElement(By.id("num1")).sendKeys("5");
    await driver.findElement(By.id("num2")).sendKeys("7");

    // Click Add
    await driver.findElement(By.tagName("button")).click();

    // Get Result
    let result = await driver.findElement(By.id("result")).getText();

    console.log("Result = " + result);

    // 👇 WAIT 5 seconds so you can see browser
    await driver.sleep(5000);
  } catch (err) {
    console.log("Error:", err);
  } finally {
    await driver.quit();
  }
}

testSum();
