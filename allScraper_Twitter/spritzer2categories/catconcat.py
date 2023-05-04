import pandas as pd
import sys
catNumber = sys.argv[1]

df = pd.read_csv(f'/mnt/smdata/twitter/VAMoS/spritzer2categories/data0_cat{catNumber}.csv')
for n in range (1,466):
    df1 = pd.read_csv(f'/mnt/smdata/twitter/VAMoS/spritzer2categories/data{n}_cat{catNumber}.csv')
    df = pd.concat([df, df1], axis=0)

print(df.head)
df = df['id'].drop_duplicates()

#df.to_csv(f'/mnt/smdata/twitter/VAMoS/ALLcat{catNumber}.csv', index=False)