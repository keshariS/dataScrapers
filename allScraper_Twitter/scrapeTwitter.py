import twint

out_dir = "/mnt/smdata/twitter/VAMoS/" #output directory for the csv files
f = open("all_hashtags.csv", "r")
for line in f:
    h = line.strip("#\n")
    print(f"Scraping: #{h}...")

    c = twint.Config()
    c.Hide_output = True
    c.Search = f"#{h}"
    #c.Limit = 40 # number of tweets to scrape: increments of 20
    c.Output = f"{out_dir}{h}.csv"
    c.Store_csv = True
    c.Count = True

    twint.run.Search(c)
