from flask import render_template, request, redirect, url_for
from . import main
from ..models import Source, Article
from ..requests import get_sources, get_articles

#views
@main.route('/')
def index():
    '''
    view root function that returns the index page and its data
    '''

    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    general_news = get_sources('general')
    health_news = get_sources('health')
    science_news = get_sources('science')
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')

    title = 'Welcome to Global News'

    return render_template('index.html', title=title, business=business_news, entertainment=entertainment_news, general=general_news, health=health_news, science=science_news, sports=sports_news, technology=technology_news)


@main.route('/articles/<source>')
def articles(source):
    '''
    View articles from source
    '''
    articles = get_articles(source)
    return render_template('article.html', articles=articles)