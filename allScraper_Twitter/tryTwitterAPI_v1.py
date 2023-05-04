import tweepy

# API keys that yous saved earlier
api_key = "5eRNfxQac10gulNMV5x2Bpd6R"
api_secrets = "NI0sivJCi1YU1dSlxJhlwPkr2vcZmhDPe9tsZR3VBZtrjDoRsn"
access_token = "24355706-2V9PfUtoWh4ie5wDjeFb7SMlfqo8vw1GGzdBz9x3F"
access_secret = "F2K9K97DgFpvtytSth876I2HISMqIl2iSQfb1tkyQmcTL"


# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)
 
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

q = ' OR '.join(abc)


"""
id = '1593590803347263489' # tweet ID
tweet = api.get_status(id)
user = api.get_user(id)
location = user.location

# Get tweet data
print(f'Created at:{tweet.created_at}')
print(f'Tweet id:{tweet.id}')
 
# Get tweet text
try:
    print(f'Tweet text:{tweet.text}')
except:
    # Get tweet text in extended mode
    print(f'Tweet text:{tweet.full_text}')
 
# Get tweet status
print(f'Is Retweeted:{tweet.retweeted}')
print(f'Is favorited:{tweet.favorited}')
print(f'Is quote:{tweet.is_quote_status}')
 
# Get Tweet statistics
print(f'Retweet count:{tweet.retweet_count}')
print(f'Favorite count:{tweet.favorite_count}')
 
# Get tweet lang
print(f'Tweet lang:{tweet.lang}')

print(location)"""