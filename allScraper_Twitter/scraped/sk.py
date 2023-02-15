import pandas as pd
import os

data = []
n = []
c=0
target = "C:/Users/User/Desktop/scraped/"
htags = f"{target}hashtags/"
for file in os.listdir(htags):
    c=c+1
    f = file.split(".csv")
    df = pd.read_csv(f"{htags}{file}")
    print(f"{f[0]}: {df.shape[0]}")
    data.append(df.shape[0])
    n.append(c)

from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# Plot bar chart with data points
plt.bar(n,data)

# Display the plot
plt.show()