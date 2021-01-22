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
##options.add_argument('--user-data-dir')
options.add_argument("user-data-dir=C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument('--allow-running-insecure-content')


chrome_driver_path = "C:/Users/Rajesh Kumar K/Desktop/ssn/chromedriver"
login_url = "https://www.tickertape.in/login"
driver = webdriver.Chrome(chrome_driver_path, options=options)
driver.get(login_url)
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-container"]/div/div/div/div[3]/div/div/div[1]/button[1]'))).click()
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="click-to-continue"]'))).click()

##wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierIsd"]'))).send_keys(userName)
##wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button'))).click()
##wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(password)
##wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button'))).click()




