import unittest
from app.news import Everything

class EverythingTest(unittest.TestCase):

    '''

    Test Class to test the behaviour of the Everything class.
    
    '''

    def setUp(self):

        '''
        Set up method that will run before every Test
        '''
        self.new_movie = Everything('Watch Tesla','Stocks retreated last week. Elon Musk says the new Tesla FSD Beta will \"blow your mind.','A thrilling new Python Series','https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-market-rally-retreats-epic-apple-sell-off-tesla-self-driving-release/','https://www.investors.com/wp-content/uploads/2021/01/Stock-Tesla-modelY-01-adobe.jpg','Dow Jones futures will open Sunday evening, along with S&amp;P 500 futures and Nasdaq futures. The stock market rally retreated last week, with losses picking up steam Friday, led by Apple, Google an… [+10921 chars]',2021)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Everything))