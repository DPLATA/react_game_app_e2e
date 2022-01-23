from selenium.webdriver.common.by import By
from poms.Page import PageSignedIn

class EditProfilePage(PageSignedIn):
    '''
    Parent class for both before and after updating user
    (because "back to profile" button changes)
    '''
    def __init__(self, browser):
        
        super().__init__(browser)
        self.name_box = self.browser.find_element(By.XPATH, '//*[@id="update-from"]/input[1]')
        self.nickname_box = self.browser.find_element(By.XPATH, '//*[@id="update-from"]/input[2]')
        self.avatar_btn_1 = self.browser.find_element(By.XPATH, '//*[@id="https://robohash.org/eteosqui.png?size=300x300&set=set1"]')
        self.avatar_btn_2 = self.browser.find_element(By.XPATH, '//*[@id="https://robohash.org/adnesciuntconsequatur.png?size=300x300&set=set1"]')
        self.avatar_btn_3 = self.browser.find_element(By.XPATH, '//*[@id="https://robohash.org/sequisimiliquepraesentium.png?size=300x300&set=set1"]')
        self.avatar_btn_4 = self.browser.find_element(By.XPATH, '//*[@id="https://robohash.org/eamollitiadolores.png?size=300x300&set=set1"]')
        self.avatar_btn_5 = self.browser.find_element(By.XPATH, '//*[@id="https://robohash.org/nihilconsequaturet.png?size=300x300&set=set1"]')
        self.update_btn = self.browser.find_element(By.XPATH, '//*[@id="update-from"]/button')
        
    def type_name(self, name):
        self.name_box.clear()
        self.name_box.send_keys(name)
    
    def type_nickname(self, nickname):
        self.nickname_box.clear()
        self.nickname_box.send_keys(nickname)
        
    def click_avatar(self, avatar_no):        
        self.avatar_buttons = [self.avatar_btn_1.click,
                               self.avatar_btn_2.click,
                               self.avatar_btn_3.click,
                               self.avatar_btn_4.click,
                               self.avatar_btn_5.click]
        
        self.avatar_buttons[avatar_no - 1]()
    
    def click_update(self):
        self.update_btn.click()
        
    def update_user(self, name, nickname, avatar_no):
        self.type_name(name)
        self.type_nickname(nickname)
        self.click_avatar(avatar_no)
        self.click_update()

class UpdateUserPage(EditProfilePage):
    '''
    Update user page must be initialized from dashboard page
    '''
    def __init__(self, browser):
        super().__init__(browser)    
        self.profile_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/main/section/a')
        
    def click_profile(self):
        self.profile_btn.click()
    


class UpdateSuccesfulPage(EditProfilePage):
    '''
    Initialized after updating user
    '''
    def __init__(self, browser):
        
        super().__init__(browser)
        self.profile_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/main/section/a')
    
    def click_profile(self):
        self.profile_btn.click()

# prueba de creacion
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from poms.SignInPage import LoginPage
from poms.DashboardPage import DashboardPage

service = r"C:\Users\Rafael\Documents\Reesby\Projects\Web scraping\chromedriver.exe"
addr = 'http://localhost:3000'
ser = Service(service)
browser = webdriver.Chrome(service = ser)
browser.get('http://localhost:3000/sign-in')

nickname = 'Dolf0'
password = 'BnwizXuDwmP105'

loginPage = LoginPage(browser)
loginPage.log_in(nickname, password)

# wait for page to load
browser.implicitly_wait(10)

dashboardPage = DashboardPage(browser)
dashboardPage.click_update_user()

updateUserPage = UpdateUserPage(browser)

# EL PROFILE BUTTON NO SIRVE DESPUES DE HACER CLICK EN EL UPDATE BUTTON
# updateUserPage.update_user('Alysia', 'Dolf0', 4)
updateUserPage.click_profile()

# updateSuccesfulPage = UpdateSuccesfulPage(browser)

# browser.implicitly_wait(10)
# updateSuccesfulPage.update_user('Alysia', 'Dolf0', 3)

# browser.implicitly_wait(10)
# updateSuccesfulPage.click_profile()



       
        
        