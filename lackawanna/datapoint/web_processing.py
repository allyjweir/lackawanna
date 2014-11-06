import newspaper
from newspaper import Article

def process_website(url):
    a = Article(url)
    a.download()
    a.parse()
    a.nlp()

    article['authors']=a.authors
    article['title']=a.title
    article['summary']=a.summary
    article['lead_image']=a.top_image
    article['images']=a.images
    article['movies']=a.movies
    article['text']=a.text
    article['keywords']=a.keywords

    return article
