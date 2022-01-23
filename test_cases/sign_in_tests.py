import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

from poms.HomePage import HomePage
from poms.HallOfFamePage import HallOfFamePage
from poms.AboutPage import AboutPage
from poms.PlayersPage import PlayersPage
from poms.SignInPage import LoginPage, RegisterPage

class SignInTests(unittest.TestCase):
    
    def setUp(self):
        
        # Initialize browser driver
        self.service = r"C:\Users\Rafael\Documents\Reesby\Projects\Web scraping\chromedriver.exe"
        self.addr = 'http://localhost:3000'
        
        self.ser = Service(self.service)
        self.browser = webdriver.Chrome(service = self.ser)