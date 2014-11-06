import newspaper
from newspaper import Article

def process_website(url):
    a = Article(url)
    a.download()
    a.parse()
    a.nlp()

    article={}
    article['authors']=a.authors
    article['title']=a.title
    article['summary']=a.summary
    article['lead_image']=a.top_image
    #article['images']=a.images - Also returns random images from the page so will not be returned
    article['movies']=a.movies
    article['text']=a.text
    #article['keywords']=a.keywords - Newspaper's keyword extraction isn't great so a more specialised library will be used. To be added

    return article
