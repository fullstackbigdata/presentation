## environment set up
# pip install yahoo_finance
# pip install awscli
# pip install boto3 --ignore-installed six
## aws sqs receive-message --queue-url https://queue.amazonaws.com/773351289708/kpmg-demo --attribute-names All --message-attribute-names All --max-number-of-messages 10

from yahoo_finance import Share
import boto3
import json
import array
from multiprocessing import Process

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='kpmg-demo')
print(queue.url)
s3 = boto3.resource('s3')

def yahoo_ticker():
    yahoo_counter = 1
    while True:
        # Selects the ticker to be used
        yahoo = Share('YHOO')

        # Create the data tuple
        yahoo_data = 'Ticker: YHOO:', yahoo.get_price(), yahoo.get_trade_datetime()
        yahoo_message = str(yahoo_data)

        # Sends the data to the SQS queue
        response = queue.send_message(MessageBody=yahoo_message)

        # Writes ticker, current price, and timestamp to a txt file locally
        yahoo_filename = "yahoo" + " " + yahoo.get_trade_datetime() + str(yahoo_counter) + ".txt"
        with open(yahoo_filename, 'w') as outfile:
            json.dump(yahoo_data, outfile)

        # Uploads the file to S3
        data = open(yahoo_filename, 'rb')
        s3.Bucket('kpmg-interview-demo').put_object(Key=yahoo_filename, Body=data)

        # Prints the ticker information to the console
        print "Ticker: YHOO", yahoo.get_price(), yahoo.get_trade_datetime()

        # Refreshes the selected ticker
        yahoo.refresh()
        yahoo_counter = yahoo_counter + 1
def google_ticker():
    google_counter = 1
    while True:
        google = Share('GOOG')
        google_data = 'Ticker: GOOG:', google.get_price(), google.get_trade_datetime()
        google_message = str(google_data)
        response = queue.send_message(MessageBody=google_message)
        google_filename = "google" + " " + google.get_trade_datetime() + str(google_counter) + ".txt"
        with open(google_filename, 'w') as outfile:
            json.dump(google_data, outfile)
        data = open(google_filename, 'rb')
        s3.Bucket('kpmg-interview-demo').put_object(Key=google_filename, Body=data)
        print "Ticker: GOOG", google.get_price(), google.get_trade_datetime()
        google.refresh()
        google_counter = google_counter + 1
def facebook_ticker():
    facebook_counter = 1
    while True:
        facebook = Share('FB')
        facebook_data = 'Ticker: FB:', facebook.get_price(), facebook.get_trade_datetime()
        facebook_message = str(facebook_data)
        response = queue.send_message(MessageBody=facebook_message)
        facebook_filename = "facebook" + " " + facebook.get_trade_datetime() + str(facebook_counter) + ".txt"
        with open(facebook_filename, 'w') as outfile:
            json.dump(facebook_data, outfile)
        data = open(facebook_filename, 'rb')
        s3.Bucket('kpmg-interview-demo').put_object(Key=facebook_filename, Body=data)
        print "Ticker: FB", facebook.get_price(), facebook.get_trade_datetime()
        facebook.refresh()
        facebook_counter = facebook_counter + 1
def twitter_ticker():
    twitter_counter = 1
    while True:
        twitter = Share('TWTR')
        twitter_data = 'Ticker: TWTR:', twitter.get_price(), twitter.get_trade_datetime()
        twitter_message = str(twitter_data)
        response = queue.send_message(MessageBody=twitter_message)
        twitter_filename = "twitter" + " " + twitter.get_trade_datetime() + str(twitter_counter) + ".txt"
        with open(twitter_filename, 'w') as outfile:
            json.dump(twitter_data, outfile)
        data = open(twitter_filename, 'rb')
        s3.Bucket('kpmg-interview-demo').put_object(Key=twitter_filename, Body=data)
        print "Ticker: TWTR", twitter.get_price(), twitter.get_trade_datetime()
        twitter.refresh()
        twitter_counter = twitter_counter + 1
def hortonworks_ticker():
    hortonworks_counter = 1
    while True:
        hortonworks = Share('HDP')
        hortonworks_data = 'Ticker: HDP:', hortonworks.get_price(), hortonworks.get_trade_datetime()
        hortonworks_message = str(hortonworks_data)
        response = queue.send_message(MessageBody=hortonworks_message)
        hortonworks_filename = "hortonworks" + " " + hortonworks.get_trade_datetime() + str(hortonworks_counter) + ".txt"
        with open(hortonworks_filename, 'w') as outfile:
            json.dump(hortonworks_data, outfile)
        data = open(hortonworks_filename, 'rb')
        s3.Bucket('kpmg-interview-demo').put_object(Key=hortonworks_filename, Body=data)
        print "Ticker: HDP", hortonworks.get_price(), hortonworks.get_trade_datetime()
        hortonworks.refresh()
        hortonworks_counter = hortonworks_counter + 1
def amazon_ticker():
    amazon_counter = 1
    while True:
        amazon = Share('AMZN')
        amazon_data = 'Ticker: AMZN:', amazon.get_price(), amazon.get_trade_datetime()
        amazon_message = str(amazon_data)
        response = queue.send_message(MessageBody=amazon_message)
        amazon_filename = "amazon" + " " + amazon.get_trade_datetime() + str(amazon_counter) + ".txt"
        with open(amazon_filename, 'w') as outfile:
            json.dump(amazon_data, outfile)
        data = open(amazon_filename, 'rb')
        s3.Bucket('kpmg-interview-demo').put_object(Key=amazon_filename, Body=data)
        print "Ticker: AMZN", amazon.get_price(), amazon.get_trade_datetime()
        amazon.refresh()
        amazon_counter = amazon_counter + 1

if __name__ == '__main__':
    Process(target=yahoo_ticker).start()
    Process(target=google_ticker).start()
    Process(target=facebook_ticker).start()
    Process(target=twitter_ticker).start()
    Process(target=hortonworks_ticker).start()
    Process(target=amazon_ticker).start()
