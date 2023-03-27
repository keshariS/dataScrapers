#download all files in the given range from the server, convert from ndjson to csv, and search and divide into categories

import os

for n in range(466,500):
    os.system(f"scp -i twitter-private.key opc@193.122.142.7:/mnt/store/twitterscrape/scraped_twitter_data{n}.ndjson /mnt/smdata/twitter/spritzer/")
    os.system(f"python3 ndjson2csv.py {n}")
    os.system(f"python3 data2categories.py {n}")