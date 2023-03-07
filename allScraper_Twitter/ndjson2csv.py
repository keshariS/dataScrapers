import ndjson, json
import csv
import sys

fileNumber = sys.argv[1]

ndJsonFile = []
infile = f'/mnt/smdata/twitter/spritzer/scraped_twitter_data{fileNumber}.ndjson'
outfile = infile.split('.ndjson')
outfile = outfile[0] + '.csv'

with open(infile) as f:
    currLine = f.readline()
    while (currLine != "") :
        ndJsonFile.append(currLine)
        currLine = f.readline()

keys = set()
print(f"Converting from [...{fileNumber}.ndjson] to [...{fileNumber}.csv] ...")
for ndj_elem in ndJsonFile:
    try:
        ndj_elem = json.loads(ndj_elem)
        for key in ndj_elem.keys():
            keys.add(key)
    except:
        pass

keys = sorted(keys)
print("Done! Writing to csv...")
with open(outfile,'w') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=',')
        csvWriter.writerow(keys)
        for ndj_elem in ndJsonFile:
                try:
                    ndj_elem = json.loads(ndj_elem)
                    for key in keys:
                        if key not in ndj_elem:
                            ndj_elem[key]=""
                    csvWriter.writerow([ndj_elem[key] for key in keys])
                except:
                    pass
print("Done!")