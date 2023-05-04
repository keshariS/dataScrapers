import os

target = "/mnt/smdata/twitter/VAMoS/images/"

for folder in os.listdir(target):
    count = 0
    for file in os.listdir(f"{target}{folder}/"):
        count = count+1
    print(f"{folder}: {count}")
