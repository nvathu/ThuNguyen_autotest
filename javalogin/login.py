from selenium import webdriver
from time import sleep

class Google:

    def __init__(self, username, password):

        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get('https://youtube.com')
        sleep(5)

username = 'rdteam1510@gmail.com'
passwort = 'dataanalysis0621'
Google(username, password)