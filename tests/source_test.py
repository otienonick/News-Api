import unittest
from app.news import News_Source

class SourceTest(unittest.TestCase):

    '''

    Test Class to test the behaviour of the News_Source class.
    
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = News_Source('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com','"https://abcnews.go.com','general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,News_Source))