import re
import numpy as np
import pandas as pd

with open("insta_hashtags.txt") as f:
    data = f.read()
hshtgs = re.findall(r"#\w*\b", data)
print(len(hshtgs))
hshtgs = np.unique(np.array(hshtgs))
print(hshtgs.shape)

df = pd.DataFrame(hshtgs)
df.to_csv("insta_hashtags.csv", header = None, index=False)