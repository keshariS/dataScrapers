#imports here
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

#specify the path to chromedriver.exe (download and save on your computer)
#driver = webdriver.Firefox()
#CHROMEDRIVER_PATH = '/home/ubuntu/dataScrapers/chromedriver_linux64/chromedriver'
options = Options()
options.add_argument('--no-sandbox')
options.add_argument("--headless")
options.add_argument('--disable-dev-shm-usage')

#driver = webdriver.Chrome(CHROMEDRIVER_PATH, options = options) # deprecated in selenium > v4, executable file not needed
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#open the webpage
driver.get("http://www.instagram.com")
print("sk")
driver.close()