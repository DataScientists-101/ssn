from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import getpass

#credentials
userName='automation2826@gmail.com'
password='India_@123'

options = Options()
##options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-web-security')
options.add_argument("user-data-dir=C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument('--allow-running-insecure-content')

chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"


##options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver_path = "C:/Users/Rajesh Kumar K/Desktop/ssn/chromedriver"
login_url = "https://www.tickertape.in/login"
driver = webdriver.Chrome(chrome_driver_path, options=options)
driver.get(login_url)
wait = WebDriverWait(driver, 20)


wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))).send_keys(userName)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button'))).click()
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(password)























##from selenium import webdriver
##from selenium.webdriver.common.by import By
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.support import expected_conditions as EC
##import time
###import pyautogui as pg
##
##
##username = 'automation2826@gmail.com'
##
##password = 'India_@123'
##
##driver = webdriver.Chrome()
##driver.maximize_window()
##driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
##driver.maximize_window()
##
##
##mail = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierId']"))).send_keys(username)
##
##login = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/span"))).click()
##
##passw = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input"))).send_keys(password)
##
##next = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='passwordNext']/span/span"))).click()
