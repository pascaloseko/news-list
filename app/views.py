from flask import render_template
from app import app
from .requests import get_news,get_sources

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

@app.route('/sources/<string:id>')
def sources(id):

    '''
    View sources page function that returns the source details page and its data
    '''
    sources = Sources.get_sources(sources.id)
    print(sources)

    return render_template('sources.html',sources = sources)
