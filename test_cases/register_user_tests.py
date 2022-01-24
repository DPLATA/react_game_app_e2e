import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from poms.SignInPage import RegisterPage
import time

class RegisterUserTests(unittest.TestCase):
    
    def setUp(self):
        
        # Initialize browser driver
        self.service = r"C:\Users\Rafael\Documents\Reesby\Projects\Web scraping\chromedriver.exe"
        self.addr = 'http://localhost:3000/sign-in'
        self.ser = Service(self.service)
        self.browser = webdriver.Chrome(service = self.ser)
        
    def test_register_new_user(self):
        '''
        Attempt to register new user (correctly)
        '''
        self.browser.get(self.addr)
        self.registerPage = RegisterPage(self.browser)
        
        # Create unique username based on current timestamp
        self.unique_user = str(time.time())
        self.registerPage.register_user('Test', self.unique_user, 'password')
        
        # Taken to dashboard page if registration is succesful
        self.browser.implicitly_wait(15)
        self.assertIn('dashboard', self.browser.current_url)
        
        
        
    
    # def test_register_user_different_passwords(self):
    #     pass
    
    # def test_no_repeatable_users(self):
    #     pass
        
    def tearDown(self):
        self.browser.quit()
        
if __name__ == "__main__":
        unittest.main()