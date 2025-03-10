import os
from dotenv import load_dotenv
import tweepy
import requests


def scrape_user_tweets(username,num_tweets=5,mock = False):
    """
    Scrapes pre made Edens's Github Gist file of tweets and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    https://twitter.com/EdenEmarco177
    """
    tweet_list = []

    if mock:
        EDEN_TWITTER_GIST = "https://gist.githubusercontent.com/emarco177/827323bb599553d0f0e662da07b9ff68/raw/57bf38cf8acce0c87e060f9bb51f6ab72098fbd6/eden-marco-twitter.json"
     #   tweets = scrape_user_tweets(username="EdenEmarco177")
        tweets = requests.get(EDEN_TWITTER_GIST).json()
        #return tweets
       # print(tweets)
    else:
        # need to add keys to .env file
        twitter_client = tweepy.Client(
            bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
            consumer_key=os.environ["TWITTER_API_KEY"],
            consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
            access_token=os.environ["TWITTER_ACCESS_TOKEN"],
            access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
        )
        user_id = twitter_client.get_user(username=username).data.id
        tweets = twitter_client.get_users_tweets(id=user_id, max_results=num_tweets)
    
    for tweet in tweets:
        tweet_dict = {}
      #  tweet_dict['text'] = tweet.text
      #  print(f"---------------**************text is: {tweet["text"]}")
        tweet_dict["text"] = tweet["text"]
        #tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
        tweet_dict["url"] = "lettuce field"
        tweet_list.append(tweet_dict)
    return tweet_list

if __name__ == "__main__":
    tweets = scrape_user_tweets(username="EdenEmarco177",mock=True)
    print(tweets)