from selenium import webdriver
import os

ip = 'http://115.230.246.102:8118'
chromedriver = 'C:\\Users\\bxm\AppData\Local\Programs\Python\Python36\chromedriver.exe'
chome_options = webdriver.ChromeOptions()  
chome_options.add_argument('--proxy-server=http://115.230.246.102:8118')
os.environ["webdriver.chrome.driver"] = chromedriver  
driver = webdriver.Chrome(chromedriver, chrome_options=chome_options)
driver.get('http://httpbin.org/ip')