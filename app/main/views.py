from flask import render_template
from . import main
from ..request import get_sources,get_articles,get_everything

# # Views



@main.route('/')
def index():

    '''
    
    View root page function that returns the index page and its data

    '''

    title = 'Home - Welcome to Know It all'
    apple = get_sources()
    every = get_everything()


    return render_template('index.html' , title = title  , apple =apple ,every = every)





@main.route('/source/<name>')

def news(name):

    '''
     View root page function that returns the index page and its data

    '''
    news = get_articles(name)

    return render_template('source.html',news=news)





