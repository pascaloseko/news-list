from app import app
import urllib.request,json
from .models import news,sources

News = news.News
Sources = sources.Sources

# Getting the api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(general):
    get_news_url = base_url.format(general,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def get_sources():
    get_sources_url = 'https://newsapi.org/v2/sources?api_key={}'.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_object = None

        if get_source_response:
            id = get_source_response.get('id')
            name = get_source_response.get('name')
            description = get_source_response.get('description')
            url = get_source_response.get('url')
            country = get_source_response.get('country')

            source_object = Sources(id,name,description,url,country)


    return source_object

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        if url:
            news_object = News(author,title,description,url,urlToImage,publishedAt)
            news_results.append(news_object)

    return news_results
