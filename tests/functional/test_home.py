# -*- coding: utf-8 -*-
"""
    tests.functional/test_home
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Basic check that home page works
"""
from selenium import webdriver
import unittest

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        self.browser.get('http://localhost:5000')
        self.assertIn('PyLit6', self.browser.title)

if __name__ == '__main__':
    unittest.main()
