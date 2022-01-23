from selenium.webdriver.common.by import By
from poms.Page import PageSignedIn

class DashboardPage(PageSignedIn):
    '''
    Dashboard page must be initialized from log in page
    '''
    def __init__(self, browser):
        
        super().__init__(browser)
        self.update_btn = self.browser.find_element(By.XPATH, '//*[@id="user-card"]/a')
        
    def click_update_user(self):
        self.update_btn.click()