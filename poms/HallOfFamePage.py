from selenium.webdriver.common.by import By
from poms.Page import PageNotSignedIn, PageSignedIn

class HallOfFamePage():
    
    def __init__(self, browser):
        pass

class HallOfFamePageNotSignedIn(PageNotSignedIn, HallOfFamePage):
    
    def __init__(self, browser):
        PageNotSignedIn.__init__(self, browser)
        HallOfFamePage.__init__(self, browser)

class HallOfFamePageSignedIn(PageSignedIn, HallOfFamePage):
    
    def __init__(self, browser):
        PageSignedIn.__init__(self, browser)
        HallOfFamePage.__init__(self, browser)

# # %%

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# from poms.SignInPage import LoginPage
# from poms.DashboardPage import DashboardPage

# service = r"C:\Users\Rafael\Documents\Reesby\Projects\Web scraping\chromedriver.exe"
# addr = 'http://localhost:3000/hof'
# ser = Service(service)
# browser = webdriver.Chrome(service = ser)
# browser.get(addr)

# hallOfFamePageNotSignedIn = HallOfFamePageNotSignedIn(browser)
# hallOfFamePageNotSignedIn.click_signIn()

# loginPage = LoginPage(browser)
# nickname = 'Dolf0'
# password = 'BnwizXuDwmP105'
# loginPage.log_in(nickname, password)

# # wait for page to load
# browser.implicitly_wait(10)

# dashboardPage = DashboardPage(browser)
# dashboardPage.click_hall_of_fame()

# # wait for page to load
# browser.implicitly_wait(10)

# hallOfFamePageSignedIn = HallOfFamePageSignedIn(browser)

# hallOfFamePageSignedIn.click_dashboard()
