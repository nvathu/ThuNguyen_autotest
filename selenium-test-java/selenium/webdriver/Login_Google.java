package webdriver;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;


public class Login_Google {
    WebDriver driver;


    System.setProperty("webdriver.chrome.driver",System.getProperty("user.dir")+"/browserDrivers/chromedriver.exe");
    driver = new ChromeDriver();

    GeneralClass te = new GeneralClass();

    driver.get("https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn."
            +"apps.googleusercontent.com&as=JS6BM8cjL-8j9votansdkw&destination=https%3A%2F%2Fstackauth"
            +".com&approval_state=!ChRoYWVvLUlNMk5hSXJWUGlaSVl2WBIfc3lSa0lueENpb29lSU5vbEVpbVNxcUZGaGNkSEJoYw%E2%88%99AJDr988AAAAAXlBKc7PzEomxSzgNqd4wLptVlf0Ny3Qx&oauthgdpr=1&xsrfsig=ChkAeAh8T8JNDxCf2Zah5fb_rQ55OMiF8KmMEg5hcHByb3ZhbF9zdGF0ZRILZGVzdGluYXRpb24SBXNvYWN1Eg9vYXV0aHJpc2t5c2NvcGU&flowName=GeneralOAuthFlow");
    te.waitingForElementSendingKey(driver,By.id("identifierId"),"XXXXXXXX@gmail.com");
    te.waitingForElementForClickOnly(driver,By.id("identifierNext"));
    te.waitingForElementSendingKey(driver,By.name("password"),"PASSSWORD");
    te.waitingForElementForClickOnly(driver,By.id("passwordNext"));
    Thread.sleep(1500);
    driver.get("https://mail.google.com/mail/u/0/#inbox");
}
