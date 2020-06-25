from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import random
from configparser import ConfigParser
from utils.utils import *

config = ConfigParser()
config.read('config.ini')
username = config.get('AUTH', 'USERNAME')
password = config.get('AUTH', 'PASSWORD')

class ClassAutomation:
     def __init__(self):
          #open Browser - instagram.com
          self.options = Options()
          '''
          Selenium fails if your default profile has many bookmarks and extensions
          Create a new profile and get the paths using chrome://version/
          '''
          #self.options.add_argument("--user-data-dir=/home/soorya/.config/chromium/Profile 1/")
          self.driver = webdriver.Chrome()
          #self.driver.get("https://classroom.google.com/")
          sleep(5)
          self.login()
          self.classroom()
     @operation
     def login(self):
          self.driver.get("https://accounts.google.com/")
          sleep(2)
          #email address
          self.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')[0].send_keys(username)
          sleep(1)
          #next button
          self.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div')[0].click()
          sleep(3)
          self.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')[0].send_keys(password)
          sleep(2)
          self.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div')[0].click()
          sleep(2)
     @operation
     def classroom(self):
          self.driver.get("https://classroom.google.com/")
          sleep(3)
          
ClassAutomation()