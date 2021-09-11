from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles,get_everything,search_news

# # Views



@main.route('/')
def index():

    '''
    
    View root page function that returns the index page and its data

    '''

    title = 'Home - Welcome to Know It all'
    apple = get_sources()
    every = get_everything()
    search_all_news = request.args.get('news_query')
    if search_all_news:
        return redirect(url_for('main.search',search_news_name = search_all_news))
    else:
        return render_template('index.html' , title = title  , apple =apple ,every = every)





@main.route('/source/<name>')

def news(name):

    '''
     View root page function that returns the index page and its data

    '''
    news = get_articles(name)

    return render_template('source.html',news=news)




@main.route('/search/<search_news_name>')

def search(search_news_name):

    '''

    View function to display the search results

    '''

    news_name_list = search_news_name.split(" ")

    news_format = "+".join(news_name_list)

    searched_news = search_news(news_format)

    title = f'search results for {search_news_name}'


    return render_template('search.html',title = title,news = searched_news)



