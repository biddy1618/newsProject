import os
import pickle

from flask import Flask, render_template, url_for

from pymystem3 import Mystem

from .db import init_db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if app.config['ENV'] == 'development':
        app.config.from_object('config.development')
    elif app.config['ENV'] == 'testing':
        app.config.from_object('config.testing')
    else:
        app.config.from_pyfile('production.py')
    

    load_search(app)
    init_db(app)
    
    # test
    @app.route('/hello')
    def hello():
        return render_template('base.html')
    
    from .views import base
    app.register_blueprint(base.bp)

    from .views import articles
    app.register_blueprint(articles.bp)

    return app


def load_search(app):

    app._mystem = Mystem()
    
    tfidf_search = {
        'tfidf_index': pickle.load(open(app.config['DATA_PATH'] + '/search/tfidf_index.pkl', 'rb')),
        'tfidf_body': pickle.load(open(app.config['DATA_PATH'] + '/search/tfidf_body.pkl', 'rb')),
        'tfidf_body_matrix': pickle.load(open(app.config['DATA_PATH'] + 'search/tfidf_body_matrix.pkl', 'rb')),
        'tfidf_title': pickle.load(open(app.config['DATA_PATH'] + 'search/tfidf_title.pkl', 'rb')),
        'tfidf_title_matrix': pickle.load(open(app.config['DATA_PATH'] + 'search/tfidf_title_matrix.pkl', 'rb')),
    }

    app.tfidf_search = tfidf_search