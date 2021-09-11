import urllib.request,json
from app.news import Everything

# Getting api key
api_key = None

def configure_request(app):
    global api_key
    api_key = app.config['NEWS_API_KEY']


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
           news_results = process_everything(top_list)

    return news_results                       

def process_everything(top_list):

    '''
    function that processes the  news_result and transform them to a list of objects.

    Args:news_list:A list of dicts that contains news details.

    Returns:news_results:A list of news Objects.

    '''
    every_result = []
    
    for newsource_item in top_list:
        title = newsource_item.get('title')
        description = newsource_item.get('description')
        url = newsource_item.get('url')
        urlToImage = newsource_item.get('urlToImage')
        content = newsource_item.get('content')

        if urlToImage:
            news_object = Everything(title,description,url,urlToImage,content)
            every_result.append(news_object)

    return every_result    


