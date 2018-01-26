class Config:

    '''
    general config parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG=True