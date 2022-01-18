import unittest
from selenium import webdriver
import poms.home_page as home_page
import poms.signin_page as signin_page

class SimpleTestCase(unittest.TestCase):

    # def __init__(self):
    def setUp(self):
        self.firefox_options = webdriver.FirefoxOptions()
        self.firefox_options.headless = False
        self.browser = webdriver.Firefox(options=self.firefox_options)
        self.home_page = home_page.HomePage(self.browser)
        self.signin_page = signin_page.SignInPage(self.browser)
        print('Init test case')
        browser = self.browser
        browser.get("http://localhost:3000/")


    def test_sign_in(self):
        # dar click en signin
        self.home_page.click_signin()
        # poner tu usuario
        self.signin_page.type_nickname('usuarioprueba1')
        # poner tu contraseña
        self.signin_page.type_password('contraseñapruebauno')
        # dar click en sign in
        self.signin_page.click_signin_button()
        # 
        self.assertIn("React App", self.browser.title)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
        unittest.main()