from selenium.webdriver.common.by import By
import poms.Page as page

class SignInPage(page.Page):
    
    def __init__(self, browser):
        
        super().__init__(browser)
        self.toggle_btn = browser.find_element(By.XPATH, '//*[@id="root"]/main/section/p/button')
        self.submit_btn = browser.find_element(By.XPATH, '//*[@id="root"]/main/section/form/button')
        self.name_box = browser.find_element(By.XPATH, '//*[@id="root"]/main/section/form/input[1]')
        self.nickname_box = browser.find_element(By.XPATH, '//*[@id="root"]/main/section/form/input[2]')
        self.password_box = browser.find_element(By.XPATH, '//*[@id="root"]/main/section/form/input[3]')

