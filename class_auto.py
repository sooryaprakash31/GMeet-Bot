from selenium import webdriver
from time import sleep
from configparser import ConfigParser
from datetime import datetime
import schedule
import csv

config = ConfigParser()
config.read('config.ini')
username = config.get('AUTH', 'USERNAME')
password = config.get('AUTH', 'PASSWORD')

classTime = ["09:15","11:35","14:20"]

class ClassAutomation():
    def __init__(self):
        self.count = 0
        self.findCount()
        schedule.every().day.at(classTime[self.count]).do(self.initClass)
        while True:
            schedule.run_pending()
            sleep(1)

    def findCount(self):
        currentTime=datetime.now().strftime("%H:%M")
        currentHour = currentTime.split(":")[0]
        for i in classTime:
            if int(currentHour)<int(i.split(":")[0]):
                self.count = classTime.index(i)
            
    def initClass(self):
        self.login()
        className = self.findClass()
        self.driver.find_element_by_xpath("//div[text()='{}']".format(className)).click()
        sleep(10)
        link=self.driver.find_element_by_partial_link_text("https://meet.google.com/lookup/").text
        self.driver.get(link)
        sleep(10)
        self.driver.find_element_by_xpath("//span[text()='Join now']").click()
        sleep(60*60)
        self.driver.quit()
        if self.count < 2:
            self.count = self.count + 1
        else:
            self.count = 0

    def findClass(self):
        with open("schedule.csv","r") as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                if row["Day"]== datetime.now().strftime("%a"):
                    return row[classTime[self.count]]

    def login(self):    
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
        sleep(5)
        
ClassAutomation()