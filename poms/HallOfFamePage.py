from selenium.webdriver.common.by import By
from poms.Page import PageNotSignedIn, PageSignedIn

class HallOfFamePage():
    
    def __init__(self, browser):
        pass

class HallOfFamePageNotSignedIn(PageNotSignedIn, HallOfFamePage):
    
    def __init__(self, browser):
        PageNotSignedIn.__init__(self, browser)
        HallOfFamePage.__init__(self, browser)

class HallOfFamePageSignedIn(PageSignedIn, HallOfFamePage):
    
    def __init__(self, browser):
        PageSignedIn.__init__(self, browser)
        HallOfFamePage.__init__(self, browser)
