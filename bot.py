import tweepy
import time

consumer_key='X9NTxaDUyP50DCMfKSw02Ntw8'
consumer_secret='370tUVlgN99By6qaxo7koLsWJTuueiP5MkpjrY2sltHbTUFf14'
key='1265561666755989504-yxW9aS8GRotfmszFUKxfcZvaPgmkgM'
secret='VkV9ZM1EWqVpsDDvwnHJdKUagE9HHPzqjYJ04zfYZXx4n'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


api = tweepy.API(auth)
# api.update_status('Hello I am Twitter Bot this is my third message')
# print("Status Updated")
# tweets=api.mentions_timeline()
# print(type(tweets))
# print(tweets[0])
# print(tweets[0].text)
FILE_NAME='last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read=open(FILE_NAME,'r')
    last_seen_id=int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME,last_seen_id):
    file_write=open(FILE_NAME,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

# store_last_seen(FILE_NAME,'1265632351893114864')


# id=read_last_seen(FILE_NAME)
# print(id)


# for tweet in tweets:
#     if "#randtweet" in tweet.text.lower():
#         print("New Tweet Found!")
#         print(str(tweet.id) + '-' + tweet.text)
# print(str(tweet.id) + '-' + tweet.full_text)
# tweets=api.mentions_timeline(id of tweet)
  ##earlier we using single line if using multiple lines or parra extended is used

 ##full text since using extended
 ##reversed so that old tweet first replied
def reply():
    tweets=api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode='extended')
    for tweet in reversed(tweets):
        if "#randtweet" in tweet.full_text.lower():  
            # print("New Tweet Found!")
            try:
                print("Replied To Id:" + str(tweet.id))
                api.update_status("@" + tweet.user.screen_name + " Good Luck " , tweet.id)
                api.create_favorite(tweet.id)
                api.retweet(tweet.id)
            except tweepy.TweepError as e:
                print(e.reason)
            store_last_seen(FILE_NAME,tweet.id)


while True:
    reply()
    time.sleep(60)
    print("Working")
