import urllib.request
import json
from .models import Source,Article

#getting api key
api_key = None

#getting news base url
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key=app.config['NEWS_API_KEY']
    base_url=app.config['NEWS_API_BASE_URL']
    article_url=app.config['ARTICLE_NEWS_URL']

def get_sources(category):
    '''
    Function that gets json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results

def process_sources(sources_list):
    '''
    function that processes the news results and transform them to a list of objects
    Args:
        sources_list: A list of dictionaries that contain news details
    Returns:
        sources_results: Alist of news source objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

        if id:
            sources_object = Source(id,name,description,url,category,language,country)

            sources_results.append(sources_object)
    return sources_results

def get_articles(id):
    '''
    Function that gets the json response to url request
    '''
    get_article_news_url = article_url.format(id,api_key)
    with urllib.request.urlopen(get_article_news_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(articles_list):
    '''
    process the dictionary and output a list of objects
    '''
    article_results = []
    source_dictionary = {}
    for result in articles_list:
        source_id = result ['source']
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        id = source_dictionary['id']
        name = source_dictionary['name']

        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        publishedAt = result.get('publishedAt')

        if urlToImage:
            print (id)
            article_object = Article(id,name,author,title,description,url,urlToImage,publishedAt)

            article_results.append(article_object)

    return article_results