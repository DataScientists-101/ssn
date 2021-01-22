from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import getpass  

gmailId, passWord = 'automation2826@gmail.com','India_@123'
chrome_driver_path = "C:/Users/Rajesh Kumar K/Desktop/ssn/chromedriver"
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-web-security')
options.add_argument("user-data-dir=C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument('--allow-running-insecure-content')

login_url = "https://www.tickertape.in/login"
driver = webdriver.Chrome(chrome_driver_path, options=options)
driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+'&flowName=GlifWebSignIn&flowEntry = ServiceLogin') 
driver.implicitly_wait(15) 
loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]') 
loginBox.send_keys(gmailId) 

nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]') 
nextButton[0].click() 

passWordBox = driver.find_element_by_xpath( 
    '//*[@id ="password"]/div[1]/div / div[1]/input') 
passWordBox.send_keys(passWord) 

nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]') 
nextButton[0].click() 

print('Login Successful...!!') 


