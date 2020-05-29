import unittest
from app.models import Update


class UpdateTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Update class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_update = Update('Google News','Cecilia Barasa','NY times under fire','Pretty good','https://image.tmdb.org/t/p/w500/khsjha27hbs','www.foxnews.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_update,Update))