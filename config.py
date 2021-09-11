import os
class Config:

    '''
    General configuration parent class
    
    '''
    
    
    NEWS_EVERYTHING_URL = 'https://newsapi.org/v2/everything?q=news&apiKey={}'
    NEWS_SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'


    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('ead4ba544d5d4f75942062f71d3b4720')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}