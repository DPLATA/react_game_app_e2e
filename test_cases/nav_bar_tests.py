import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from poms.HomePage import HomePageNotSignedIn
from poms.HallOfFamePage import HallOfFamePageNotSignedIn
from poms.AboutPage import AboutPageNotSignedIn
from poms.PlayersPage import PlayersPageNotSignedIn
from poms.SignInPage import LoginPage, RegisterPage
from poms.DashboardPage import DashboardPage

class NavBarTests(unittest.TestCase):
    
    def setUp(self):
        
        # Initialize browser driver
        self.service = r"C:\Users\Rafael\Documents\Reesby\Projects\Web scraping\chromedriver.exe"
        self.addr = 'http://localhost:3000'
        self.ser = Service(self.service)
        self.browser = webdriver.Chrome(service = self.ser)
    
    def test_NavBar_links_not_signed_in(self):
        '''
        Go through every subpage and test that all links from the 
        navigation bar(except its own) work properly
        '''
        
        # List of all pages
        self.pages = [HomePageNotSignedIn, HallOfFamePageNotSignedIn,
                      AboutPageNotSignedIn, PlayersPageNotSignedIn,
                      LoginPage, RegisterPage]
        # List of all addrss sufixes
        self.sub_addresses = ['', 'hof', 'about', 'players',
                              'sign-in', 'sign-in']
        
        for self.PageClass, self.sub_addr in zip(self.pages, self.sub_addresses):
            
            # Go to subpage's address
            self.subpage_addr = os.path.join(self.addr, self.sub_addr)
            self.browser.get(self.subpage_addr)
            # Wait for page to load all elements
            self.browser.implicitly_wait(5)
            
            # Create page object
            self.page = self.PageClass(self.browser)
            
            # Check "home" navigation bar link
            if type(self.page) != HomePageNotSignedIn:
                self.page.click_home()
                self.assertIn(self.addr, self.browser.current_url)
                self.browser.back()
            
            # Check "hall of fame" navigation bar link
            if type(self.page) != HallOfFamePageNotSignedIn:
                self.page.click_hall_of_fame()
                self.assertIn('hof', self.browser.current_url)
                self.browser.back()
            
            # Check "about" navigation bar link
            if type(self.page) != AboutPageNotSignedIn:
                self.page.click_about()
                self.assertIn('about', self.browser.current_url)
                self.browser.back()
            
            # Check players navigation bar link
            if type(self.page) != PlayersPageNotSignedIn:
                self.page.click_players()
                self.assertIn('players', self.browser.current_url)
                self.browser.back()
            
            # Check sign-in navigation bar link
            if (type(self.page) != LoginPage) and (type(self.page) != RegisterPage):
                self.page.click_signIn()
                self.assertIn('sign-in', self.browser.current_url)
                self.browser.back()
            
            # Check Universe Gods navigation bar link
            if type(self.page) != HomePageNotSignedIn:
                self.page.click_univ_gods()
                self.assertIn(self.addr, self.browser.current_url)
                self.browser.back()
            
            # Check globe navigation bar link
            if type(self.page) != HomePageNotSignedIn:
                self.page.click_globe()
                self.assertIn(self.addr, self.browser.current_url)
                self.browser.back()
    
    def test_NavBar_links_signed_in(self):
        '''
        Sign in and test every link from dashboard page, then log out
        '''
        # Log in
        self.subpage_addr = os.path.join(self.addr, 'sign-in')
        self.browser.get(self.subpage_addr)
        self.loginPage = LoginPage(self.browser)
        self.loginPage.log_in('rsg2703', 'password')
        
        # Check Universe Gods logo link
        self.dashboardPage = DashboardPage(self.browser)        
        self.dashboardPage.click_univ_gods()
        self.assertIn(self.addr, self.browser.current_url)
        self.browser.back()
        
        # Check globe link
        self.dashboardPage = DashboardPage(self.browser)
        self.dashboardPage.click_globe()
        self.assertIn(self.addr, self.browser.current_url)
        self.browser.back()
        
        # Check "home" link
        self.dashboardPage = DashboardPage(self.browser)
        self.dashboardPage.click_home()
        self.assertIn(self.addr, self.browser.current_url)
        self.browser.back()
        
        # Check "hall of fame" link
        self.dashboardPage = DashboardPage(self.browser)
        self.dashboardPage.click_hall_of_fame()
        self.assertIn('hof', self.browser.current_url)
        self.browser.back()
        
        # Check "about" link
        self.dashboardPage = DashboardPage(self.browser)        
        self.dashboardPage.click_about()
        self.assertIn('about', self.browser.current_url)
        self.browser.back()
        
        # Check "my hero" link
        self.dashboardPage = DashboardPage(self.browser)        
        self.dashboardPage.click_dashboard()
        self.assertIn('dashboard', self.browser.current_url)
        
        # Check "logout" link
        self.dashboardPage = DashboardPage(self.browser)
        self.dashboardPage.click_logout()
        self.assertIn(self.addr, self.browser.current_url)
        
    
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
        unittest.main()
        