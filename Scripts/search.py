import tweepy
import csv
import re

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("",
                      "")

api = tweepy.API(auth)

query_keyword = "Halifax"
max_count = 2000
per_query_count = 100

# Initially set max_id to max. It will be used in getting the tweets
max_id = 9999999999999999999

# We will run a loop till 2000 tweets are extracted.
# In each loop, 100 tweets are fetched and max_id will be used to fetch old 100 tweets

# https://realpython.com/python-csv/
with open('search_data.csv', 'w') as file_object:
    file_object = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_object.writerow(['number', 'handle name', 'handle ID', 'tweet', 'tweet time', 'retweet count', 'likes count'])
    row_count = 1
    while row_count < max_count:
        id_list = []   # it stores tweet ids so that it can be useful to fetch old 100 tweets from that id
        results = api.search(q=query_keyword, count=per_query_count, max_id = max_id, tweet_mode='extended')
        for tweet in results:
            id_list.append(tweet.id)
            try:
                if (hasattr(tweet, 'retweeted_status')):
                    make_text = re.sub(r'@#[A-Za-z0-9]+', '', tweet.retweeted_status.full_text)   # full_text fetches all chracters of tweets i.e. 240 characters, only @ and # are kept in tweets
                    make_text.replace("\\u", "")   # To remove emoticons
                    file_object.writerow(
                        [row_count, tweet.user.name, tweet.user.screen_name, 'RT @' +tweet.retweeted_status.user.screen_name + ": " + make_text,
                         tweet.created_at, tweet.retweet_count, tweet.favorite_count])
                else:
                    make_text = re.sub(r'@#[A-Za-z0-9]+', '', tweet.full_text)
                    make_text.replace("\\u", "")
                    file_object.writerow([row_count, tweet.user.name, tweet.user.screen_name, make_text, tweet.created_at,tweet.retweet_count, tweet.favorite_count])
                row_count += 1
            except:
                continue
        max_id = min(id_list)