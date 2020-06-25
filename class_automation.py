from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import random
from configparser import ConfigParser
from utils.utils import *
from datetime import datetime

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
          #self.login()
          self.findClass()
          #self.classroom()
          #self.initClass("CS16008 SNA")
     @operation
     def login(self):
          sleep(2)
          self.driver.get("https://accounts.google.com/")
          sleep(2)
          #email address
          self.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')[0].send_keys(username)
          sleep(2)
          #next button
          self.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div')[0].click()
          sleep(4)
          self.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')[0].send_keys(password)
          sleep(3)
          self.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div')[0].click()
          sleep(3)
     @operation
     def classroom(self):
          self.driver.get("https://classroom.google.com/")
          sleep(10)
          class_text=self.calculateDay()
          self.initClass(class_text)
     
     def findClass(self):
          today=datetime.today().weekday()
          days={0:"Mon",1:"Tue",2:"Wed",3:"Thur",4:"Fri"}
          today=days[today]
          classes_days = { "Mon":["CNS","GTA","RMT"],"Tue":["DA","SNA","CNS"],"Wed":["GTA","RMT","SNA"],"Thur":["SNA","DA","GTA"],"Fri":["RMT","CNS","DA"] }
          classes = { "SNA":"CS16008 SNA","DA":"CS16004 Data Analytics","GTA":"CS16702 - GTA","CNS":"CS16701-CNS","RMT":"SVCE-CSE-IV-C-RMT" }
          classes_time=["09:15","11:30","02:25"]
          while True:
               now = datetime.now()
               timeNow = now.strftime("%I:%M")
               print(timeNow)
               if timeNow in classes_time:
                    class_time=classes_time.index(timeNow)
                    class_name=classes_days[today][class_time]
                    class_text=classes[class_name]
                    self.initClass(class_text)
                    sleep(3600)
               sleep(60)
     @operation
     def initClass(self,class_text):
          self.login()
          sleep(3)
          self.driver.get("https://classroom.google.com/")
          sleep(10)
          self.driver.find_elements_by_xpath("//div[text()='{}']".format(class_text))[0].click()
          sleep(5)
          #self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/span/a/div').click()
          #print(self.driver.find_elements_by_xpath('//*[@id="yDmH0d"]/div[2]/div[3]/div[1]/div/div[2]/div[2]/span'))
          #print(self.driver.find_elements_by_class_name("rbygle NMm5M"))
          for i in self.driver.find_elements_by_xpath("//div[contains(@class, 'QRiHXd')]"):
               if "meet.google.com" in i.text:
                    meet_link = i.text
          self.driver.get(meet_link)
          sleep(5)
ClassAutomation()