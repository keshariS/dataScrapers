# uses twarc2 to sscrape new data for a given hashtag


import os
import time

"""cat1 = ['boxmod', 'disposablevapepen', 'ecig', 'ecigar', 'ecigarette', 'subohm', 'vapepen', 'vaporizer','elfbar', 'geekvape', 'joyetech', 'juul', 'Uwell'] #Electronic cigarette device names, parts and brand types: pod moved to popular category
cat2 = ['ejuice', 'eliquid', 'premiumliquid', 'vapejuice', 'vapor']  #Smoking substances: cannabis, cbd moved to pop category
cat3 = ['geekvapestore', 'geekup', 'geekvapetech', 'geekfam', 'smokeshop', 'vapelustion', 'vapetime', 'Uwelltech', 'TPE23', 'vapeshop', 'vapestore', 'vapewholesale']  #Store names, events and promotions
cat4 = ['cloudchaser', 'vapebabes', 'vapecommunity', 'vapefam', 'vapefriends', 'vapelover', 'vapenation', 'vaper', 'vapers', 'vapesociety', 'vapingcommunity']  #Vape user names
cat5 = ['vapefun', 'smoke','stopsmokingstartvaping', 'vapeallday', 'vapedaily', 'vapeadvocacy', 'vapelife', 'vapelifestyle', 'vapelove', 'vapelyfe', 'vapeon', 'vapestyle', 'vapingsavedmylife']  #Vape adjectives/actions: vape, vaping moved to pop category
cat6 = ['vapeadores', 'vapear','VapearNoEsFumar','vapeo','vapersmexico']  #Spanish words/associated with Mexico
cat = [cat1,cat2,cat3,cat4,cat5,cat6]

wait = 3 # minutes
limit = 2000

for i in range (3,6):
    for word in cat[i]:
        print(f"Scraping #{word}...")
        os.system(f"twarc2 search '#{word} -is:retweet' {word}.json")
        os.system(f"twarc2 csv {word}.json {word}.csv")

    print(f"Waiting {wait} minutes......")
    time.sleep(60*wait)"""

"""cat_pop = ['cbd','pod']# more popular hashtags: 'cannabis',

cat_pop2 = ['vape','vaping']

wait = 20 # minutes
limit = 10000

for word in cat_pop:
    print(f"Scraping #{word}...")
    os.system(f"twarc2 search --archive --limit {limit} '#{word} -is:retweet' {word}.json")
    os.system(f"twarc2 csv {word}.json {word}.csv")
    print(f"Waiting {wait} minutes......")
    time.sleep(60*wait)"""

print("Done!")

word = 'elfbar'
os.system(f"twarc2 search --archive --limit 1000000 '#{word} -is:retweet' {word}.json")
os.system(f"twarc2 csv {word}.json {word}.csv")