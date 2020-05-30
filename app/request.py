import urllib.request,json
from .models import Topnews, Catnews, Update

# Getting api key
api_key = None

# Getting the news api base urls
base_url = None
base2_url = None
base3_url = None

def configure_request(app):
    global api_key,base_url,base2_url,base3_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["TOPNEWS_API_BASE_URL"]
    base2_url = app.config["CATEGORIES_API_BASE_URL"]
    base3_url = app.config["ARTICLES_BASE_URL"]

def get_topnews(source):
    """
    Function that gets the json response to our url request
    """
    get_topnews_url = base_url.format(source)

    with urllib.request.urlopen(get_topnews_url) as url:
        get_topnews_data = url.read()
        get_topnews_response = json.loads(get_topnews_data)
        print(get_topnews_response)
        topnews_results = None

        if get_topnews_response['articles']:
            topnews_results_list = get_topnews_response['articles']
            topnews_results = process_results(topnews_results_list)

    return topnews_results

def process_results(topnews_list):
    '''
    Function  that processes the topnews result and transform them to a list of Objects
    Args:
        topnews_list: A list of dictionaries that contain topnews details
    Returns :
        topnews_results: A list of topnews objects
    '''
    topnews_results = []
    for topnews_item in topnews_list:
        name = topnews_item.get('name')
        title = topnews_item.get('title')
        author = topnews_item.get('author')
        description = topnews_item.get('description')
        urlToImage = topnews_item.get('urlToImage')
        url = topnews_item.get('url')

        if urlToImage:
            topnews_object = Topnews(name,author,title,description,urlToImage,url)
            topnews_results.append(topnews_object)

    return topnews_results



def get_catnews(category):
    """
    Function that gets the json response to our url request
    """
    get_catnews_url = base2_url.format(category)

    with urllib.request.urlopen(get_catnews_url) as url:
        get_catnews_data = url.read()
        get_catnews_response = json.loads(get_catnews_data)
        print(get_catnews_response)
        catnews_results = None

        if get_catnews_response['sources']:
            catnews_results_list = get_catnews_response['sources']
            catnews_results = process2_results(catnews_results_list)

    return catnews_results

def process2_results(catnews_list):
    '''
    Function  that processes the catnews result and transform them to a list of Objects
    Args:
        catnews_lis A list of dictionaries that contain catnews details
t:
    Returns :
        catnews_results: A list of catnews objects
    '''
    catnews_results = []
    for catnews_item in catnews_list:
        id = catnews_item.get('id')
        name = catnews_item.get('name')
        description = catnews_item.get('description')
        url = catnews_item.get('url')

        if id:
            catnews_object = Catnews(id,name,description,url)
            catnews_results.append(catnews_object)

    return catnews_results
def get_updates(id):
    """
    Function that gets the json response to our url request
    """
    get_updates_url = base3_url.format(id)
    print(get_updates_url)

    with urllib.request.urlopen(get_updates_url) as url:
        get_updates_data = url.read()
        get_updates_response = json.loads(get_updates_data)
       
        updates_results = None

        if get_updates_response['articles']:
            updates_results_list = get_updates_response['articles']
            updates_results = process3_results(updates_results_list)

    return updates_results

def process3_results(updates_list):
    '''
    Function  that processes the update result and transform them to a list of Objects
    Args:
        updates_list: A list of dictionaries that contain category news' details
    Returns :
        updates_results: A list of update objects
    '''
    updates_results = []
    for update_item in updates_list:
        id = update_item.get('id')
        author = update_item.get('author')
        title = update_item.get('title')
        description = update_item.get('description')
        url = update_item.get('url')
        urlToImage = update_item.get('urlToImage')
        publishedAt = update_item.get('publishedAt')
       
        updates_object = Update(id,author,title,description,url,urlToImage,publishedAt)
        updates_results.append(updates_object)

    return updates_results