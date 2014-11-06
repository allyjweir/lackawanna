'''
Basically from researching it I cannot find a library that when given a URL of a tweet, it can go and find the text, timestamp and username of that tweet. This hack solves that. It is dangerous and likely to become outmoded in the future but is at least easily testable. It will do the task okay for the project as long as it is backed up by the PNG/PDF of the page itself.

The twitter API itself seems to be more about creating clients. There seems to be a lot of hoops for just retrieving a singular tweet in (for argument's sake) JSON. You require authentication, it is rate limited etc. It can do it (as seen here https://dev.twitter.com/rest/reference/get/statuses/show/%3Aid but I'm not sure if it is worth all of that hassle...yet. I am sure the perfectionist in me will make me want to sort it out properly!)
'''

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
