import unittest
from app.news import News_Articles

class ArticlesTest(unittest.TestCase):

    '''
    Test Class to test the behaviour of the News_Articles class
    
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = News_Articles('BBC SPORT','US Open final: Raducanu v Fernandez - radio & text',"Britain's Emma Raducanu faces Canada's Leylah Fernandez in the US Open final - follow live radio and text commentary",'http://www.bbc.co.uk/sport/live/tennis/54517115','https://www.investors.com/wp-content/uploads/2021/01/Stock-Tesla-modelY-01-adobe.jpg','https:////m.files.bbci.co.uk/modules/bbc-morph-sport-seo-meta/1.21.1/images/bbc-sport-logo.png')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,News_Articles))