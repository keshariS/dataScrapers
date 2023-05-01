import os
import pandas as pd

category = 5
file = f'/mnt/smdata/twitter/VAMoS/finalData/ALLcat{category}.csv'
df = pd.read_csv(file)
n = df.shape[0]

for i in range(100,103):
    print(df.id[i])
    print(df.text[i])
    os.system(f"twarc2 tweet '{i}' /mnt/smdata/twitter/VAMoS/finalData/cat{category}/cat{category}_{i}.jsonl")
    os.system(f"twarc2 csv /mnt/smdata/twitter/VAMoS/finalData/cat{category}/cat{category}_{i}.jsonl /mnt/smdata/twitter/VAMoS/finalData/cat{category}/cat{category}_{i}.csv")
