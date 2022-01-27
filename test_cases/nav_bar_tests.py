import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from poms.HomePage import HomePageNotSignedIn, HomePageSignedIn
from poms.HallOfFamePage import HallOfFamePageNotSignedIn
from poms.AboutPage import AboutPageNotSignedIn
from poms.PlayersPage import PlayersPageNotSignedIn
from poms.SignInPage import LoginPage, RegisterPage
from poms.DashboardPage import DashboardPage

class NavBarTests(unittest.TestCase):
    
    def setUp(self):
        self.service = r"C:\Users\Rafael\Documents\Reesby\Projects\Web scraping\chromedriver.exe"
        self.addr = 'http://localhost:3000'
        self.ser = Service(self.service)
        self.browser = webdriver.Chrome(service = self.ser)
    
    def test_univ_gods_logo_link(self):
        '''
        Universe Gods logo takes user to homepage
        '''
        self.browser.get(os.path.join(self.addr, 'sign-in'))
        self.page = LoginPage(self.browser)
        self.page.click_univ_gods()
        self.assertIn('http://localhost:3000', self.browser.current_url)
    
    def test_globe_icon_link(self):
        '''
        Globe icon takes user to homepage
        '''
        self.browser.get(os.path.join(self.addr, 'sign-in'))
        self.page = LoginPage(self.browser)
        self.page.click_globe()
        self.assertIn('http://localhost:3000', self.browser.current_url)
    
    def test_home_link(self):
        '''
        Home button works correctly
        '''
        self.browser.get(os.path.join(self.addr, 'sign-in'))
        self.page = LoginPage(self.browser)
        self.page.click_home()
        self.assertIn('http://localhost:3000', self.browser.current_url)
    
    def test_hall_of_fame_link(self):
        '''
        Hall of fame button works correctly
        '''
        self.browser.get(self.addr)
        self.page = HomePageNotSignedIn(self.browser)
        self.page.click_hall_of_fame()
        self.assertIn('hof', self.browser.current_url)
    
    def test_about_link(self):
        '''
        About button works correctly
        '''
        self.browser.get(self.addr)
        self.page = HomePageNotSignedIn(self.browser)
        self.page.click_about()
        self.assertIn('about', self.browser.current_url)
    
    def test_players_link(self):
        '''
        Players link works correctly
        '''
        self.browser.get(self.addr)
        self.page = HomePageNotSignedIn(self.browser)
        self.page.click_players()
        self.assertIn('players', self.browser.current_url)
    
    def test_sign_in_link(self):
        '''
        Sign-in button works correctly
        '''
        self.browser.get(self.addr)
        self.page = HomePageNotSignedIn(self.browser)
        self.page.click_signIn()
        self.assertIn('sign-in', self.browser.current_url)
        
    def test_dashboard_link(self):
        '''
        My Hero button works correctly
        '''
        self.browser.get(self.addr)
        self.page = HomePageNotSignedIn(self.browser)
        self.page.click_signIn()
        self.page = LoginPage(self.browser)
        self.page.log_in('rsg2703', 'password')
        self.page = DashboardPage(self.browser)
        self.page.click_home()
        self.page = HomePageSignedIn(self.browser)
        self.page.click_dashboard()
        self.assertIn('dashboard', self.browser.current_url)
        
    def test_logout_link(self):
        '''
        Logout button works correctly
        '''
        self.browser.get(self.addr)
        self.page = HomePageNotSignedIn(self.browser)
        self.page.click_signIn()
        self.page = LoginPage(self.browser)
        self.page.log_in('rsg2703', 'password')
        self.page = DashboardPage(self.browser)
        self.page.click_logout()
        self.assertIn('http://localhost:3000', self.browser.current_url)
    
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
        unittest.main()
        