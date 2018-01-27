from flask import render_template
from app import app
from .requests import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Get news
    top_headlines = get_news('general')
    sports        = get_news('sports')
    tech           = get_news('technology')
    print(top_headlines)
    title = 'News'
    return render_template('index.html', title = title,trending = top_headlines,sports=sports,techie=tech)

@app.route('/news/<int:news_id>')
def news(news_id):

    return render_template('news.html',id=news_id)
