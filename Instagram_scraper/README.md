The files in this folder are used for scraping images/metadata from instagram for a given list of hashtags.

# Scraping Instagram on Oracle cloud

Issues:

1. Since Instagram doesn’t have any API, we have to sign in to a fake account and use that for data scraping.
2. Selenium was used to scrape all of the 118 unique hashtags.
3. For some hashtags (e.g #cbd) there were a lot of posts (>10M) However instagram limits the amount of data that can be viewed from a new fake account
4. For some hashtags (e.g #blowingclouds) there were a lot of irrelevant posts (e.g posts of actual clouds in the sky)
5. For some hashtags (e.g #cannabis) NO post was found. This maybe because instagram has banned such hashtags? (I’m not sure, but no post could be found)
6. Hence, a new list was created called: 'insta_hashtags.csv' with 53 out of 118 hashtags

# Scraping Idea

1. Get shortcodes (essentially links) of the posts that are relevant to the corresponding hashtag and create .csv files under scrapedData/00 post_links/..
    or scrapedData/00 new_post_links.. or any other blank folder (same name of folder must be updated in getShortcodes_fromHashtags_win.py)
3. Scrape the actual raw data from the shortcodes using 'instaloader' python library
4. Organize the raw data into a csv file using json library and other python code

Navigating the repository:

# 1. For Windows
use: getShortcodes_fromHashtags_win.py (uses selenium in normal mode) and uses the chromedriver which should be compatible 
with the Chrome browser version: check here for relevant version: https://chromedriver.chromium.org/downloads

>>> $ python getShortcodes_fromHashtags_win.py

# 1. For Linux instance (OCI)
use: getShortcodes_fromHashtags_linux.py (uses selenium in headless mode), no webdriver needed


# 2. usage of scrapedData/scrapeData_fromShortcodes.py:

>>> ~/scrapedData $ python scrapeData_fromShortcodes.py

Uses the instaloader library : https://instaloader.github.io/module/structures.html
This is the code to strip shortcodes from csv files in scrapedData/post_links/.. blank folder (same name of folder must be updated in getShortcodes_fromHashtags_win.py)
It creates folders in scrapedData by hashtag name with all the raw metadata. Extract the .json.xz files in the folder.
(Run this in the scraped data folder directly, it will automatically create folders)


# 3. usage of scrapedData/metadata_generator.py:

>>> ~/scrapedData $ python metadata_generator.py '(insert folder name without quotes)'
  
This file generates a csv file of metadata:
('Name','Date', 'Location','#likes','#comments','caption','hashtags','tagged-users')
from the posts collected by 'instaloader' library and placed in a folder
The .json.xz files should be extracted and kept in the folder


The scraped data can be found on the CML lab's 4TB drive under the NIH VAMoS/instagram/scrapedData folder.

More iterations of data scraping can be done using the process outlined above (create a blank folder scrapedData/02 post_links/.. folder.
