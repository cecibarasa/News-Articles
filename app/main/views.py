from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and
    its data
    '''

    #get general sources
    political_sources = get_sources('political')
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    business_sources = get_sources('business')
    health_sources = get_sources('health')
    science_sources = get_sources('science')

    title = 'Home - Welcome to the best Online News Website'
    return render_template('index.html',business = business_sources,health=health_sources,science=science_sources,title=title,sports = sports_sources, technology = technology_sources,entertainment = entertainment_sources ,general=general_sources)

@main.route('/news/<id>')
def news(id):
    '''
    view page function that returns the news articles and its data
    '''
    articles = get_articles(id)
    title = 'Home - Welcome to the best Online News Website'

    return render_template('news.html', articles=articles, title=title)