from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from sqlalchemy.sql.expression import func

from app.db import get_session, models


bp = Blueprint('articles', __name__, url_prefix='/articles')

@bp.route('/', methods = ('GET', 'POST'))
def main():
    if request.method == 'POST':
        query = request.form['query']
        calendar = request.form['calendar']
        print(query, calendar)
        
    s = get_session()
    a = s.query(models.Article).order_by(func.random())[:10]
    return render_template('articles/main.html', articles=a)



