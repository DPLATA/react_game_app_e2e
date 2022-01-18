import unittest
from selenium import webdriver

class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        self.firefox_options = webdriver.FirefoxOptions()
        self.firefox_options.headless = False
        self.browser = webdriver.Firefox(options=self.firefox_options)

    def test_validate_google_search(self):
        browser = self.browser
        browser.get("http://localhost:3000/")
        self.assertIn("React App", browser.title)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
        unittest.main()