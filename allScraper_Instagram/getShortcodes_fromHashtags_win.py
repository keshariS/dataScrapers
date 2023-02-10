#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import numpy as np
import pandas as pd

f = open("test_hashtags.csv", "r") # input file containing list of hashtags
out_dir = "post_links/" # output directory for the scraped .csv files


#specify the path to chromedriver.exe (download and save on your computer)
#driver = webdriver.Firefox()
driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

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
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!

# handle alerts
time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()



count = 0
for line in f:
    h = line.strip("#\n")
    count = count + 1
    print(f"[{count}] Scraping keyword: #{h}...")
    out_file = f"{out_dir}{h}.csv"


    # search for a certain hashtag
    print("[+] Targetting the searchbox for keyword...")
    button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@aria-label='Search']"))).click()

    #target the search input field
    searchbox = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    searchbox.clear()

    #search for the hashtag cat
    keyword = f"#{h}"
    searchbox.send_keys(keyword)

    #FIXING THE DOUBLE ENTER
    time.sleep(5)  # Wait for 5 seconds
    my_link = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
    my_link.click()

    print("[+] Waiting for page to load...")
    time.sleep(25)



    #increase the range to scroll more
    n_scrolls = 1
    print("[+] Scrolling...")
    for j in range(0, n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(25)

    #target all the link elements on the page
    anchors = driver.find_elements_by_tag_name('a')
    anchors = [a.get_attribute('href') for a in anchors]
    #narrow down all links to image links only
    anchors = [a for a in anchors if str(
        a).startswith("https://www.instagram.com/p/")]

    print('[+] Found ' + str(len(anchors)) + ' links to posts')

    df = pd.DataFrame(np.array(anchors))
    print("[+] Writing to csv...")
    df.to_csv(out_file, header = None, index=False)
    print("[-] Done!")

driver.close()
