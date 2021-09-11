import urllib.request,json
from app.news import News_Articles, News_Source,Everything


# Getting api key
api_key = None
# Getting the newsSource base url
source_url = None
# Getting the newsArticle base url

article_url = None

def configure_request(app):
    global api_key,source_url,article_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_SOURCE_URL ']
    article_url = app.config['NEWS_ARTICLE_URL']

def get_sources():

    '''
    function that gets the json response to our url request

    '''
    get_news_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=16d08e904b854e69b6d30c2bc03e7a20'
    # get_news_url = article_url.format('https://newsapi.org/v2/top-headlines/sources?apiKey={}',api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_response = json.loads(get_news_data)

        news_results = None

        if get_response['sources']:
            news_list = get_response['sources']
            news_results = process_sources(news_list)

    return news_results        

def process_sources(news_list):

    '''
    function that processes the  news_result and transform them to a list of objects.

    Args:news_list:A list of dicts that contains news details.

    Returns:news_results:A list of news Objects.

    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')

        if url:
            news_object = News_Source(id,name,description,url,category)
            news_results.append(news_object)

    return news_results        


def get_articles(category):

    '''
    function that gets the json response to our url request

    '''
    get_newsource_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=16d08e904b854e69b6d30c2bc03e7a20'.format(category)


    with urllib.request.urlopen(get_newsource_url) as url:
        get_newsource_data = url.read()
        get_newsresponse = json.loads(get_newsource_data)

        newsource_results = None

        if get_newsresponse['articles']:
            newsource_list = get_newsresponse['articles']
            newsource_results = process_articles(newsource_list)

    return newsource_results 

    
def process_articles(source_list):

    '''
    function that processes the  news_result and transform them to a list of objects.

    Args:news_list:A list of dicts that contains news details.

    Returns:news_results:A list of news Objects.

    '''
    newsource_results = []
    
    for newsource_item in source_list:
        source = newsource_item.get('source')
        author = newsource_item.get('author')
        title = newsource_item.get('title')
        description = newsource_item.get('description')
        url = newsource_item.get('url')
        urlToImage = newsource_item.get('urlToImage')

        if urlToImage:
            news_object = News_Articles(source,author,title,description,url,urlToImage)
            newsource_results.append(news_object)

    return newsource_results    






def get_everything():

    '''
    function that gets the json response to our url request

    '''
    get_every_news = 'https://newsapi.org/v2/everything?q=news&apiKey=16d08e904b854e69b6d30c2bc03e7a20'
    with urllib.request.urlopen(get_every_news) as url:
        get_news_data = url.read()
        get_all_response = json.loads(get_news_data)

        news_results = None

        if get_all_response['articles']:
           top_list = get_all_response['articles']
           news_results = process_everything_news(top_list)

    return news_results                       

def process_everything_news(top_list):

    '''
    function that processes the  news_result and transform them to a list of objects.

    Args:news_list:A list of dicts that contains news details.

    Returns:news_results:A list of news Objects.

    '''
    every_result = []
    
    for newsource_item in top_list:
        title = newsource_item.get('title')
        description = newsource_item.get('description')
        description = newsource_item.get('description')
        url = newsource_item.get('url')
        urlToImage = newsource_item.get('urlToImage')

        if urlToImage:
            news_object = Everything(title,description,url,urlToImage)
            every_result.append(news_object)

    return every_result    


