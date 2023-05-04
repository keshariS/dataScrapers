# fetches metadata from tweet ids
# de-duplicate ALLcat1.csv and fetch metadata and write to cat1_withMetadata.csv
# files should be present in the same folder

import os
import pandas as pd

category = 2

df = pd.read_csv(f"ALLcat{category}.csv")
print(df.shape)
df = df.drop_duplicates(subset=['text'])
print("after removing duplicate tweets:")
print(df.shape)


file = open(f'cat{category}_ids.txt','w')
for i in range(0,df.shape[0]):
    try:
        a = df['edit_history_tweet_ids'][i].split(",")
        b = a[0].strip("'[]'")
        file.write( b + "\n")
    except:
        continue
file.close()


"""
ids = df['id'].to_list()
file = open(f'cat{category}_ids.txt','w')
for id in ids:
    file.write(str(id)+"\n")
file.close()"""

os.system(f"twarc2 hydrate cat{category}_ids.txt cat{category}.json")
os.system(f"twarc2 csv cat{category}.json cat{category}_withMetadata.csv")