import praw
import requests
import cv2
import numpy as np
import os
import pickle
import pandas as pd
import datetime

from utils.create_token import create_token




POST_SEARCH_AMOUNT = 1500 # --------
scale_percent = 10 # percent of original image resolution (for saving the scraped image)------





# Create directory if it doesn't exist to save images
def create_folder(image_path):
    CHECK_FOLDER = os.path.isdir(image_path)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(image_path)

# Path to save images
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path_og = os.path.join(dir_path, "scraped_images/")
ignore_path = os.path.join(dir_path, "ignore_images/")
create_folder(image_path_og)

# Get token file to log into reddit.
# You must enter your....
# client_id - client secret - user_agent - username password
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
else:
    creds = create_token()
    pickle_out = open("token.pickle","wb")
    pickle.dump(creds, pickle_out)

reddit = praw.Reddit(client_id=creds['client_id'],
                    client_secret=creds['client_secret'],
                    user_agent=creds['user_agent'],
                    username=creds['username'],
                    password=creds['password'])




f_final = open("sub_list.csv", "r") # file containing subreddits to scrape from----------

img_notfound = cv2.imread('imageNF.png')

for line in f_final:
    sub = line.strip()
    subreddit = reddit.subreddit(sub)
    image_path = os.path.join(image_path_og, f"raw_images_{sub}/")#----create separate folders for subreddits
    create_folder(image_path)

    posts = []

    print(f"Scraping from subreddit!: {sub}")
    count = 0
    for submission in subreddit.new(limit=POST_SEARCH_AMOUNT):
        posts.append([datetime.datetime.fromtimestamp(submission.created), submission.subreddit, submission.title, submission.selftext])
        """
        if "jpg" in submission.url.lower() or "png" in submission.url.lower():
            try:
                resp = requests.get(submission.url.lower(), stream=True).raw
                image = np.asarray(bytearray(resp.read()), dtype="uint8")
                image = cv2.imdecode(image, cv2.IMREAD_COLOR)

                # Transforms on images: resize, to lower resolution for faster training

                width = int(image.shape[1] * scale_percent / 100)
                height = int(image.shape[0] * scale_percent / 100)
                dim = (width, height)
  
                # resize image
                resized_img = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
                compare_image = cv2.resize(image,(224,224))

                # Get all images to ignore
                for (dirpath, dirnames, filenames) in os.walk(ignore_path):
                    ignore_paths = [os.path.join(dirpath, file) for file in filenames]
                ignore_flag = False

                for ignore in ignore_paths:
                    ignore = cv2.imread(ignore)
                    difference = cv2.subtract(ignore, compare_image)
                    b, g, r = cv2.split(difference)
                    total_difference = cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)
                    if total_difference == 0:
                        ignore_flag = True

                if not ignore_flag:
                    cv2.imwrite(f"{image_path}{sub}-{submission.id}.jpg", resized_img)
                    count += 1
                    
            except Exception as e:
                print(f"Image failed. {submission.url.lower()}")
                print(e)
"""
    df = pd.DataFrame(posts, columns = ['date', 'subreddit', 'title', 'text'])
    df.to_csv('x.csv',index=False)
        