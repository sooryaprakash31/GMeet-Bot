from selenium import webdriver
from time import sleep
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
username = config.get('AUTH', 'USERNAME')
password = config.get('AUTH', 'PASSWORD')

class ClassAutomation():
    def __init__(self):
        profile = webdriver.FirefoxProfile('/home/soorya/.mozilla/firefox/2uxqa4qk.Class')
        self.driver = webdriver.Firefox(profile)
        self.driver.get("https://accounts.google.com/")
        sleep(2)
        self.driver.find_element_by_name("identifier").send_keys(username)
        sleep(1)
        self.driver.find_element_by_id("identifierNext").click()
        sleep(3)
        self.driver.find_element_by_name("password").send_keys(password)
        sleep(1)
        self.driver.find_element_by_id("passwordNext").click()
        sleep(2)
        self.driver.get("https://classroom.google.com/")
        sleep(4)
        self.driver.find_element_by_xpath("//div[text()='{}']".format("CS16004-7SemC-DA")).click()
        sleep(10)
        link=self.driver.find_element_by_partial_link_text("https://meet.google.com/lookup/").text
        self.driver.get(link)
        sleep(10)
        self.driver.find_element_by_xpath("//span[text()='Join now']").click()
        
        
ClassAutomation()