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

import numpy as np
import pandas as pd
f = open("test_hashtags.csv", "r") # input file containing list of hashtags
out_dir = "/mnt/smdata/instagram/scrapedData/post_links/" # output directory for the scraped .csv files


options = Options()
options.add_argument('--no-sandbox')
options.add_argument("--headless")
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#driver.get("https://www.google.com")
#print(driver.title)
#driver.close()


#open the webpage
driver.get("http://www.instagram.com")
print("[+] Opened Instagram")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
user = "sonchirayi"
username.send_keys(user)
password.clear()
password.send_keys("instagramak@80")
time.sleep(5)
#target the login button and click it
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
print(f"[+] Logging into Instagram (username: {user})...")

# handle alerts
time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
print("[+] Logged in!")
print("[+] 1st popup clicked")
time.sleep(5)
#alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
#print("2nd popup clicked")


STOP_AT = 1 # stop at this number of hashtags
count = 0
for line in f:
    h = line.strip("#\n")
    count = count + 1
    print(f"[{count}] Scraping keyword: #{h}...")
    out_file = f"{out_dir}{h}.csv"


    # search for a certain hashtag
    time.sleep(5)
    print("    [+] Targetting the searchbox for keyword...")
    button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@aria-label='Search']"))).click()

    #target the search input field
    searchbox = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    searchbox.clear()

    #search for the hashtag
    keyword = f"#{h}"
    searchbox.send_keys(keyword)

    #FIXING THE DOUBLE ENTER
    time.sleep(5)  # Wait for 5 seconds
    my_link = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
    my_link.click()

    print("    [+] Waiting for page to load...")
    time.sleep(25)

    #increase the range to scroll more
    n_scrolls = 4
    print("    [+] Scrolling...")
    for j in range(0, n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(25)

    #target all the link elements on the page
    anchors = driver.find_elements(By.TAG_NAME,'a')
    anchors = [a.get_attribute('href') for a in anchors]
    #narrow down all links to image links only
    anchors = [a for a in anchors if str(
        a).startswith("https://www.instagram.com/p/")]

    print('    [+] Found ' + str(len(anchors)) + ' links to posts')

    df = pd.DataFrame(np.array(anchors))
    print("    [+] Writing to csv...")
    df.to_csv(out_file, header = None, index=False)
    print("    [-] Done!")
    if(count==STOP_AT):
        break

driver.close()


"""
# search for a certain hashtag
#target the search button and click it
print("[+] Targetting the searchbox for keyword...")
button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-label='Search']"))).click()

#target the search input field
searchbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
#searchbox = EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))
searchbox.clear()

#search for the hashtag cat
keyword = "#cat"
searchbox.send_keys(keyword)
print(f"[INFO] Searching for {keyword}...")
 
#FIXING THE DOUBLE ENTER
time.sleep(5) # Wait for 5 seconds
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()

print("[+] Waiting for page to load...")
time.sleep(25)

#increase the range to sroll more
n_scrolls = 4
print("[+] Scrolling...")
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(20)

#target all the link elements on the page
anchors = driver.find_elements(By.TAG_NAME,'a')
anchors = [a.get_attribute('href') for a in anchors]
#narrow down all links to image links only
anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

print('Found ' + str(len(anchors)) + ' links to posts')
print(anchors[:5])

driver.close()
"""