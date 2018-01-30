import urllib.request,json
from .models import News
from .models import Source

# News = news.News
# Sources = sources.Sources

# Getting the api key
api_key = None

# Getting the news base url
base_url = None

#Getting the source base url
source_url = None

def configure_request(app):
    global api_key,base_url,source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    source_url = app.config['SOURCE_NEWS_URL']

def get_news_sources(country,category):
    get_news_url = base_url.format(country,category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        #print(get_news_response)

        source_results = None

        if get_news_response['sources']:
            source_results_list = get_news_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):

    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    #print("source list is",repr(source_list))
    for source_item in source_list:
        id = source_item.get('id')
        #print(id)
        name = source_item.get('name')
        #print(name)
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')

        if url:
            source_object = Source(id,name,description,url,category,country)
            news_results.append(source_object)

    return news_results

def get_sources_articles(id):
    """
    Function that gets the json response to our url request
    """
    get_news_url = source_url.format(id,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_articles(news_results_list)


    return news_results

def process_articles(articles_list):
    '''
    We now process the dictionary and output the 
    list of objects - news_results

    We process results which will transform our dict into a list of objects
    '''
    news_results = []
    source_dict = {}

    for result in articles_list:
        # Store the nested dict in source_id
        source_id = result['source']
        # now we extract it and store in our source_dict
        source_dict['id'] = source_id['id']
        source_dict['name'] = source_id['name']
        id = source_dict['id']
        name = source_dict['name']
        print(name)
        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        publishedAt = result.get('publishedAt')

        if urlToImage:
            source_object = News(id,name,author,title,description,url,urlToImage,publishedAt)
            news_results.append(source_object)

    return news_results