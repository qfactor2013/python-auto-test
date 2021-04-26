import pyautogui
from selenium import webdriver
import openpyxl

class scraping():

    def __init__(self, keyword=None, site=None):
        self.keyword = keyword
        self.site = site

    def view_print(self):
        print(self.keyword + " : " + self.site)

    def scrap_use_selenium(self):

        driver = webdriver.Chrome()
        
        if self.site == '네이버' :
            url = 'https://www.naver.com'
        elif self.site == '구글' :
            url = 'https://www.google.com'
        elif self.site == '다음' :
            url = 'https://www.daum.net'

        driver.get(url)

    def run(self):
        self.scrap_use_selenium()