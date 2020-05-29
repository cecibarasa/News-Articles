import unittest
from datetime import datetime
from app.models import Sources, Articles

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('CNN','CNN News','Cable News Newtork that is a leader in providing news worldwide','cnn.com','general','U.S.A','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'CNN')
        self.assertEquals(self.new_source.name,'CNN News')
        self.assertEquals(self.new_source.description,'Cable News Newtork that is a leader in providing news worldwide')
        self.assertEquals(self.new_source.url,'cnn.com')
        self.assertEquals(self.new_source.category,'general')  
        

        self.assertEquals(self.new_source.country,'U.S.A')
        self.assertEquals(self.new_source.language,'en')

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles ('CNN','Cecilia Barasa','Centonomy should help Africa grow','A look at how centonomy can grow Africas blue economy','centonomy.com','centonomy.com/1245.jpeg','2018-11-14T10:57:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.author,'Amira Mugure')
        self.assertEquals(self.new_article.title,'Centonomy should help Africa grow')
        self.assertEquals(self.new_article.description,'A look at how centonomy can grow Africas blue economy')
        self.assertEquals(self.new_article.url,'centonomy.com')
        self.assertEquals(self.new_article.image,'centonomy.com/1245.jpeg')
        self.assertEquals(self.new_article.date,'2018-11-14T10:57:16Z')