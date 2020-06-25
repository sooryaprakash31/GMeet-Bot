from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import random
from configparser import ConfigParser
from utils.utils import *

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
          self.driver.get("https://classroom.google.com/")
          sleep(5)   

ClassAutomation()