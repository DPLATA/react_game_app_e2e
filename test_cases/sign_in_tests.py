import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import json
import numpy as np
from poms.SignInPage import LoginPage
from poms.DashboardPage import DashboardPage

class SignInTests(unittest.TestCase):
    
    def setUp(self):
        
        # Initialize browser driver
        self.service = r"C:\Users\Rafael\Documents\Reesby\Projects\Web scraping\chromedriver.exe"
        self.addr = 'http://localhost:3000/sign-in'
        self.ser = Service(self.service)
        self.browser = webdriver.Chrome(service = self.ser)
        
    def test_sign_in_no_data(self):
        '''
        Attempt to sign-in without username
        '''
        self.browser.get(self.addr)
        self.loginPage = LoginPage(self.browser)
        self.loginPage.log_in('', 'password')
        self.assertIn('sign-in', self.browser.current_url)
        
        '''
        Attempt to sign-in without password
        '''
        self.browser.get(self.addr)
        self.loginPage = LoginPage(self.browser)
        self.loginPage.log_in('Dolf0', '')
        self.assertIn('sign-in', self.browser.current_url)    
        
        '''
        Attempt to sign-in without username nor password
        '''
        self.browser.get(self.addr)
        self.loginPage = LoginPage(self.browser)
        self.loginPage.log_in('', '')
        self.assertIn('sign-in', self.browser.current_url)
    
    def test_correct_sign_in(self):
        '''
        Pick random users and log in
        '''
        # Load user data
        data_path = r'C:\Users\Rafael\Documents\Projects\Universe Gods\react_game_app_e2e'
        self.user_data1 = json.load(open(os.path.join(data_path, 'MOCK_DATA.json')))
        self.user_data2 = json.load(open(os.path.join(data_path, 'MOCK_DATA-2.json')))
        self.user_data3 = json.load(open(os.path.join(data_path, 'MOCK_DATA-3.json')))
        self.user_data = self.user_data1 + self.user_data2 + self.user_data3
        
        # Pick several random users
        self.random_picks = np.random.randint(0, len(self.user_data), size = 20)
        self.users = [self.user_data[n] for n in self.random_picks]
        
        # Attempt log in with every user's username and password
        for user in self.users:
            username = user['nickname']
            password = user['password']
            
            self.browser.get(self.addr)
            self.loginPage = LoginPage(self.browser)
            self.loginPage.log_in(username, password)
            self.dashboardpage = DashboardPage(self.browser)
            self.assertIn('dashboard', self.browser.current_url)
    
    def tearDown(self):
        self.browser.quit()
        
if __name__ == "__main__":
        unittest.main()