# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service 
# from time import sleep

# class Google:

#     def __init__(self, username, password):
#         self.service = Service(executable_path=ChromeDriverManager().install());
#         self.driver = webdriver.Chrome(service=self.service)
#         self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
#         sleep(3)
#         self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
#         self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
#         self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
#         sleep(3)
#         self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
#         self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
#         sleep(2)
#         self.driver.get('https://youtube.com')
#         sleep(5)

# username = 'rdteam1510'
# password = 'dataanalysis0621'
# Google(username, password)

# import undetected_chromedriver.v2 as uc
# import random,time,os,sys
# from selenium.webdriver.common.keys import Keys

# GMAIL = 'rdteam1510@gmail.com'
# PASSWORD = 'dataanalysis0621'

# chrome_options = uc.ChromeOptions()

# chrome_options.add_argument("--disable-extensions")

# chrome_options.add_argument("--disable-popup-blocking")

# chrome_options.add_argument("--profile-directory=Default")

# chrome_options.add_argument("--ignore-certificate-errors")

# chrome_options.add_argument("--disable-plugins-discovery")

# chrome_options.add_argument("--incognito")

# chrome_options.add_argument("user_agent=DN")

# driver = uc.Chrome(options=chrome_options)

# driver.delete_all_cookies()

# driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")

# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(GMAIL)
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)

# time.sleep(10)

from selenium import webdriver
# import geckodriver_autoinstaller
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# geckodriver_autoinstaller.install()
# driver= webdriver.Firefox() 
# driver.get("python.org")  

profile = webdriver.FirefoxProfile(
    '/Users/User/AppData/AppData/Roaming/Mozilla/Firefox/Profiles/i2wsr4ej.default-release')

profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

driver = webdriver.Firefox(firefox_profile=profile,
                           desired_capabilities=desired)