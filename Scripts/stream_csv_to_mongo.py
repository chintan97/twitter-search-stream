from pymongo import MongoClient
import csv

try:
    connection = MongoClient()
    print("Connection successful")
except:
    print("MongoDB connection request failed!")

# select database
db = connection.assignment2

# select collection
collection = db.stream_data_second

# https://realpython.com/python-csv/

# This program will need to be executed twice. One with file name tweets_stream_old.csv and collection name stream_data, and other with tweets_stream_new.csv and collection name stream_data_second
with open("tweets_stream_new.csv", 'r', encoding='unicode_escape', newline='') as my_csv:
    read_file = csv.DictReader(my_csv)
    for data in read_file:
        if (data['number'] == ''):
            continue
        make_document = {"tweet_count": data['number'], "handle_name": data['handle name'], "handle_id": data['handle ID'], "tweet_text": data['tweet'], "tweet_time": data['tweet time'], "retweet_count": data['retweet count'], "favorite_count": data['likes count']}
        collection.insert_one(make_document)   # insert each row as document in the collection
    my_csv.close()