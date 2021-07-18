from app.views.articles import index
import os
from flask import Flask, render_template

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