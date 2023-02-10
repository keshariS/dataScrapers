import os
import pandas as pd
import wget

# Create directory if it doesn't exist to save data
def create_folder(image_path):
    CHECK_FOLDER = os.path.isdir(image_path)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(image_path)

target = "scraped1/" # folder containing all csv files
htags = f"{target}hashtags/"
imgs = f"{target}images/"
#read each file and create respective folder

####--------modifyyyy with folders::::
for file in os.listdir(htags):
    print(file)
    df = pd.read_csv(f"{htags}{file}")
    folder = file.strip(".csv")
    create_folder(os.path.join(imgs, folder))
    
    photos = df.photos
    print(f"[+] Downloading images to {folder}/...")
    count = 0
    for pics in photos:
        pics = pics.strip("[]")
        pics = pics.split(',')
        for pic in pics:
            pic = pic.strip(" '")
            if(pic!=""):
                #print(pic)
                count = count +1
                wget.download(pic, out = f"{imgs}{folder}/", bar = None) # visit each link and download to respective folder
    print(f"[-] {count} images downloaded.")
