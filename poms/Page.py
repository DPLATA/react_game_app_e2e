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
        self.navbar_logo = self.browser.find_element(By.XPATH, '//*[@id="root"]/nav/div/a')
        self.navbar_globe = self.browser.find_element(By.XPATH, '//*[@id="root"]/nav/div/a[1]/i')
        
        # Navigation buttons
        self.home_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/nav/div/ul/li[1]/a')
        self.hall_of_fame_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/nav/div/ul/li[3]/a')
        self.about_btn = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/ul/li[3]/a')
        self.signIn_btn = self.browser.find_element(By.ID, 'Sign-in Button ')
      
    # Methods for clicking all available buttons
    def click_home(self):
        self.home_btn.click()
    
    def click_hall_of_fame(self):
        self.hall_of_fame_btn.click()
    
    def click_about(self):
        self.about_btn.click()
    
    def click_signIn(self):
        self.signIn_btn.click()
    
    def click_univ_gods(self):
        self.navbar_logo.click()
    
    def click_globe(self):
        self.navbar_globe.click()