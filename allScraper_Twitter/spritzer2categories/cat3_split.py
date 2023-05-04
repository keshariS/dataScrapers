cat3a = ['geekvapestore', 'geekup', 'geekvapetech', 'geekfam', 'smokeshop', 'vapelustion', 'vapetime', 'Uwelltech', 'TPE23', 'vapeshop', 'vapestore', 'vapewholesale']  #Store names/brand types/slogans/events
cat3b = ['elfbar', 'geekvape', 'joyetech', 'juul', 'Uwell']  #Store names/brand types/slogans/events
cat = [cat3a, cat3b]
import pandas as pd

infile = f'/mnt/smdata/twitter/VAMoS/finalData/ALLcat3.csv'
df = pd.read_csv(infile)

fcat1 = f'/mnt/smdata/twitter/VAMoS/finalData/ALLcat3a.csv'
fcat2 = f'/mnt/smdata/twitter/VAMoS/finalData/ALLcat3b.csv'
fcat = [fcat1,fcat2]

for i in range(0,2):
    pattern = fr"\b({'|'.join(cat[i])})\b"
    a = df[df['text'].str.contains(pattern,case=False, na=False)]
    print(f"category {i+1}: {a.shape[0]} rows found")
    a.to_csv(fcat[i],index=False)