from selenium.webdriver.common.by import By
from poms.Page import PageNotSignedIn, PageSignedIn

class HomePage():
    
    def __init__(self, browser):

        self.get_started_btn = browser.find_element(By.XPATH, '//*[@id="Sign-in Button "]')
    
    def click_get_started(self):
        self.get_started_btn.click()

class HomePageNotSignedIn(PageNotSignedIn, HomePage):
    
    def __init__(self, browser):
        PageNotSignedIn.__init__(self, browser)
        HomePage.__init__(self, browser)

class HomePageSignedIn(PageSignedIn, HomePage):
    
    def __init__(self, browser):
        PageSignedIn.__init__(self, browser)
        HomePage.__init__(self, browser)

# # %%
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# from poms.SignInPage import LoginPage
# from poms.DashboardPage import DashboardPage

# service = r"C:\Users\Rafael\Documents\Reesby\Projects\Web scraping\chromedriver.exe"
# addr = 'http://localhost:3000'
# ser = Service(service)
# browser = webdriver.Chrome(service = ser)
# browser.get('http://localhost:3000/')

# homePageNotSignedIn = HomePageNotSignedIn(browser)
# homePageNotSignedIn.click_get_started()


# browser.back()
# homePageNotSignedIn.click_signIn()