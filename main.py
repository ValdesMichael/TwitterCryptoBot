from requests import Request, Session
import json
import tweepy
#Consumer keys and access tokens for CoinMarketCap and Twitter APIs
coinmarketcap_api_key = ""
twitter_consumer_key = ""
twitter_consumer_secret = ""
twitter_access_token = ""
twitter_access_token_secret = ""
# Authenticate to Twitter
auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

# Create twitter API object
api = tweepy.API(auth)

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'slug': 'bitcoin',
    'convert': 'USD'
}
#autheticate to coinmarketcap API
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': coinmarketcap_api_key,
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
#create a tweet
bitImg = api.media_upload("bitcoin.png")
bitTweet = 'The current price of ' + json.loads(response.text)['data']['1']['name'] + ' is' + ' $' + str(round(json.loads(response.text)['data']['1']['quote']['USD']['price'], 2))


# Post tweet with image
api.update_status(bitTweet, media_ids=[bitImg.media_id_string])
