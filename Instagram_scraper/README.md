The files in this folder are used for scraping images/metadata from instagram for a given list of hashtags.

Scraping Instagram on Oracle cloud:

1. Since Instagram doesn’t have any API, we have to sign in to a fake account and use that for data scraping.
2. Fictitious account created for scraping
3. Selenium was used to scrape all of the 118 unique hashtags.
  For some hashtags (e.g #cbd) there were a lot of posts (>10M) For such hashtags, how many posts do we need to scrape?
  For some hashtags (e.g #blowingclouds) there were a lot of irrelevant posts (e.g posts of actual clouds in the sky)
  For some hashtags (e.g #cannabis) NO post was found. This maybe because instagram has banned such hashtags? (I’m not sure, but no post could be found)
A new list was created called: 'insta_hashtags.csv'

Navigating the repository:

For windows, use: getShortcodes_fromHashtags_win.py (uses selenium in normal mode)
For Linux instance (OCI) use: getShortcodes_fromHashtags_linux.py (uses selenium in headless mode)

Either of these codes scrape the links of the posts that are relevant to the corresponding hashtag
and create csv files under scrapedData/post_links/...


usage of scrapedData/scrapeData_fromShortcodes.py:
Uses the instaloader library : https://instaloader.github.io/module/structures.html
This is the code to strip shortcodes from csv files in scrapedData/post_links/ folder
It creates folders in scrapedData by hashtag name with all the raw metadata. Extract .json.xz files.
(Run this in the scraped data folder directly, it will automatically create folders)


usage of scrapedData/metadata_generator.py:
>>>python metadata_generator.py <folder name without quotes>
This file generates a csv file of metadata:
('Name','Date', 'Location','#likes','#comments','caption','hashtags','tagged-users')
from the posts collected by 'instaloader' library and placed in a folder
The .json.xz files should be extracted and kept in the folder