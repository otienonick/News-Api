from flask import render_template
from . import main
from ..request import get_everything

# Views
@main.route('/')
def index():

    '''
    
    View root page function that returns the index page and its data

    '''

    title = 'Home - Welcome to  AllinAll'
    apple = get_everything()

    return render_template('index.html' , title = title , apple = apple)



