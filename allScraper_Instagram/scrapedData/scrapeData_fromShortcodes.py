# code to strip shortcodes from csv files in post_links
# store in scrapedData by folders
# ------------Run this in the scraped data folder directly, it will automatically create folders----------

from instaloader import Instaloader, Post
import os

in_dir = "post_links" #directory containing .csv files of extracted post-links
dir_path = os.getcwd()
in_dir = os.path.join(dir_path, in_dir)

L = Instaloader()
username = 'versache_123456'
password = 'ut232699'
L.login(username, password)

"""
# Create directory if it doesn't exist to save images
def create_folder(image_path):
    CHECK_FOLDER = os.path.isdir(image_path)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(image_path)
"""

for file in os.listdir(in_dir):
    # get filename and open file
    file_path = os.path.join(in_dir, file)
    file_name = os.path.splitext(file)
    file_name = file_name[0]
    f = open(file_path,"r")
    print(f"[+] Opened {file}...")
    
    # create folder for the corresponding .csv file
    #data = os.path.join(out_dir, f"{file_name}")
    #create_folder(data)

    for line in f:
        p = line.strip("\n")
        p = p.split("https://www.instagram.com/p/")
        shortCode = p[1]
        shortCode = shortCode.strip("/")

        post = Post.from_shortcode(L.context, shortCode)
        L.download_post(post, target = file_name)