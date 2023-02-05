#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

#specify the path to chromedriver.exe (download and save on your computer)
#driver = webdriver.Firefox()
driver = webdriver.Chrome('C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe')

#open the webpage
driver.get("http://www.instagram.com")


#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("versache_123456")
password.clear()
password.send_keys("ut232699")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!

# handle alerts
time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# search for a certain hashtag
#target the search button and click it
button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-label='Search']"))).click()

#target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

#search for the hashtag cat
keyword = "#cat"
searchbox.send_keys(keyword)
 
#FIXING THE DOUBLE ENTER
time.sleep(5) # Wait for 5 seconds
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()



#increase the range to sroll more
n_scrolls = 0
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)

#target all the link elements on the page
anchors = driver.find_elements_by_tag_name('a')
anchors = [a.get_attribute('href') for a in anchors]
#narrow down all links to image links only
anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

print('Found ' + str(len(anchors)) + ' links to posts')
print(anchors[:5])

