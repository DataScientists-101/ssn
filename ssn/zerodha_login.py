from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import getpass

#credentials
userName='SZ9101'
password='Jaya@0610'
_2factor='240297'


options = Options()
##options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-web-security')
##options.add_argument("user-data-dir=C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument('--allow-running-insecure-content')


chrome_driver_path = "C:/Users/Rajesh Kumar K/Desktop/ssn/chromedriver"
driver = webdriver.Chrome(chrome_driver_path, options=options)

#zerodha_login
login_url = "https://kite.zerodha.com"
driver.get(login_url)
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="userid"]'))).send_keys(userName)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(password)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div/form/div[4]/button'))).submit()
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pin"]'))).send_keys(_2factor)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div/form/div[3]/button'))).submit()

#Tickertape_login
home_url = "https://tickertape.in/login"
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
driver.get(home_url)


##wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-container"]/div/div/div/div[3]/div/div/div[1]/button[1]'))).click()
##wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="click-to-continue"]'))).click()
##wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierIsd"]'))).send_keys(userName)
##wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button'))).click()
##wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(password)
##wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button'))).click()
