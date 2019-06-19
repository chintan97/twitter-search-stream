import csv
import tweepy
import re
import sys
import json

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("",
                      "")

api = tweepy.API(auth)

# For first streaming I used file name as tweets_stream_old.csv and for second streaming I used tweets_stream_new.csv
file_object = open("tweets_stream_new.csv", "a+")
file_object = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
file_object.writerow(['number', 'handle name', 'handle ID', 'tweet', 'tweet time', 'retweet count', 'likes count'])

row_count = 1
max_count = 1500

# http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
class MyStreamListener(tweepy.StreamListener):
    def on_data(self, status):
        global row_count
        if row_count <= max_count:
            json_data = json.loads(status)
            try:
                make_data = re.sub(r'@#[A-Za-z0-9]+', '', json_data['extended_tweet']['full_text'])   # full_text returns whole tweet of 240 characters
                make_data.replace("\\u", "")   # remove emoticons
                file_object.writerow(
                    [row_count, json_data['user']['name'], json_data['user']['screen_name'], make_data,
                     json_data['created_at'], json_data['retweet_count'], json_data['favorite_count']])
                print("\nCount = " + str(row_count))
                row_count += 1
            except:
                try:
                    make_data = re.sub(r'@#[A-Za-z0-9]+', '', json_data['retweeted_status']['extended_tweet']['full_text'])
                    make_data.replace("\\u", "")
                    file_object.writerow(
                        [row_count, json_data['user']['name'], json_data['user']['screen_name'], make_data,
                         json_data['created_at'], json_data['retweet_count'], json_data['favorite_count']])
                    print("\nCount = " + str(row_count))
                    row_count += 1
                except:
                    try:
                        make_data = re.sub(r'@#[A-Za-z0-9]+', '', json_data['quoted_status']['extended_tweet']['full_text'])
                        make_data.replace("\\u", "")
                        file_object.writerow(
                            [row_count, json_data['user']['name'], json_data['user']['screen_name'], make_data,
                             json_data['created_at'], json_data['retweet_count'], json_data['favorite_count']])
                        print("\nCount = " + str(row_count))
                        row_count += 1
                    except:
                        pass
        else:
            sys.exit()


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=['Halifax'])
