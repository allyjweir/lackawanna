from newspaper import Article
import requests
from bs4 import BeautifulSoup
from topia.termextract import extract
from selenium import webdriver
import random
from django.core.files import File
import os
import errno


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def get_article(url):
    a = Article(url)
    a.download()
    a.parse()
    a.nlp()

    article={}
    article['authors']=a.authors
    article['title']=a.title
    article['summary']=a.summary
    article['lead_image']=a.top_image
    article['movies']=a.movies
    article['text']=a.text
    article['keywords']=get_keywords(a.text)

    return article


'''This calls out to PhantomJS through Selenium WebDriver to capture a PNG of a web page'''
def get_screenshot(url):
    make_sure_path_exists('temp')
    random_integer = '{0:05}'.format(random.randint(1,100000))
    filename = 'temp/temp_screencap_' + str(random_integer) + '.png'

    # TODO: Add error checking, add logging and exceptions throughout!

    temp_file = open(filename, 'w+')
    web = webdriver.PhantomJS()
    web.set_window_size(1280, 1080)
    web.get(url)
    web.save_screenshot(filename)
    temp_file.close()
    web.quit()
    return filename




'''Using the Toperia Term Extractor, this finds keywords, along with their importance to the text as a whole, and returns them'''
def get_keywords(text):
    extractor = extract.TermExtractor()
    return sorted(extractor(text))


'''
Basically from researching it I cannot find a library that when given a URL of a tweet, it can go and find the text, timestamp and username of that tweet. This hack solves that. It is dangerous and likely to become outmoded in the future but is at least easily testable. It will do the task okay for the project as long as it is backed up by the PNG/PDF of the page itself.
The Twitter API itself seems to be more about creating clients. There seems to be a lot of hoops for just retrieving a singular tweet in (for argument's sake) JSON. You require authentication, it is rate limited etc. It can do it (as seen here https://dev.twitter.com/rest/reference/get/statuses/show/%3Aid but I'm not sure if it is worth all of that hassle...yet. I am sure the perfectionist in me will make me want to sort it out properly!)
'''
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
