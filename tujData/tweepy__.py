import tweepy



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tweepyapi = tweepy.API(auth)

tweepyapi.update_status('Hello World!')
print("Hello {}".format(tweepyapi.me().name))