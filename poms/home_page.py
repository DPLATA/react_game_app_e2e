# from selenium import webdriver

class HomePage():

    def __init__(self, browser):
        self.browser = browser
        self.title = self.browser.title
        #self.home_button = self.browser.find_element_by_xpath('/html/body/div/nav/div/ul/li[1]/a')
        self.hall_of_fame_button = self.browser.find_element_by_xpath('/html/body/div/nav/div/ul/li[3]/a')
        self.about_button = self.browser.find_element_by_xpath('/html/body/div/nav/div/ul/li[4]/a')
        self.signin_button = self.browser.find_elemnt_by_xpath('/html/body/div/nav/div/ul/li[2]/a')


    # def click_home(self):
    #     self.home_button.click()

    def click_hall_of_fame(self):
        self.hall_of_fame_button.click

    def click_about(self):
        self.about_button.click()

    def click_signin(self):
        self.signin_button.click()
