import requests
from bs4 import BeautifulSoup

    def get_tweet(url):
    # Retrieve tweet
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    # Find it in the soup
    acc_name = soup.find_all('strong', 'fullname')
    username = soup.find_all('span', 'username js-action-profile-name')
    tweet_text = soup.find_all('p', 'js-tweet-text')
    tweet_timestamp = soup.find_all('a', 'tweet-timestamp')

    # Process it to get something intelligible
    tweet={}
    tweet['text'] = tweet_text[0].get_text().encode('ascii', 'ignore')
    tweet['timestamp'] = tweet_timestamp[0]['title']
    tweet['username'] = username[0].get_text().encode('ascii', 'ignore')
    tweet['name'] = acc_name[0].get_text().encode('ascii', 'ignore')

    return tweet
