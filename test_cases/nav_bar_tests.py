import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

from poms.HomePage import HomePage
from poms.HallOfFamePage import HallOfFamePage
from poms.AboutPage import AboutPage
from poms.PlayersPage import PlayersPage
from poms.SignInPage import LoginPage, RegisterPage

class NavBarTests(unittest.TestCase):
    
    def setUp(self):
        
        # Initialize browser driver
        self.service = r"C:\Users\Rafael\Documents\Reesby\Projects\Web scraping\chromedriver.exe"
        self.addr = 'http://localhost:3000'
        
        self.ser = Service(self.service)
        self.browser = webdriver.Chrome(service = self.ser)
        
        # List of all pages
        self.pages = [HomePage, HallOfFamePage, AboutPage,
                      PlayersPage, LoginPage, RegisterPage]
        # List of all addrss sufixes
        self.sub_addresses = ['', 'halloffame', 'about',
                              'players', 'sign-in', 'sign-in']
    
    def test_NavBar_links_OK(self):
        '''
        Go through every subpage and test that all links from the 
        navigation bar(except its own) work properly
        '''
        for PageClass, sub_addr in zip(self.pages, self.sub_addresses):
            
            # Go to subpage's address
            subpage_addr = os.path.join(self.addr, sub_addr)
            self.browser.get(subpage_addr)  
            # Create page object
            page = PageClass(self.browser)
            
            # Check "home" navigation bar link
            if type(page) != HomePage:
                page.click_home()
                self.assertIn(self.addr, self.browser.current_url)
                self.browser.back()
            
            # Check "hall of fame" navigation bar link
            if type(page) != HallOfFamePage:
                page.click_hall_of_fame()
                self.assertIn('halloffame', self.browser.current_url)
                self.browser.back()
            
            # Check "about" navigation bar link
            if type(page) != AboutPage:
                page.click_about()
                self.assertIn('about', self.browser.current_url)
                self.browser.back()
            
            # Check players navigation bar link
            if type(page) != PlayersPage:
                page.click_players()
                self.assertIn('players', self.browser.current_url)
                self.browser.back()
            
            # Check sign-in navigation bar link
            if (type(page) != LoginPage) and (type(page) != RegisterPage):
                page.click_signIn()
                self.assertIn('sign-in', self.browser.current_url)
                self.browser.back()
            
            # Check Universe Gods navigation bar link
            if type(page) != HomePage:
                page.click_univ_gods()
                self.assertIn(self.addr, self.browser.current_url)
                self.browser.back()
            
            # Check globe navigation bar link
            if type(page) != HomePage:
                page.click_globe()
                self.assertIn(self.addr, self.browser.current_url)
                self.browser.back()
        
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
        unittest.main()
        