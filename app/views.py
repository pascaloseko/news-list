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
    top_headlines = get_news()
    print(top_headlines)
    title = 'News'
    return render_template('index.html', title = title,trending = top_headlines)

@app.route('/news/<int:news_id>')
def news(news_id):

    return render_template('news.html',id=news_id)
