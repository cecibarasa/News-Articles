import os
class Config:
    '''
    General configuration parent class
    '''
    
    TOPNEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey=fc0dd4871fc54be18c1ae26a02ba8a53'
    CATEGORIES_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=fc0dd4871fc54be18c1ae26a02ba8a53'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=fc0dd4871fc54be18c1ae26a02ba8a53'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
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