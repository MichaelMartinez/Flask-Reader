from flask import Flask, render_template
# Import flask-bootstrap extension from extension namespace
from flask.ext.bootstrap import Bootstrap
# Import flask moment stuff
from flask.ext.moment import Moment

from flask.ext.script import Manager
import os
from rss_feed import get_sorted_posts, get_posts, get_single_blog

# set up base directory
basedir = os.path.abspath(os.path.dirname(__file__))

'''----------APP SETUP-------------'''
app = Flask(__name__)

# Set secret key for csrf in WTF forms
app.config['SECRET_KEY'] = 'kjer9034-09uei0909KW454()%(Q#)(I)(IKJWEI'

# initialize flask bootstrap
bootstrap = Bootstrap(app)

# init flask moment to add simple date/time to templates
moment = Moment(app)

# Flask Script
manager = Manager(app)

'''-----------------^^^^-----------------'''


@app.route('/')
def index():
    page_title = 'Today\'s Posts from all feeds'
    posts = get_posts()
    my_posts = get_sorted_posts(posts)
    # TODO: async or pull from DB or something... thing is sslllooowwww.

    return render_template('index.html', my_posts=my_posts, page_title=page_title)


@app.route('/all')
def all_posts():
    page_title = 'All posts from: '
    the_posts = get_single_blog()
    return render_template('all_posts.html', the_posts=the_posts, page_title=page_title)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
