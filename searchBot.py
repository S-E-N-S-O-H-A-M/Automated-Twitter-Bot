import tweepy
import time

consumer_key='X9NTxaDUyP50DCMfKSw02Ntw8'
consumer_secret='370tUVlgN99By6qaxo7koLsWJTuueiP5MkpjrY2sltHbTUFf14'
key='1265561666755989504-yxW9aS8GRotfmszFUKxfcZvaPgmkgM'
secret='VkV9ZM1EWqVpsDDvwnHJdKUagE9HHPzqjYJ04zfYZXx4n'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


hashtag="100daysofcode" ##if more thatn 1 hashtaguse tupple like("100daysofcode","python")
tweetNumber=10

tweets=tweepy.Cursor(api.search,hashtag).items(tweetNumber)  ##if want one page instead of item write pages and each page has 20 tweets it may vary 

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()