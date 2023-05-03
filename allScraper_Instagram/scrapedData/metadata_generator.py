"""
usage:
>>>python metadata_generator.py <folder name without quotes>

This file generates a csv file of metadata:
('Name','Date', 'Location','#likes','#comments','caption','hashtags','tagged-users')
from the posts collected by instaloader and placed in a folder

The profile must be already scraped using 'instaloader' and the json files should be extracted in a folder

"""

import json
import datetime
import re
import pandas as pd
import os
import sys

# initialize list of lists
metadata = []
c = 0

# ENTER THE FOLDER name CONTAINING METADATA, ETC..
folder = sys.argv[1]

# assign directory
directory = os.getcwd()
directory = os.path.join(directory, folder)
save_file = os.path.join(directory, f"{folder}.csv")

# iterate over files in that directory
for file in os.listdir(directory):
    if file.endswith('.json'):
        file_path = os.path.join(directory, file)
        file_name = os.path.basename(file_path)
        file = os.path.splitext(file_name)
        name = file[0]
        f = open(file_path, errors='replace')
        data = json.load(f)
        # returns JSON object as a dictionary

        ep = data['node']['taken_at_timestamp']
        date_time = datetime.datetime.fromtimestamp(ep)
    
        try:
            loc = data['node']['location']['name']
        except:
            #print(c,": no location info")
            loc = ""
        
        post_likes = data['node']['edge_media_preview_like']['count']
        post_comments = data['node']['edge_media_to_comment']['count']
    
        try:
            post_caption = data['node']['edge_media_to_caption']['edges'][0]['node']['text']
        except:
            #print(c,": no caption")
            post_caption = ""
        
        hashtgs = re.findall(r"#\w*\b", post_caption)
        usertgs = re.findall(r"@\w*\b", post_caption)

        metadata_i = [name,date_time,loc,post_likes,post_comments,post_caption,hashtgs,usertgs]

        metadata.append(metadata_i)
        c = c+1

print(f"[+] {c} posts processed ...")
# Create the pandas DataFrame
df = pd.DataFrame(metadata, columns=['Name','Date', 'Location','#likes','#comments','caption','hashtags','tagged-users']) 

print(f"Writing to {save_file} ...")
df.to_csv(save_file,index=False)

print("Done!")