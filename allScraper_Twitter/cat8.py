#test for a specific category/keywords for tweets

#cat8 = ['dontvape',  'therealcost']
cat8 = ['musk']

import pandas as pd
import sys
import warnings
warnings.filterwarnings("ignore", 'This pattern is interpreted as a regular expression, and has match groups')

fileNumber = sys.argv[1]

infile = f'/mnt/smdata/twitter/spritzer/scraped_twitter_data{fileNumber}.csv'
#freq = '/mnt/smdata/twitter/VAMoS/spritzer2categories/frequency.csv'
#fcat8 = f'/mnt/smdata/twitter/VAMoS/spritzer2categories/data{fileNumber}_cat8.csv'


df = pd.read_csv(infile)
df = df.drop('withheld',axis=1)

#df1 = pd.read_csv(freq)
print(f"Searching data{fileNumber}.csv for category 8...")

pattern = fr"\b({'|'.join(cat8)})\b"
a = df[df['text'].str.contains(pattern,case=False, na=False)]
print(f"category 8: {a.shape[0]} rows found")
#a.to_csv(fcat8,index=False)
#df1.loc[int(fileNumber), f'cat8'] = a.shape[0]

#df1.to_csv(freq, index=False)
#print("Done! Wrote numbers to frequency.csv")
#print(" ")