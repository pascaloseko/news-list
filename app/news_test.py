import unittest
from models import news

News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News('Pascal oseko','My awesome book','its about my life as a developer','https://www.cbsnews.com/videos/todays-top-entertainment-headlines/','https://cbsnews1.cbsistatic.com/hub/i/r/2017/12/06/292daff0-3220-41dd-b1d1-5663b2ae4325/thumbnail/1200x630/aa306d2bc8379b636769146cc82df9c8/cbsn-fusion-todays-top-entertainment-headlines-thumbnail-1457181-640x360.jpg','2017-12-06')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()