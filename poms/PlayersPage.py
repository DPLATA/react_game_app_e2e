from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from poms.Page import PageNotSignedIn, PageSignedIn

class PlayersPage():
    
    def __init__(self, browser):
        
        self.reset_search_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/main/section/button')
        self.status_select = Select(self.browser.find_element(By.XPATH, '//*[@id="status-select"]'))
        self.nickname_box = self.browser.find_element(By.XPATH, '//*[@id="nickname-input"]')
        self.submit_btn = self.browser.find_element(By.XPATH, '//*[@id="submit-query-btn"]')
        self.prev_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/main/section/div[1]/button[1]')
        
        
        
        # podría usar find_elements (con *) y .text para identificar los botones
        # self.slot1_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/main/section/div[1]/button[3]')
        # self.slot2_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/main/section/div[1]/button[4]')
        # self.slot3_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/main/section/div[1]/button[5]')
        # self.slot4_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/main/section/div[1]/button[6]')
        # self.slot5_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/main/section/div[1]/button[7]')
        # self.next_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/main/section/div[1]/button[9]')
        
    def click_reset(self):
        self.reset_search_btn.click()
        
    def select_status(self, status):
        '''
        All, oro, plata, bronce
        '''
        self.status_select.select_by_value(status)
        
    def type_nickname(self, nickname):
        self.nickname_box.clear()
        self.nickname_box.send_keys(nickname)
        
    def click_submit(self):
        self.submit_btn.click()
        
    # def click_prev(self):
    #     self.prev_btn.click()
        
    # def click_num(self, slot):
        
    #     self.slot_buttons = [self.slot1_btn, self.slot2_btn, self.slot3_btn,
    #                          self.slot4_btn, self.slot5_btn]
        
    #     self.slot_buttons[slot - 1]()
    
    # def click_next(self):
    #     self.next_btn.click()
        
class PlayersPageNotSignedIn(PageNotSignedIn, PlayersPage):
    
    def __init__(self, browser):
        PageNotSignedIn.__init__(self, browser)
        PlayersPage.__init__(self, browser)

class PlayersPageSignedIn(PageSignedIn, PlayersPage):
    
    def __init__(self, browser):
        PageSignedIn.__init__(self, browser)
        PlayersPage.__init__(self, browser)

