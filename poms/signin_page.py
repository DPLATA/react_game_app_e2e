# from selenium import webdriver

class SignInPage():

    def __init__(self, browser):
        self.browser = browser
        self.title = self.browser.title
        self.home_button = self.browser.find_element_by_xpath('/html/body/div/nav/div/ul/li[1]/a')
        self.hall_of_fame_button = self.browser.find_element_by_xpath('/html/body/div/nav/div/ul/li[3]/a')
        self.about_button = self.browser.find_element_by_xpath('/html/body/div/nav/div/ul/li[4]/a')
        self.signin_button = self.browser.find_elemnt_by_xpath('/html/body/div/nav/div/ul/li[2]/a')
        self.nickname_text_box = self.browser.find_element_by_name('nickname')
        self.password_text_box = self.browser.find.element_by_name('password')
        self.signin_button = self.browser.find_element_by_xpath('/html/body/div/main/section/form/button')


    def click_home(self):
        self.home_button.click()

    def click_hall_of_fame(self):
        self.hall_of_fame_button.click

    def click_about(self):
        self.about_button.click()

    def click_signin(self):
        self.signin_button.click()

    def type_nickname(self, nickname):
        self.nickname_text_box.send_keys(nickname)

    def type_password(self, password):
        self.password_text_box.send_keys(password)

    def click_signin_button(self):
        self.signin_button.click()