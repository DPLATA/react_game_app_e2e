from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from poms.HomePage import HomePageNotSignedIn
from poms.SignInPage import LoginPage
from poms.DashboardPage import DashboardPage
from poms.HallOfFamePage import HallOfFamePageNotSignedIn

# mobile_emulation = { "deviceName": "Galaxy S5" }
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# driver = webdriver.Remote(command_executor='http://localhost:3000/dashboard',desired_capabilities = chrome_options.to_capabilities())

# chrome_options = Options()
# chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
# driver = webdriver.Chrome(service = ser, options = chrome_options)
# driver.get('https://www.google.com')

import unittest

class DeviceCompatibilityTests(unittest.TestCase):
    
    def setUp(self):
        self.service = r"C:\Users\Rafael\Documents\Reesby\Projects\Web scraping\chromedriver.exe"
        self.addr = 'http://localhost:3000'
        self.ser = Service(self.service)
        self.chrome_options = Options()
        
    # def test_random_user_agent(self):
    #     '''
    #     '''
    #     self.ua = UserAgent()
    #     self.userAgent = self.ua.random
        
    #     print(self.userAgent)
        
    #     self.chrome_options.add_argument(f'user-agent={self.userAgent}')
        
    #     # self.chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    #     self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
    #     self.browser.get(self.addr)
        
    #     self.homePageNotSignedIn = HomePageNotSignedIn(self.browser)
    #     self.homePageNotSignedIn.click_get_started()
    #     self.loginPage = LoginPage(self.browser)
    #     self.loginPage.log_in('rsg2703', 'password')
    #     self.dashboardPage = DashboardPage(self.browser)
    #     self.assertIn('dashboard', self.browser.current_url)
    
    def sample_steps(self):
        self.homePageNotSignedIn = HomePageNotSignedIn(self.browser)
        self.homePageNotSignedIn.click_signIn()
        self.loginPage = LoginPage(self.browser)
        self.loginPage.log_in('rsg2703', 'password')
        self.dashboardPage = DashboardPage(self.browser)
        self.dashboardPage.click_logout()
        self.homePageNotSignedIn = HomePageNotSignedIn(self.browser)
        self.homePageNotSignedIn.click_hall_of_fame()
        self.hallOfFamePageNotSignedIn = HallOfFamePageNotSignedIn(self.browser)
        self.assertIn('hof', self.browser.current_url)
        
    def test_1920x1080_window(self):
        self.chrome_options.add_argument('window-size=1920,1080')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
    
    def test_1366x768_window(self):
        self.chrome_options.add_argument('window-size=1366,768')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
    
    def test_360x640_window(self):
        self.chrome_options.add_argument('window-size=360,640')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
        
    def test_414x896_window(self):
        self.chrome_options.add_argument('window-size=414,896')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
        
    def test_1536x864_window(self):
        self.chrome_options.add_argument('window-size=1366,768')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
        
    def test_375x667_window(self):
        self.chrome_options.add_argument('window-size=1366,768')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
    
    def tearDown(self):
        self.browser.quit()
    
if __name__ == "__main__":
        unittest.main()