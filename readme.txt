Assignment 2

Data Management Warehousing and analytics [CSCI 5408]
Winter 2019
Dalhousie University


Flow of my assignment

1. Setup of cluster and apache spark. Screenshots are given in the report
2. Written program for search and stream API. I have used tweepy to extract raw tweets. (Files in scripts folder: search.py and stream.py)
3. Executed both scripts and collected 1999 tweets for search API and 1168 and 1500 tweets for stream API respectively. (Files in data folder: search_data.csv, tweets_stream_old.csv, tweets_stream_new.csv)
3. Written a script to import CSV file to mongo collection. (Files in script folder: search_csv_to_mongo.py, stream_csv_to_mongo.py)
4. Uploaded all files from script and data folder to AWS instance. 
5. Executed search_csv_to_mongo.py and stream_csv_to_mongo.py to import CSV files to mongoDB collection.
6. Written commands in pyspark for counting the words. I have included txt files which contain command line. (Files in scripts folder: pyspark_code_search.txt, pyspark_code_stream_old_data.txt and pyspark_code_stream_new_data.txt)


#Notes:
1. I have created an account in Twitter with handle @my_data_test for testing purposes. I tweeted many tweets with keywords mentioned in the problem so that I can use them for program efficiently.