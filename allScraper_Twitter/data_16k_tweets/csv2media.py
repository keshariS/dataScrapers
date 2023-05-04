import os
import pandas as pd
import wget

# Create directory if it doesn't exist to save data
def create_folder(image_path):
    CHECK_FOLDER = os.path.isdir(image_path)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(image_path)

#target = "scraped1/" # folder containing all csv files
target = "/mnt/smdata/twitter/VAMoS/"

htags = f"{target}hashtags/"
imgs = f"{target}images/"

#read each file and create respective folder
fcnt = 0
imcnt = 0
for file in os.listdir(htags):
    fcnt = fcnt +1
    #print(file)
    df = pd.read_csv(f"{htags}{file}")
    folder = file.split(".csv")
    folder = folder[0]
    create_folder(os.path.join(imgs, folder))
    
    photos = df.photos
    print(f"[{fcnt}] Downloading images to {folder}/...")
    count = 0
    for pics in photos:
        pics = pics.strip("[]")
        pics = pics.split(',')
        for pic in pics:
            pic = pic.strip(" '")
            if(pic!=""):
                #print(pic)
                count = count +1
                try:
                    wget.download(pic, out = f"{imgs}{folder}/", bar = None) # visit each link and download to respective folder
                except:
                    continue
    print(f"[-] {count} images downloaded.")
    imcnt = imcnt + count
print(f"[-] Total images downloaded: {imcnt}")
