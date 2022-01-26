import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from poms.SignInPage import LoginPage, RegisterPage
from poms.DashboardPage import DashboardPage
import time
import os
import numpy as np
import json

class RegisterUserTests(unittest.TestCase):
    
    def setUp(self):
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
        self.dashboardPage = DashboardPage(self.browser)
        self.assertIn('dashboard', self.browser.current_url)
        
    def test_register_user_different_passwords(self):
        '''
        Attempt to register without passwords matching
        '''
        self.browser.get(self.addr)
        self.registerPage = RegisterPage(self.browser)
        self.unique_user = str(time.time())
        self.registerPage.register_user_diff_passwords('Test', self.unique_user, 'password')
        self.loginPage = LoginPage(self.browser)
        self.assertIn('sign-in', self.browser.current_url)
        
    def test_no_repeatable_users(self):
        '''
        Attempt to register with an already-existing username
        '''
        data_path = r'C:\Users\Rafael\Documents\Projects\Universe Gods\react_game_app_e2e'
        self.user_data1 = json.load(open(os.path.join(data_path, 'MOCK_DATA.json')))
        self.user_data2 = json.load(open(os.path.join(data_path, 'MOCK_DATA-2.json')))
        self.user_data3 = json.load(open(os.path.join(data_path, 'MOCK_DATA-3.json')))
        self.user_data = self.user_data1 + self.user_data2 + self.user_data3
        
        self.browser.get(self.addr)
        self.registerPage = RegisterPage(self.browser)
        
        # Pick a random user
        self.random_pick = np.random.randint(0, len(self.user_data))
        self.nickname = self.user_data[self.random_pick]['nickname']
        self.registerPage.register_user('Test', self.nickname, 'password')
        # self.registerPage = RegisterPage(self.browser)
        self.assertIn('sign-in', self.browser.current_url)
        
    def tearDown(self):
        self.browser.quit()
        
if __name__ == "__main__":
        unittest.main()