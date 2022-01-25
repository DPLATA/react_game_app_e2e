from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Parent class for all different subpages
class Page():
    
    def __init__(self, browser):
        
        # Selenium browser driver
        self.browser = browser
        # Webpage title
        self.title = self.browser.title
        
        
        # self.page_xpaths = {'navbar_logo': '//*[@id="Navbar"]/div/a',
        #                     'navbar_globe': '//*[@id="Navbar"]/div/a/i',
        #                     'home_btn': '//*[@id="root"]/nav/div/ul/li[1]/a',
        #                     'hof_btn': '//*[@id="Navbar"]/div/ul/li[2]/a',
        #                     'about_btn': '//*[@id="Navbar"]/div/ul/li[3]/a',
        #                     'players_btn': '//*[@id="Navbar"]/div/ul/li[4]/a'}
        
        # WebDriverWait(self.browser, 10).until(
        #     EC.presence_of_all_elements_located(
        #         By.XPATH, list(self.page_xpaths.values())))
        
        # Common attributes for all subpages
        # Navigation bar logo & globe
        self.navbar_logo = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/a')
        self.navbar_globe = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/a/i')
                
        # Navigation buttons
        self.home_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/nav/div/ul/li[1]/a')
        self.hof_btn = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/ul/li[2]/a')
        self.about_btn = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/ul/li[3]/a')
        self.players_btn = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/ul/li[4]/a')
        
    # Methods for clicking all available buttons
    def click_univ_gods(self):
        self.navbar_logo.click()
    
    def click_globe(self):
        self.navbar_globe.click()    

    def click_home(self):
        self.home_btn.click()
    
    def click_hall_of_fame(self):
        self.hof_btn.click()
    
    def click_about(self):
        self.about_btn.click()
        
    def click_players(self):
        self.players_btn.click()

class PageNotSignedIn(Page):
    '''
    Navigation bar buttons specific to when user is not signed in
    '''
    def __init__(self, browser):
        
        super().__init__(browser)
        self.signIn_btn = self.browser.find_element(By.ID, 'Sign-in Button ')
        
    def click_signIn(self):
        self.signIn_btn.click()

class PageSignedIn(Page):
    '''
    Navigation bar buttons specific to when user is signed in
    '''
    def __init__(self, browser):
        
        super().__init__(browser)
        
        self.dashboard_btn = WebDriverWait(self.browser, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="Navbar"]/div/ul/li[5]/a')))
        
        self.logout_btn = self.browser.find_element(By.XPATH, '//*[@id="Sign-in Button "]/button')
        
    def click_dashboard(self):
        self.dashboard_btn.click()
        
    def click_logout(self):
        self.logout_btn.click()
    