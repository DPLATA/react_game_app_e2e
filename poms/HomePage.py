from selenium.webdriver.common.by import By
import poms.Page as page

class HomePage(page.Page):
    
    def __init__(self, browser):
        
        super().__init__(browser)
        self.get_started_btn = browser.find_element(By.XPATH, '//*[@id="Sign-in Button "]')
    
    def click_get_started(self):
        self.get_started_btn.click()

