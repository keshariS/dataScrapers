# categories of hashtags created:
cat1 = ['boxmod', 'disposablevapepen', 'ecig', 'ecigar', 'ecigarette', 'pod', 'subohm', 'vapepen', 'vaporizer'] #Electronic cigarette device names and parts
cat2 = ['cannabis', 'cbd', 'ejuice', 'eliquid', 'premiumliquid', 'vapejuice', 'vapor']  #Smoking substances
cat3 = ['geekvapestore', 'geekup', 'geekvapetech', 'geekfam', 'elfbar', 'geekvape', 'joyetech', 'juul', 'smokeshop', 'vapelustion', 'vapetime', 'Uwell', 'Uwelltech', 'TPE23', 'vapeshop', 'vapestore', 'vapewholesale']  #Store names/brand types/slogans/events
cat4 = ['cloudchaser', 'vapebabes', 'vapecommunity', 'vapefam', 'vapefriends', 'vapelover', 'vapenation', 'vaper', 'vapers', 'vapesociety', 'vapingcommunity']  #Vape user names
cat5 = ['vapefun', 'smoke','stopsmokingstartvaping', 'vape', 'vapeallday', 'vapedaily', 'vapeadvocacy', 'vapelife', 'vapelifestyle', 'vapelove', 'vapelyfe', 'vapeon', 'vaping', 'vapestyle', 'vapingsavedmylife']  #Vape adjectives/actions
cat6 = ['vapeadores', 'vapear','VapearNoEsFumar','vapeo','vapersmexico']  #Spanish words/associated with Mexico
cat7 = ['vapephoto','vapephotography','vapepics','vapestagram','instavape']  #Vape Social media
cat = [cat1,cat2,cat3,cat4,cat5,cat6,cat7]


import pandas as pd
import sys
import warnings
warnings.filterwarnings("ignore", 'This pattern is interpreted as a regular expression, and has match groups')

fileNumber = sys.argv[1]

infile = f'/mnt/smdata/twitter/spritzer/scraped_twitter_data{fileNumber}.csv'
freq = '/mnt/smdata/twitter/VAMoS/spritzer2categories/frequency.csv'
fcat1 = f'/mnt/smdata/twitter/VAMoS/spritzer2categories/data{fileNumber}_cat1.csv'
fcat2 = f'/mnt/smdata/twitter/VAMoS/spritzer2categories/data{fileNumber}_cat2.csv'
fcat3 = f'/mnt/smdata/twitter/VAMoS/spritzer2categories/data{fileNumber}_cat3.csv'
fcat4 = f'/mnt/smdata/twitter/VAMoS/spritzer2categories/data{fileNumber}_cat4.csv'
fcat5 = f'/mnt/smdata/twitter/VAMoS/spritzer2categories/data{fileNumber}_cat5.csv'
fcat6 = f'/mnt/smdata/twitter/VAMoS/spritzer2categories/data{fileNumber}_cat6.csv'
fcat7 = f'/mnt/smdata/twitter/VAMoS/spritzer2categories/data{fileNumber}_cat7.csv'
fcat = [fcat1,fcat2,fcat3,fcat4,fcat5,fcat6,fcat7]

df = pd.read_csv(infile)
df = df.drop('withheld',axis=1)

df1 = pd.read_csv(freq)
print(f"Searching data{fileNumber}.csv for categories...")
for i in range(0,7):
    pattern = fr"\b({'|'.join(cat[i])})\b"
    a = df[df['text'].str.contains(pattern,case=False, na=False)]
    print(f"category {i+1}: {a.shape[0]} rows found")
    a.to_csv(fcat[i],index=False)
    df1.loc[int(fileNumber), f'cat{i+1}'] = a.shape[0]

df1.to_csv(freq, index=False)
print("Done! Wrote numbers to frequency.csv")
print(" ")