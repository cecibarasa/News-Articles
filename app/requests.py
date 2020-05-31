import urllib.request
import json
from .models import Source, Article

# Getting api key
api_key = None
# Getting the news base url
base_url = None

article_url = None


def configure_request(app):
    global api_key, base_url, article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['NEWS_ARTICLE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results


def process_results(source_list):
    '''
    Function that processes the source result and transforms them to a list of objects
    
    Args:
        source_list: A list of dictionaries that contain source details
    Returns:
        source_results: A lost of source objects
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get("id")
        name = source_item.get("name")
        description = source_item.get("description")
        url = source_item.get("url")
        category = source_item.get("category")
        language = source_item.get("language")
        country = source_item.get("country")

        source_object = Source(id, name, description, url,category, language, country)
        source_results.append(source_object)

    return source_results


def get_articles(source_id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = article_url.format(source_id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles_results(article_results_list)

    return article_results


def process_articles_results(articles_list):
    '''
    Function that processes the article result and transforms them to a list of objects
    
    Args:
        article_list: A list of dictionaries that contain article details
    Returns:
        article_results: A list of article objects
    '''

    article_results = []
    for article_item in articles_list:
        author = article_item.get("author")
        title = article_item.get("title")
        description = article_item.get("description")
        url = article_item.get("url")
        urlToImage = article_item.get("urlToImage")
        publishedAt = article_item.get("publishedAt")

        article_object = Article(
            author, title, description, url, urlToImage, publishedAt)
        article_results.append(article_object)

    return article_results

def search_article(article_name):
    search_article_url = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'.format(api_key,article_name)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['results']:
            search_article_list = search_article_response['results']
            search_article_results = process_results(search_article_list)


    return search_article_results	