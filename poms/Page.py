from selenium.webdriver.common.by import By

# Parent class for all different subpages
class Page():
    
    def __init__(self, browser):
        
        # Selenium browser driver
        self.browser = browser
        # Webpage title
        self.title = self.browser.title
        
        # Common attributes for all subpages
        # Navigation bar logo & globe
        self.navbar_logo = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/a')
        self.navbar_globe = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/a/i')
                
        # Navigation buttons
        self.home_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/nav/div/ul/li[1]/a')
        self.hall_of_fame_btn = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/ul/li[2]/a')
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
        self.hall_of_fame_btn.click()
    
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
        self.dashboard_btn = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/ul/li[5]/a')
        self.logout_btn = self.browser.find_element(By.XPATH, '//*[@id="Sign-in Button "]/button')
        
    def click_dashboard(self):
        self.dashboard_btn.click()
        
    def click_logout(self):
        self.logout_btn.click()
    