from flask import render_template,request
from . import main
from ..requests import get_news_sources,get_sources_articles
from ..models import Source

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Get news
    general       = get_news_sources('gb','general')
    #print(general)
    sports        = get_news_sources('gb','sports')
    tech          = get_news_sources('us','technology')
    #print(tech)
    business      = get_news_sources('gb','business')
    #print(business)
    health        = get_news_sources('us','health')
    #print(health)
    entertainment = get_news_sources('gb','entertainment')
    #print(entertainment)
    #print(top_headlines)
    #title = 'News'
    return render_template('index.html', 
                            general = general,
                            sports=sports,
                            techie=tech,
                            business=business,
                            health=health,
                            entertainment=entertainment)

@main.route('/news/<id>')
def news(id):
    """
    View articles page that returns the news article from a highlight
    """
    news = get_sources_articles(id)

    return render_template('sources.html',news=news)

