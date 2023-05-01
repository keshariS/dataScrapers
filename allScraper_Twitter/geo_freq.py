import pandas as pd

df = pd.read_csv(f"topicModels/iter5_GEO_cat1.csv", engine='python')

for category in range (2,7):
    df1 = pd.read_csv(f"topicModels/iter5_GEO_cat{category}.csv", engine='python')
    df1 = df1.drop(df1.index[0])
    df = pd.concat([df, df1], axis=0)

#print(df.head)
country_counts = df["country"].value_counts()
#print(country_counts)
country_counts.to_csv("topicModels/iter5_GEO_country_freq.csv")
print("Saved country counts")

usa = df.loc[df['country'] == "USA"]
#print(usa)
usa = usa.dropna()
#print(usa)
state_counts = usa["state"].value_counts()
#print(state_counts)
state_counts.to_csv("topicModels/iter5_GEO_state_freq.csv")
print("Saved state counts")